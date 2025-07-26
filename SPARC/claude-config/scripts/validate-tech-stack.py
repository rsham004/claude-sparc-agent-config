#!/usr/bin/env python3
"""
Technology Stack Validation Script

Enforces strict compliance with approved technology stack as defined in technology-lock.json.
Scans code files for unauthorized imports, dependencies, and technology usage.
"""

import json
import ast
import re
import sys
import os
import argparse
import subprocess
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional

class TechStackValidator:
    def __init__(self, tech_lock_file: str, strict_mode: bool = True):
        self.tech_lock_file = tech_lock_file
        self.strict_mode = strict_mode
        self.approved_tech = self._load_tech_lock()
        self.violations = []
        
    def _load_tech_lock(self) -> Dict:
        """Load approved technologies from technology-lock.json"""
        try:
            with open(self.tech_lock_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"❌ Technology lock file not found: {self.tech_lock_file}")
            print("   Solution Architect must create this file first!")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON in technology lock file: {e}")
            sys.exit(1)
    
    def _get_approved_packages(self) -> Set[str]:
        """Extract all approved package names from tech lock"""
        approved = set()
        
        # Frontend packages
        if 'frontend' in self.approved_tech:
            for category, packages in self.approved_tech['frontend'].items():
                if isinstance(packages, dict):
                    approved.update(packages.keys())
                elif isinstance(packages, list):
                    approved.update(packages)
        
        # Backend packages  
        if 'backend' in self.approved_tech:
            for category, packages in self.approved_tech['backend'].items():
                if isinstance(packages, dict):
                    approved.update(packages.keys())
                elif isinstance(packages, list):
                    approved.update(packages)
        
        # Database packages
        if 'database' in self.approved_tech:
            for category, packages in self.approved_tech['database'].items():
                if isinstance(packages, dict):
                    approved.update(packages.keys())
                elif isinstance(packages, list):
                    approved.update(packages)
        
        return approved
    
    def _check_python_imports(self, file_path: str) -> List[Dict]:
        """Check Python file for unauthorized imports"""
        violations = []
        approved_packages = self._get_approved_packages()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse AST to find imports
            try:
                tree = ast.parse(content)
            except SyntaxError:
                return violations  # Skip files with syntax errors
            
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        package = alias.name.split('.')[0]
                        if package not in approved_packages and not self._is_stdlib(package):
                            violations.append({
                                'file': file_path,
                                'line': node.lineno,
                                'type': 'unauthorized_import',
                                'package': package,
                                'full_import': alias.name,
                                'approved_alternatives': self._suggest_alternatives(package)
                            })
                
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        package = node.module.split('.')[0]
                        if package not in approved_packages and not self._is_stdlib(package):
                            violations.append({
                                'file': file_path,
                                'line': node.lineno,
                                'type': 'unauthorized_from_import',
                                'package': package,
                                'full_import': node.module,
                                'approved_alternatives': self._suggest_alternatives(package)
                            })
        
        except Exception as e:
            print(f"⚠️  Warning: Could not parse {file_path}: {e}")
        
        return violations
    
    def _check_javascript_imports(self, file_path: str) -> List[Dict]:
        """Check JavaScript/TypeScript file for unauthorized imports"""
        violations = []
        approved_packages = self._get_approved_packages()
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find import statements
            import_patterns = [
                r"import\s+.*?\s+from\s+['\"]([^'\"]+)['\"]",  # import ... from 'package'
                r"import\s+['\"]([^'\"]+)['\"]",                # import 'package'
                r"require\s*\(\s*['\"]([^'\"]+)['\"]\s*\)",     # require('package')
            ]
            
            for pattern in import_patterns:
                matches = re.finditer(pattern, content, re.MULTILINE)
                for match in matches:
                    package_path = match.group(1)
                    
                    # Skip relative imports
                    if package_path.startswith('.') or package_path.startswith('/'):
                        continue
                    
                    # Extract package name (first part before /)
                    package = package_path.split('/')[0]
                    
                    # Skip Node.js built-ins
                    if self._is_node_builtin(package):
                        continue
                    
                    if package not in approved_packages:
                        line_num = content[:match.start()].count('\n') + 1
                        violations.append({
                            'file': file_path,
                            'line': line_num,
                            'type': 'unauthorized_import',
                            'package': package,
                            'full_import': package_path,
                            'approved_alternatives': self._suggest_alternatives(package)
                        })
        
        except Exception as e:
            print(f"⚠️  Warning: Could not parse {file_path}: {e}")
        
        return violations
    
    def _check_package_json(self, file_path: str) -> List[Dict]:
        """Check package.json for unauthorized dependencies"""
        violations = []
        approved_packages = self._get_approved_packages()
        
        try:
            with open(file_path, 'r') as f:
                package_data = json.load(f)
            
            # Check dependencies
            for dep_type in ['dependencies', 'devDependencies', 'peerDependencies']:
                if dep_type in package_data:
                    for package, version in package_data[dep_type].items():
                        if package not in approved_packages:
                            violations.append({
                                'file': file_path,
                                'line': None,
                                'type': 'unauthorized_dependency',
                                'package': package,
                                'version': version,
                                'dependency_type': dep_type,
                                'approved_alternatives': self._suggest_alternatives(package)
                            })
        
        except Exception as e:
            print(f"⚠️  Warning: Could not parse {file_path}: {e}")
        
        return violations
    
    def _check_requirements_txt(self, file_path: str) -> List[Dict]:
        """Check requirements.txt for unauthorized packages"""
        violations = []
        approved_packages = self._get_approved_packages()
        
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
            
            for line_num, line in enumerate(lines, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                
                # Extract package name (before ==, >=, etc.)
                package = re.split(r'[=<>!]', line)[0].strip()
                
                if package not in approved_packages:
                    violations.append({
                        'file': file_path,
                        'line': line_num,
                        'type': 'unauthorized_requirement',
                        'package': package,
                        'full_line': line,
                        'approved_alternatives': self._suggest_alternatives(package)
                    })
        
        except Exception as e:
            print(f"⚠️  Warning: Could not parse {file_path}: {e}")
        
        return violations
    
    def _is_stdlib(self, package: str) -> bool:
        """Check if package is Python standard library"""
        stdlib_packages = {
            'os', 'sys', 'json', 'datetime', 'time', 'random', 'math', 'collections',
            'itertools', 'functools', 'operator', 're', 'string', 'io', 'pathlib',
            'urllib', 'http', 'email', 'html', 'xml', 'sqlite3', 'csv', 'configparser',
            'logging', 'unittest', 'doctest', 'argparse', 'subprocess', 'threading',
            'multiprocessing', 'asyncio', 'concurrent', 'queue', 'socket', 'ssl',
            'hashlib', 'hmac', 'secrets', 'uuid', 'base64', 'binascii', 'struct',
            'codecs', 'locale', 'gettext', 'pickle', 'copyreg', 'copy', 'pprint',
            'reprlib', 'enum', 'types', 'weakref', 'gc', 'inspect', 'site'
        }
        return package in stdlib_packages
    
    def _is_node_builtin(self, package: str) -> bool:
        """Check if package is Node.js built-in module"""
        builtin_modules = {
            'assert', 'buffer', 'child_process', 'cluster', 'crypto', 'dgram',
            'dns', 'domain', 'events', 'fs', 'http', 'https', 'net', 'os',
            'path', 'punycode', 'querystring', 'readline', 'repl', 'stream',
            'string_decoder', 'tls', 'tty', 'url', 'util', 'v8', 'vm', 'zlib'
        }
        return package in builtin_modules
    
    def _suggest_alternatives(self, package: str) -> List[str]:
        """Suggest approved alternatives for unauthorized package"""
        approved_packages = self._get_approved_packages()
        
        # Simple similarity matching
        suggestions = []
        for approved in approved_packages:
            if (package.lower() in approved.lower() or 
                approved.lower() in package.lower() or
                self._similar_names(package, approved)):
                suggestions.append(approved)
        
        return suggestions[:3]  # Limit to top 3 suggestions
    
    def _similar_names(self, name1: str, name2: str) -> bool:
        """Check if two package names are similar"""
        # Simple similarity check
        return (abs(len(name1) - len(name2)) <= 2 and 
                sum(c1 == c2 for c1, c2 in zip(name1.lower(), name2.lower())) >= min(len(name1), len(name2)) * 0.7)
    
    def validate_file(self, file_path: str) -> List[Dict]:
        """Validate a single file for technology compliance"""
        file_ext = Path(file_path).suffix.lower()
        
        if file_ext in ['.py']:
            return self._check_python_imports(file_path)
        elif file_ext in ['.js', '.jsx', '.ts', '.tsx', '.mjs']:
            return self._check_javascript_imports(file_path)
        elif Path(file_path).name == 'package.json':
            return self._check_package_json(file_path)
        elif Path(file_path).name in ['requirements.txt', 'requirements-dev.txt']:
            return self._check_requirements_txt(file_path)
        
        return []
    
    def validate_directory(self, directory: str = '.') -> List[Dict]:
        """Validate all files in directory recursively"""
        all_violations = []
        
        # File patterns to check
        patterns = [
            '**/*.py', '**/*.js', '**/*.jsx', '**/*.ts', '**/*.tsx', '**/*.mjs',
            '**/package.json', '**/requirements*.txt'
        ]
        
        for pattern in patterns:
            for file_path in Path(directory).glob(pattern):
                if self._should_skip_file(str(file_path)):
                    continue
                
                violations = self.validate_file(str(file_path))
                all_violations.extend(violations)
        
        return all_violations
    
    def _should_skip_file(self, file_path: str) -> bool:
        """Check if file should be skipped during validation"""
        skip_patterns = [
            'node_modules/', '.git/', '__pycache__/', '.pytest_cache/',
            'venv/', 'env/', '.venv/', 'dist/', 'build/', '.next/',
            'coverage/', '.nyc_output/', '.tox/', 'htmlcov/'
        ]
        
        return any(pattern in file_path for pattern in skip_patterns)
    
    def create_github_issue(self, violations: List[Dict]) -> None:
        """Create GitHub issue for technology violations"""
        if not violations:
            return
        
        # Group violations by type
        violation_summary = {}
        for violation in violations:
            v_type = violation['type']
            if v_type not in violation_summary:
                violation_summary[v_type] = []
            violation_summary[v_type].append(violation)
        
        # Create issue body
        issue_body = "🚨 **TECHNOLOGY STACK VIOLATIONS DETECTED**\\n\\n"
        issue_body += f"**Total Violations:** {len(violations)}\\n\\n"
        
        for v_type, v_list in violation_summary.items():
            issue_body += f"### {v_type.replace('_', ' ').title()} ({len(v_list)})\\n"
            for violation in v_list[:5]:  # Limit to first 5 per type
                issue_body += f"- **File:** `{violation['file']}`\\n"
                if violation.get('line'):
                    issue_body += f"  **Line:** {violation['line']}\\n"
                issue_body += f"  **Package:** `{violation['package']}`\\n"
                if violation.get('approved_alternatives'):
                    issue_body += f"  **Approved Alternatives:** {', '.join(violation['approved_alternatives'])}\\n"
                issue_body += "\\n"
        
        issue_body += "\\n**IMMEDIATE ACTIONS REQUIRED:**\\n"
        issue_body += "1. Remove all unauthorized technologies\\n"
        issue_body += "2. Replace with approved alternatives from technology-lock.json\\n"
        issue_body += "3. Update all dependent code\\n"
        issue_body += "4. Run validation again to verify compliance\\n"
        issue_body += "\\n**NO FURTHER DEVELOPMENT UNTIL RESOLVED**"
        
        # Create GitHub issue
        try:
            result = subprocess.run([
                'gh', 'issue', 'create',
                '--title', f'🚨 CRITICAL: {len(violations)} Technology Violations Detected',
                '--label', 'tech-violation,critical,enforcement',
                '--body', issue_body
            ], capture_output=True, text=True, check=True)
            
            print(f"✅ GitHub issue created for violations")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to create GitHub issue: {e}")
            print("Please ensure GitHub CLI is authenticated and repository is initialized")
    
    def print_violations(self, violations: List[Dict]) -> None:
        """Print violations in a formatted way"""
        if not violations:
            print("✅ No technology violations detected")
            return
        
        print(f"❌ Found {len(violations)} technology violations:")
        print("=" * 60)
        
        for i, violation in enumerate(violations, 1):
            print(f"\\n{i}. {violation['type'].replace('_', ' ').title()}")
            print(f"   File: {violation['file']}")
            if violation.get('line'):
                print(f"   Line: {violation['line']}")
            print(f"   Package: {violation['package']}")
            
            if violation.get('approved_alternatives'):
                print(f"   Approved alternatives: {', '.join(violation['approved_alternatives'])}")
            
            print(f"   Severity: {'CRITICAL' if self.strict_mode else 'WARNING'}")

def main():
    parser = argparse.ArgumentParser(description='Validate technology stack compliance')
    parser.add_argument('--tech-lock', default='technology-lock.json',
                       help='Path to technology-lock.json file')
    parser.add_argument('--file', help='Validate specific file')
    parser.add_argument('--directory', default='.', help='Directory to validate')
    parser.add_argument('--strict-mode', action='store_true', default=True,
                       help='Enable strict mode (default)')
    parser.add_argument('--create-issue', action='store_true',
                       help='Create GitHub issue for violations')
    parser.add_argument('--pre-commit', action='store_true',
                       help='Run in pre-commit mode')
    parser.add_argument('--summary', action='store_true',
                       help='Show summary only')
    
    args = parser.parse_args()
    
    validator = TechStackValidator(args.tech_lock, args.strict_mode)
    
    # Validate files
    if args.file:
        violations = validator.validate_file(args.file)
    else:
        violations = validator.validate_directory(args.directory)
    
    # Handle results
    if args.summary:
        if violations:
            print(f"❌ Technology violations: {len(violations)}")
        else:
            print("✅ Technology compliance: PASSED")
    else:
        validator.print_violations(violations)
    
    # Create GitHub issue if requested or in strict mode
    if violations and (args.create_issue or args.strict_mode):
        validator.create_github_issue(violations)
    
    # Exit with error code if violations found in strict mode
    if violations and (args.strict_mode or args.pre_commit):
        sys.exit(1)

if __name__ == '__main__':
    main()