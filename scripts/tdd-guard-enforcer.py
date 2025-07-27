#!/usr/bin/env python3
"""
TDD-Guard Enforcement System
Intercepts file operations and enforces test-driven development practices
"""

import os
import sys
import ast
import re
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import json

@dataclass
class TDDViolation:
    """Represents a TDD violation that needs to be addressed"""
    file_path: str
    violation_type: str
    description: str
    severity: str
    line_number: Optional[int] = None
    suggested_fix: Optional[str] = None

class TDDGuardEnforcer:
    """Enforces TDD practices by analyzing file changes and test coverage"""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.test_patterns = [
            "**/test_*.py", "**/tests/*.py", "**/*_test.py",
            "**/test*.js", "**/tests/*.js", "**/*.test.js",
            "**/test*.ts", "**/tests/*.ts", "**/*.test.ts"
        ]
        self.src_patterns = [
            "src/**/*.py", "lib/**/*.py", "app/**/*.py",
            "src/**/*.js", "lib/**/*.js", "app/**/*.js",
            "src/**/*.ts", "lib/**/*.ts", "app/**/*.ts"
        ]
        
    def validate_tdd_compliance(self, file_path: str, content: str) -> List[TDDViolation]:
        """Validate that file changes follow TDD practices"""
        violations = []
        
        # Check if this is a source file
        if not self._is_source_file(file_path):
            return violations
        
        # Check for tests before implementation
        if not self._has_corresponding_tests(file_path):
            violations.append(TDDViolation(
                file_path=file_path,
                violation_type="missing_tests",
                description="Implementation file has no corresponding test file",
                severity="critical",
                suggested_fix=f"Create test file for {file_path}"
            ))
        
        # Check for over-implementation
        complexity_violations = self._check_complexity(file_path, content)
        violations.extend(complexity_violations)
        
        # Check for untested functions
        untested_violations = self._check_untested_functions(file_path, content)
        violations.extend(untested_violations)
        
        return violations
    
    def _is_source_file(self, file_path: str) -> bool:
        """Check if file is a source file that requires tests"""
        file_path = Path(file_path)
        
        # Skip test files themselves
        if any(pattern in str(file_path) for pattern in ["test", "spec", "__pycache__"]):
            return False
        
        # Check if it's a source file
        return file_path.suffix in ['.py', '.js', '.ts', '.jsx', '.tsx']
    
    def _has_corresponding_tests(self, file_path: str) -> bool:
        """Check if source file has corresponding test file"""
        file_path = Path(file_path)
        base_name = file_path.stem
        
        # Possible test file patterns
        test_patterns = [
            f"test_{base_name}.py",
            f"{base_name}_test.py",
            f"test{base_name}.py",
            f"tests/{base_name}.py",
            f"test_{base_name}.js",
            f"{base_name}.test.js",
            f"tests/{base_name}.js",
            f"test_{base_name}.ts",
            f"{base_name}.test.ts",
            f"tests/{base_name}.ts"
        ]
        
        # Check in same directory and tests directory
        search_dirs = [file_path.parent, file_path.parent / "tests", self.project_root / "tests"]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                for pattern in test_patterns:
                    if (search_dir / pattern).exists():
                        return True
        
        return False
    
    def _check_complexity(self, file_path: str, content: str) -> List[TDDViolation]:
        """Check for over-implementation (too complex for TDD cycle)"""
        violations = []
        
        if file_path.endswith('.py'):
            violations.extend(self._check_python_complexity(file_path, content))
        elif file_path.endswith(('.js', '.ts')):
            violations.extend(self._check_javascript_complexity(file_path, content))
        
        return violations
    
    def _check_python_complexity(self, file_path: str, content: str) -> List[TDDViolation]:
        """Check Python code complexity"""
        violations = []
        
        try:
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    # Check function length (should be small in TDD)
                    func_lines = node.end_lineno - node.lineno
                    if func_lines > 20:
                        violations.append(TDDViolation(
                            file_path=file_path,
                            violation_type="over_implementation",
                            description=f"Function '{node.name}' is too long ({func_lines} lines)",
                            severity="medium",
                            line_number=node.lineno,
                            suggested_fix="Break function into smaller, testable units"
                        ))
                    
                    # Check cyclomatic complexity
                    complexity = self._calculate_cyclomatic_complexity(node)
                    if complexity > 5:
                        violations.append(TDDViolation(
                            file_path=file_path,
                            violation_type="high_complexity",
                            description=f"Function '{node.name}' has high complexity ({complexity})",
                            severity="medium",
                            line_number=node.lineno,
                            suggested_fix="Simplify function logic and add more unit tests"
                        ))
        
        except SyntaxError:
            violations.append(TDDViolation(
                file_path=file_path,
                violation_type="syntax_error",
                description="File has syntax errors",
                severity="critical",
                suggested_fix="Fix syntax errors before proceeding"
            ))
        
        return violations
    
    def _check_javascript_complexity(self, file_path: str, content: str) -> List[TDDViolation]:
        """Check JavaScript/TypeScript code complexity"""
        violations = []
        
        # Simple heuristic checks for JS/TS
        lines = content.split('\n')
        in_function = False
        function_start = 0
        function_name = ""
        brace_count = 0
        
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            
            # Detect function start
            if re.match(r'(function\s+\w+|const\s+\w+\s*=.*=>|\w+\s*\([^)]*\)\s*{)', stripped):
                if not in_function:
                    in_function = True
                    function_start = i
                    function_name = re.search(r'(\w+)', stripped).group(1) if re.search(r'(\w+)', stripped) else "anonymous"
                    brace_count = 0
            
            # Count braces to track function scope
            if in_function:
                brace_count += stripped.count('{') - stripped.count('}')
                
                # Function ended
                if brace_count <= 0 and i > function_start:
                    func_length = i - function_start
                    if func_length > 20:
                        violations.append(TDDViolation(
                            file_path=file_path,
                            violation_type="over_implementation",
                            description=f"Function '{function_name}' is too long ({func_length} lines)",
                            severity="medium",
                            line_number=function_start,
                            suggested_fix="Break function into smaller, testable units"
                        ))
                    in_function = False
        
        return violations
    
    def _calculate_cyclomatic_complexity(self, node: ast.FunctionDef) -> int:
        """Calculate cyclomatic complexity of a Python function"""
        complexity = 1  # Base complexity
        
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.While, ast.For, ast.AsyncFor)):
                complexity += 1
            elif isinstance(child, ast.ExceptHandler):
                complexity += 1
            elif isinstance(child, ast.BoolOp):
                complexity += len(child.values) - 1
        
        return complexity
    
    def _check_untested_functions(self, file_path: str, content: str) -> List[TDDViolation]:
        """Check for functions that appear to be untested"""
        violations = []
        
        if not file_path.endswith('.py'):
            return violations
        
        try:
            tree = ast.parse(content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and not node.name.startswith('_'):
                    # This is a simplified check - in reality, we'd cross-reference with test files
                    # For now, we'll just check if there are obvious test indicators
                    if not self._function_appears_tested(node.name, file_path):
                        violations.append(TDDViolation(
                            file_path=file_path,
                            violation_type="untested_function",
                            description=f"Function '{node.name}' appears to have no tests",
                            severity="high",
                            line_number=node.lineno,
                            suggested_fix=f"Write tests for function '{node.name}' before implementation"
                        ))
        
        except SyntaxError:
            pass  # Already caught in complexity check
        
        return violations
    
    def _function_appears_tested(self, function_name: str, file_path: str) -> bool:
        """Check if function appears to be tested (simplified heuristic)"""
        # Find corresponding test files
        file_path = Path(file_path)
        base_name = file_path.stem
        
        test_files = []
        search_dirs = [file_path.parent, file_path.parent / "tests", self.project_root / "tests"]
        
        for search_dir in search_dirs:
            if search_dir.exists():
                test_files.extend(search_dir.glob(f"test_{base_name}.*"))
                test_files.extend(search_dir.glob(f"{base_name}_test.*"))
                test_files.extend(search_dir.glob(f"test{base_name}.*"))
        
        # Check if function name appears in test files
        for test_file in test_files:
            try:
                with open(test_file, 'r') as f:
                    test_content = f.read()
                    if function_name in test_content:
                        return True
            except Exception:
                continue
        
        return False
    
    def run_tests_and_check_coverage(self) -> Tuple[bool, Dict]:
        """Run tests and check coverage"""
        results = {
            "tests_passed": False,
            "coverage_percentage": 0,
            "missing_coverage": [],
            "test_output": ""
        }
        
        try:
            # Try to run pytest with coverage
            cmd = ["python", "-m", "pytest", "--cov=.", "--cov-report=json", "--cov-report=term"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            
            results["test_output"] = result.stdout + result.stderr
            results["tests_passed"] = result.returncode == 0
            
            # Parse coverage report
            coverage_file = self.project_root / "coverage.json"
            if coverage_file.exists():
                with open(coverage_file) as f:
                    coverage_data = json.load(f)
                    results["coverage_percentage"] = coverage_data.get("totals", {}).get("percent_covered", 0)
                    
                    # Find files with low coverage
                    for file_path, file_data in coverage_data.get("files", {}).items():
                        if file_data.get("summary", {}).get("percent_covered", 0) < 90:
                            results["missing_coverage"].append({
                                "file": file_path,
                                "coverage": file_data.get("summary", {}).get("percent_covered", 0)
                            })
        
        except Exception as e:
            results["test_output"] = f"Error running tests: {e}"
        
        return results["tests_passed"], results
    
    def validate_commit_readiness(self) -> Tuple[bool, List[TDDViolation]]:
        """Check if repository is ready for commit based on TDD principles"""
        violations = []
        
        # Run tests and check coverage
        tests_passed, coverage_results = self.run_tests_and_check_coverage()
        
        if not tests_passed:
            violations.append(TDDViolation(
                file_path=".",
                violation_type="failing_tests",
                description="Tests are failing",
                severity="critical",
                suggested_fix="Fix failing tests before committing"
            ))
        
        if coverage_results["coverage_percentage"] < 90:
            violations.append(TDDViolation(
                file_path=".",
                violation_type="low_coverage",
                description=f"Test coverage is {coverage_results['coverage_percentage']:.1f}% (required: 90%)",
                severity="high",
                suggested_fix="Add tests to increase coverage above 90%"
            ))
        
        # Check for files with low coverage
        for file_info in coverage_results["missing_coverage"]:
            violations.append(TDDViolation(
                file_path=file_info["file"],
                violation_type="file_low_coverage",
                description=f"File has {file_info['coverage']:.1f}% coverage",
                severity="medium",
                suggested_fix=f"Add tests for {file_info['file']}"
            ))
        
        return len(violations) == 0, violations
    
    def enforce_tdd_on_file_change(self, file_path: str, content: str) -> Tuple[bool, List[TDDViolation]]:
        """Main enforcement function called when files are modified"""
        violations = self.validate_tdd_compliance(file_path, content)
        
        # Critical violations block the operation
        critical_violations = [v for v in violations if v.severity == "critical"]
        
        return len(critical_violations) == 0, violations
    
    def generate_tdd_guidance(self, violations: List[TDDViolation]) -> str:
        """Generate helpful guidance for resolving TDD violations"""
        if not violations:
            return "✅ All TDD checks passed!"
        
        guidance = ["🛡️ TDD-Guard Violations Found:", ""]
        
        for i, violation in enumerate(violations, 1):
            severity_emoji = {
                "critical": "🚨",
                "high": "❗",
                "medium": "⚠️",
                "low": "📝"
            }
            
            emoji = severity_emoji.get(violation.severity, "📝")
            guidance.append(f"{i}. {emoji} {violation.violation_type.upper()}")
            guidance.append(f"   File: {violation.file_path}")
            if violation.line_number:
                guidance.append(f"   Line: {violation.line_number}")
            guidance.append(f"   Issue: {violation.description}")
            if violation.suggested_fix:
                guidance.append(f"   Fix: {violation.suggested_fix}")
            guidance.append("")
        
        guidance.extend([
            "🔄 TDD Cycle Reminder:",
            "1. RED: Write a failing test first",
            "2. GREEN: Write minimal code to pass the test", 
            "3. REFACTOR: Clean up code while keeping tests green",
            "",
            "📋 Run 'python scripts/tdd-guard-enforcer.py validate-commit' to check readiness"
        ])
        
        return "\n".join(guidance)

def main():
    """CLI interface for TDD-Guard enforcement"""
    if len(sys.argv) < 2:
        print("Usage: python tdd-guard-enforcer.py <command> [args...]")
        print("Commands:")
        print("  validate-file <file_path>")
        print("  validate-commit")
        print("  check-coverage")
        print("  run-tests")
        sys.exit(1)
    
    command = sys.argv[1]
    enforcer = TDDGuardEnforcer()
    
    if command == "validate-file":
        if len(sys.argv) < 3:
            print("Usage: validate-file <file_path>")
            sys.exit(1)
        
        file_path = sys.argv[2]
        if not os.path.exists(file_path):
            print(f"❌ File not found: {file_path}")
            sys.exit(1)
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        compliant, violations = enforcer.enforce_tdd_on_file_change(file_path, content)
        
        if compliant:
            print("✅ File passes TDD validation")
        else:
            print(enforcer.generate_tdd_guidance(violations))
            sys.exit(1)
    
    elif command == "validate-commit":
        ready, violations = enforcer.validate_commit_readiness()
        
        if ready:
            print("✅ Repository ready for commit")
        else:
            print(enforcer.generate_tdd_guidance(violations))
            sys.exit(1)
    
    elif command == "check-coverage":
        tests_passed, results = enforcer.run_tests_and_check_coverage()
        
        print(f"Tests Passed: {'✅' if tests_passed else '❌'}")
        print(f"Coverage: {results['coverage_percentage']:.1f}%")
        
        if results['missing_coverage']:
            print("\nFiles with low coverage:")
            for file_info in results['missing_coverage']:
                print(f"  {file_info['file']}: {file_info['coverage']:.1f}%")
    
    elif command == "run-tests":
        tests_passed, results = enforcer.run_tests_and_check_coverage()
        print(results['test_output'])
        sys.exit(0 if tests_passed else 1)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()