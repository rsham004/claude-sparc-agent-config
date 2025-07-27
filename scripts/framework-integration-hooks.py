#!/usr/bin/env python3
"""
SPARC Framework Integration Hooks
Provides Claude Code integration points for automatic framework enforcement
"""

import os
import sys
import json
from pathlib import Path
from typing import Dict, List, Optional, Any
import subprocess

class FrameworkIntegrationHooks:
    """Integration hooks for Claude Code and SPARC framework"""
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.hooks_config = self._load_hooks_config()
        
    def _load_hooks_config(self) -> Dict[str, Any]:
        """Load hooks configuration"""
        config_file = self.project_root / ".claude" / "hooks.json"
        if config_file.exists():
            with open(config_file) as f:
                return json.load(f)
        
        # Default configuration
        return {
            "tdd_guard_enabled": True,
            "workflow_enforcement": True,
            "auto_issue_creation": True,
            "quality_gates": True,
            "technology_lock_enforcement": True
        }
    
    def pre_file_edit_hook(self, file_path: str, operation: str) -> bool:
        """Called before file edit operations"""
        if not self.hooks_config.get("tdd_guard_enabled", True):
            return True
        
        # For source files, ensure TDD compliance
        if self._is_source_file(file_path):
            return self._enforce_tdd_pre_edit(file_path, operation)
        
        # For design documents, ensure workflow compliance
        if self._is_design_document(file_path):
            return self._enforce_workflow_pre_edit(file_path, operation)
        
        return True
    
    def post_file_edit_hook(self, file_path: str, content: str, operation: str) -> bool:
        """Called after file edit operations"""
        success = True
        
        # Run TDD validation
        if self.hooks_config.get("tdd_guard_enabled", True) and self._is_source_file(file_path):
            success &= self._validate_tdd_post_edit(file_path, content)
        
        # Run workflow validation  
        if self.hooks_config.get("workflow_enforcement", True) and self._is_design_document(file_path):
            success &= self._validate_workflow_post_edit(file_path, content)
        
        # Auto-create issues for violations
        if not success and self.hooks_config.get("auto_issue_creation", True):
            self._create_violation_issues(file_path, operation)
        
        return success
    
    def pre_commit_hook(self) -> bool:
        """Called before git commits"""
        if not self.hooks_config.get("quality_gates", True):
            return True
        
        print("🛡️ Running SPARC Framework pre-commit validation...")
        
        # Run all quality checks
        checks = [
            self._run_tdd_validation,
            self._run_workflow_validation,
            self._run_technology_lock_validation,
            self._run_test_suite
        ]
        
        all_passed = True
        for check in checks:
            try:
                if not check():
                    all_passed = False
            except Exception as e:
                print(f"❌ Check failed with error: {e}")
                all_passed = False
        
        if all_passed:
            print("✅ All pre-commit checks passed")
        else:
            print("❌ Pre-commit checks failed - commit blocked")
            self._display_resolution_guidance()
        
        return all_passed
    
    def agent_execution_hook(self, agent_name: str, phase: str) -> bool:
        """Called when SPARC agents are executed"""
        if not self.hooks_config.get("workflow_enforcement", True):
            return True
        
        print(f"🤖 Validating {agent_name} execution readiness...")
        
        # Check workflow compliance
        try:
            cmd = ["python", "scripts/sparc-workflow-enforcer.py", "check-readiness", agent_name]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode == 0:
                print(f"✅ {agent_name} ready for execution")
                return True
            else:
                print(f"❌ {agent_name} blocked by workflow violations")
                print(result.stderr)
                return False
        
        except Exception as e:
            print(f"⚠️  Could not validate agent readiness: {e}")
            return True  # Don't block if validation fails
    
    def _is_source_file(self, file_path: str) -> bool:
        """Check if file is a source code file"""
        source_extensions = {'.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.go', '.rs'}
        return Path(file_path).suffix in source_extensions
    
    def _is_design_document(self, file_path: str) -> bool:
        """Check if file is a SPARC design document"""
        design_patterns = [
            'product_requirements.md',
            'architecture_guide.md',
            'ux_design.md',
            'visual_concepts.md',
            'database_design.md',
            'api_specification.md',
            'implementation_plan.md',
            'technology-lock.json'
        ]
        
        file_name = Path(file_path).name
        return any(pattern in file_name for pattern in design_patterns)
    
    def _enforce_tdd_pre_edit(self, file_path: str, operation: str) -> bool:
        """Enforce TDD rules before editing source files"""
        # For new files, ensure tests exist first
        if operation == "create" and not self._has_corresponding_tests(file_path):
            print(f"🛡️ TDD-Guard: Cannot create {file_path} without corresponding tests")
            print("📝 Create tests first following TDD red-green-refactor cycle")
            return False
        
        return True
    
    def _enforce_workflow_pre_edit(self, file_path: str, operation: str) -> bool:
        """Enforce SPARC workflow rules before editing design documents"""
        # Check if agent is ready to generate this document
        agent_name = self._get_agent_for_document(file_path)
        if agent_name:
            try:
                cmd = ["python", "scripts/sparc-workflow-enforcer.py", "check-readiness", agent_name]
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode != 0:
                    print(f"🛡️ SPARC Workflow: Cannot edit {file_path}")
                    print(f"📋 Agent {agent_name} dependencies not met")
                    return False
            except Exception:
                pass  # Don't block if check fails
        
        return True
    
    def _validate_tdd_post_edit(self, file_path: str, content: str) -> bool:
        """Validate TDD compliance after editing"""
        try:
            cmd = ["python", "scripts/tdd-guard-enforcer.py", "validate-file", file_path]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            
            if result.returncode != 0:
                print(f"🛡️ TDD violations detected in {file_path}")
                print(result.stdout)
                return False
            
            return True
        
        except Exception as e:
            print(f"⚠️  TDD validation error: {e}")
            return True  # Don't block if validation fails
    
    def _validate_workflow_post_edit(self, file_path: str, content: str) -> bool:
        """Validate workflow compliance after editing design documents"""
        # Validate document completeness
        try:
            agent_name = self._get_agent_for_document(file_path)
            if agent_name:
                cmd = ["python", "scripts/sparc-workflow-enforcer.py", "validate-agent", agent_name]
                result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
                
                if result.returncode != 0:
                    print(f"📋 Workflow violations in {file_path}")
                    print(result.stdout)
                    return False
            
            return True
        
        except Exception as e:
            print(f"⚠️  Workflow validation error: {e}")
            return True
    
    def _get_agent_for_document(self, file_path: str) -> Optional[str]:
        """Get the agent responsible for a design document"""
        document_to_agent = {
            'product_requirements.md': 'product-manager',
            'architecture_guide.md': 'solution-architect',
            'ux_design.md': 'ux-designer',
            'visual_concepts.md': 'visual-style-specialist',
            'database_design.md': 'data-architect',
            'api_specification.md': 'senior-api-developer',
            'implementation_plan.md': 'project-planner'
        }
        
        file_name = Path(file_path).name
        return document_to_agent.get(file_name)
    
    def _has_corresponding_tests(self, file_path: str) -> bool:
        """Check if source file has corresponding tests"""
        try:
            cmd = ["python", "scripts/tdd-guard-enforcer.py", "validate-file", file_path]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            return "missing_tests" not in result.stdout
        except Exception:
            return False
    
    def _run_tdd_validation(self) -> bool:
        """Run TDD validation"""
        try:
            cmd = ["python", "scripts/tdd-guard-enforcer.py", "validate-commit"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            return result.returncode == 0
        except Exception:
            return False
    
    def _run_workflow_validation(self) -> bool:
        """Run workflow validation"""
        try:
            cmd = ["python", "scripts/sparc-workflow-enforcer.py", "status"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            return "blocking" not in result.stdout.lower()
        except Exception:
            return True  # Don't block if validation unavailable
    
    def _run_technology_lock_validation(self) -> bool:
        """Run technology lock validation"""
        tech_lock_file = self.project_root / "docs" / "design" / "technology-lock.json"
        if not tech_lock_file.exists():
            return True  # No tech lock to validate
        
        try:
            with open(tech_lock_file) as f:
                json.load(f)  # Validate JSON
            return True
        except Exception:
            print("❌ technology-lock.json is invalid")
            return False
    
    def _run_test_suite(self) -> bool:
        """Run test suite"""
        try:
            cmd = ["python", "scripts/tdd-guard-enforcer.py", "run-tests"]
            result = subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)
            return result.returncode == 0
        except Exception:
            return True  # Don't block if no tests
    
    def _create_violation_issues(self, file_path: str, operation: str):
        """Create Git issues for violations"""
        try:
            cmd = [
                "python", "scripts/git-issue-automation.py", "create-violation",
                "framework_violation", "high", "implementation", "framework-hooks",
                f"Framework violation in {file_path} during {operation}"
            ]
            subprocess.run(cmd, cwd=self.project_root)
        except Exception as e:
            print(f"⚠️  Could not create violation issue: {e}")
    
    def _display_resolution_guidance(self):
        """Display guidance for resolving violations"""
        print("\n🔧 Resolution Guidance:")
        print("1. Run: python scripts/tdd-guard-enforcer.py validate-commit")
        print("2. Run: python scripts/sparc-workflow-enforcer.py status")
        print("3. Fix any reported violations")
        print("4. Ensure all tests pass")
        print("5. Retry commit")
        print("\n📋 For detailed guidance:")
        print("   python scripts/git-issue-automation.py check-blockers")

def install_hooks():
    """Install SPARC framework hooks for Claude Code"""
    hooks_dir = Path.cwd() / ".claude" / "hooks"
    hooks_dir.mkdir(parents=True, exist_ok=True)
    
    # Create hooks configuration
    hooks_config = {
        "pre_file_edit": "python scripts/framework-integration-hooks.py pre-file-edit",
        "post_file_edit": "python scripts/framework-integration-hooks.py post-file-edit", 
        "pre_commit": "python scripts/framework-integration-hooks.py pre-commit",
        "agent_execution": "python scripts/framework-integration-hooks.py agent-execution"
    }
    
    config_file = hooks_dir / "config.json"
    with open(config_file, 'w') as f:
        json.dump(hooks_config, f, indent=2)
    
    print("✅ SPARC Framework hooks installed")
    print(f"📄 Configuration: {config_file}")

def main():
    """CLI interface for framework hooks"""
    if len(sys.argv) < 2:
        print("Usage: python framework-integration-hooks.py <command> [args...]")
        print("Commands:")
        print("  install-hooks")
        print("  pre-file-edit <file_path> <operation>")
        print("  post-file-edit <file_path> <operation>")
        print("  pre-commit")
        print("  agent-execution <agent_name> <phase>")
        sys.exit(1)
    
    command = sys.argv[1]
    hooks = FrameworkIntegrationHooks()
    
    if command == "install-hooks":
        install_hooks()
    
    elif command == "pre-file-edit":
        if len(sys.argv) < 4:
            print("Usage: pre-file-edit <file_path> <operation>")
            sys.exit(1)
        
        file_path = sys.argv[2]
        operation = sys.argv[3]
        
        if hooks.pre_file_edit_hook(file_path, operation):
            print("✅ Pre-edit validation passed")
        else:
            print("❌ Pre-edit validation failed")
            sys.exit(1)
    
    elif command == "post-file-edit":
        if len(sys.argv) < 4:
            print("Usage: post-file-edit <file_path> <operation>")
            sys.exit(1)
        
        file_path = sys.argv[2]
        operation = sys.argv[3]
        
        # Read file content
        try:
            with open(file_path, 'r') as f:
                content = f.read()
        except Exception:
            content = ""
        
        if hooks.post_file_edit_hook(file_path, content, operation):
            print("✅ Post-edit validation passed")
        else:
            print("❌ Post-edit validation failed")
            sys.exit(1)
    
    elif command == "pre-commit":
        if hooks.pre_commit_hook():
            print("✅ Pre-commit validation passed")
        else:
            print("❌ Pre-commit validation failed")
            sys.exit(1)
    
    elif command == "agent-execution":
        if len(sys.argv) < 4:
            print("Usage: agent-execution <agent_name> <phase>")
            sys.exit(1)
        
        agent_name = sys.argv[2]
        phase = sys.argv[3]
        
        if hooks.agent_execution_hook(agent_name, phase):
            print("✅ Agent execution validation passed")
        else:
            print("❌ Agent execution blocked")
            sys.exit(1)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()