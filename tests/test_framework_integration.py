#!/usr/bin/env python3
"""
Integration tests for SPARC Framework automation
Tests end-to-end functionality of all framework components
"""

import os
import sys
import json
import tempfile
import shutil
import subprocess
from pathlib import Path
import pytest
from typing import Dict, List

# Add scripts directory to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from git_issue_automation import SPARCGitIssueManager, FrameworkViolation
from tdd_guard_enforcer import TDDGuardEnforcer, TDDViolation
from sparc_workflow_enforcer import SPARCWorkflowEnforcer, WorkflowViolation

class TestFrameworkIntegration:
    """Integration tests for SPARC Framework"""
    
    @pytest.fixture
    def temp_project(self):
        """Create temporary project for testing"""
        temp_dir = tempfile.mkdtemp()
        original_cwd = os.getcwd()
        
        try:
            os.chdir(temp_dir)
            
            # Initialize git repo
            subprocess.run(["git", "init"], check=True, capture_output=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], check=True)
            subprocess.run(["git", "config", "user.name", "Test User"], check=True)
            
            # Create basic project structure
            os.makedirs("docs/design/test-project", exist_ok=True)
            os.makedirs("src", exist_ok=True)
            os.makedirs("tests", exist_ok=True)
            
            yield temp_dir
            
        finally:
            os.chdir(original_cwd)
            shutil.rmtree(temp_dir, ignore_errors=True)
    
    def test_git_issue_automation(self, temp_project):
        """Test Git issue automation system"""
        issue_manager = SPARCGitIssueManager("test-project")
        
        # Test violation creation
        violation = FrameworkViolation(
            violation_type="test_violation",
            severity="high",
            phase="implementation",
            agent="test-agent",
            description="Test violation for integration testing",
            file_path="test_file.py",
            line_number=42,
            resolution_steps=["Fix the issue", "Validate the fix"]
        )
        
        # Test issue body generation
        issue_body = issue_manager._generate_issue_body(violation)
        assert "Test violation for integration testing" in issue_body
        assert "test-agent" in issue_body
        assert "Fix the issue" in issue_body
        
        # Test label generation
        labels = issue_manager._generate_labels(violation)
        assert "sparc-framework" in labels
        assert "implementation" in labels
        assert "high" in labels
    
    def test_tdd_guard_enforcement(self, temp_project):
        """Test TDD-Guard enforcement system"""
        enforcer = TDDGuardEnforcer(temp_project)
        
        # Test Python code analysis
        python_code = '''
def complex_function(x, y, z, a, b, c):
    if x > 0:
        if y > 0:
            if z > 0:
                if a > 0:
                    if b > 0:
                        if c > 0:
                            result = x + y + z + a + b + c
                            for i in range(100):
                                result += i
                            return result
        return 0
    return -1
'''
        
        violations = enforcer.validate_tdd_compliance("test_complex.py", python_code)
        
        # Should detect over-implementation
        violation_types = [v.violation_type for v in violations]
        assert any("over_implementation" in vt or "high_complexity" in vt for vt in violation_types)
        
        # Test simple, compliant code
        simple_code = '''
def add(x, y):
    return x + y
'''
        
        violations = enforcer.validate_tdd_compliance("test_simple.py", simple_code)
        complexity_violations = [v for v in violations if v.violation_type in ["over_implementation", "high_complexity"]]
        assert len(complexity_violations) == 0
    
    def test_workflow_enforcement(self, temp_project):
        """Test SPARC workflow enforcement"""
        enforcer = SPARCWorkflowEnforcer("test-project", "docs/design")
        
        # Test agent status without documents
        status = enforcer.get_agent_status("product-manager")
        assert not status.completed
        assert status.validation_score == 0.0
        
        # Create a basic PRD
        prd_path = Path("docs/design/test-project/product_requirements.md")
        prd_path.parent.mkdir(parents=True, exist_ok=True)
        prd_content = '''
# Product Requirements Document

## Elevator Pitch
This is a test product for integration testing.

## Who is this app for
Test users who need testing functionality.

## Functional Requirements
- Test feature 1
- Test feature 2

## User Stories
As a test user, I want to test things.

## User Interface Overview
Simple test interface.

## Success Metrics
- Test metric 1
- Test metric 2

## Constraints & Assumptions
Test constraints and assumptions.

## Roadmap Overview
Test roadmap overview.
'''
        with open(prd_path, 'w') as f:
            f.write(prd_content)
        
        # Test agent status with document
        status = enforcer.get_agent_status("product-manager")
        assert status.completed
        assert status.validation_score > 0.5  # Should find most sections
        
        # Test workflow status
        workflow_status = enforcer.get_workflow_status()
        assert workflow_status["current_phase"] >= 1
        assert workflow_status["completion_percentage"] > 0
    
    def test_agent_dependency_validation(self, temp_project):
        """Test agent dependency validation"""
        enforcer = SPARCWorkflowEnforcer("test-project", "docs/design")
        
        # Try to execute solution architect without PRD
        ready, violations = enforcer.validate_agent_execution_readiness("solution-architect")
        assert not ready
        
        # Should have dependency violation
        dep_violations = [v for v in violations if v.violation_type == "missing_dependency"]
        assert len(dep_violations) > 0
        assert "product-manager" in dep_violations[0].description
        
        # Create PRD and try again
        prd_path = Path("docs/design/test-project/product_requirements.md")
        prd_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create complete PRD
        complete_prd = '''
# Product Requirements Document

## Elevator Pitch
Complete test product for dependency validation.

## Who is this app for
Target users with specific needs.

## Functional Requirements
- Feature 1: User authentication
- Feature 2: Data management
- Feature 3: Reporting

## User Stories
- As a user, I want to log in securely
- As a user, I want to manage my data
- As a user, I want to generate reports

## User Interface Overview
Modern, responsive web interface with clean design.

## Success Metrics
- User engagement rate > 80%
- Data accuracy > 99%
- Performance load time < 2s

## Constraints & Assumptions
- Web-first platform
- Modern browser support
- Cloud deployment

## Roadmap Overview
- Phase 1: Core functionality (Q1)
- Phase 2: Advanced features (Q2)
- Phase 3: Optimization (Q3)
'''
        with open(prd_path, 'w') as f:
            f.write(complete_prd)
        
        # Now solution architect should be ready
        ready, violations = enforcer.validate_agent_execution_readiness("solution-architect")
        assert ready or len([v for v in violations if v.severity == "critical"]) == 0
    
    def test_technology_lock_compliance(self, temp_project):
        """Test technology lock compliance validation"""
        enforcer = SPARCWorkflowEnforcer("test-project", "docs/design")
        
        # Create invalid technology lock
        tech_lock_path = Path("docs/design/test-project/technology-lock.json")
        tech_lock_path.parent.mkdir(parents=True, exist_ok=True)
        
        invalid_tech_lock = {"incomplete": "data"}
        with open(tech_lock_path, 'w') as f:
            json.dump(invalid_tech_lock, f)
        
        violations = enforcer._check_technology_lock_compliance()
        assert len(violations) > 0
        
        # Create valid technology lock
        valid_tech_lock = {
            "frontend": {"framework": "React", "version": "18.2.0"},
            "backend": {"framework": "FastAPI", "version": "0.104.1"},
            "database": {"type": "PostgreSQL", "version": "15.0"},
            "deployment": {"platform": "AWS", "container": "Docker"}
        }
        with open(tech_lock_path, 'w') as f:
            json.dump(valid_tech_lock, f)
        
        violations = enforcer._check_technology_lock_compliance()
        critical_violations = [v for v in violations if v.severity == "critical"]
        assert len(critical_violations) == 0
    
    def test_framework_setup_script(self, temp_project):
        """Test framework setup script functionality"""
        # Copy setup script to temp directory
        setup_script = Path(__file__).parent.parent / "setup-sparc-project.sh"
        if setup_script.exists():
            shutil.copy(setup_script, ".")
            
            # Create minimal agents directory structure
            os.makedirs("agents/colored", exist_ok=True)
            
            # Create a minimal agent file for testing
            agent_content = '''# 🔵 **Test Agent**
*Color Code: BLUE - Testing*

**Role:** Test Agent
**Context:** Testing context
**Goal:** Test goal
**Instructions:** Test instructions

## ProductFoundry.ai
Test community content
'''
            with open("agents/colored/01-product-manager.md", 'w') as f:
                f.write(agent_content)
            
            # Test setup script execution
            result = subprocess.run(
                ["bash", "setup-sparc-project.sh", "integration-test"],
                capture_output=True,
                text=True
            )
            
            # Check if setup was successful (exit code 0 or reasonable output)
            assert result.returncode == 0 or "SPARC Framework" in result.stdout
            
            # Check if expected directories were created
            assert Path(".claude/agents/integration-test").exists()
            assert Path("CLAUDE.md").exists()
    
    def test_end_to_end_workflow(self, temp_project):
        """Test complete end-to-end workflow"""
        # 1. Setup project structure
        os.makedirs("docs/design/e2e-test", exist_ok=True)
        os.makedirs("src", exist_ok=True)
        os.makedirs("tests", exist_ok=True)
        
        # 2. Create PRD (Product Manager output)
        prd_path = Path("docs/design/e2e-test/product_requirements.md")
        with open(prd_path, 'w') as f:
            f.write('''
# Product Requirements Document

## Elevator Pitch
E2E test product with complete workflow validation.

## Who is this app for
Integration test users.

## Functional Requirements
- Authentication system
- Data management
- API endpoints

## User Stories
- As a user, I want secure authentication
- As a developer, I want clean APIs

## User Interface Overview
Web-based interface with React frontend.

## Success Metrics
- Performance < 100ms response time
- 99.9% uptime

## Constraints & Assumptions
- Cloud-first deployment
- Modern browser support

## Roadmap Overview
- MVP in Q1
- Full features in Q2
''')
        
        # 3. Test workflow progression
        enforcer = SPARCWorkflowEnforcer("e2e-test", "docs/design")
        
        # Validate PRD completion
        status = enforcer.get_agent_status("product-manager")
        assert status.completed
        assert status.validation_score > 0.7
        
        # Check solution architect readiness
        ready, violations = enforcer.validate_agent_execution_readiness("solution-architect")
        assert ready
        
        # 4. Create architecture document
        arch_path = Path("docs/design/e2e-test/architecture_guide.md")
        with open(arch_path, 'w') as f:
            f.write('''
# Architecture Guide

## Architecture Overview
Microservices architecture with React frontend and FastAPI backend.

## Technology Stack
- Frontend: React 18.2.0
- Backend: FastAPI 0.104.1
- Database: PostgreSQL 15.0

## System Design
Clean separation of concerns with API-first design.

## Security Considerations
JWT authentication, HTTPS encryption, input validation.

## Performance Requirements
< 100ms response time, horizontal scaling support.

## Deployment Strategy
Docker containers on AWS with CI/CD pipeline.
''')
        
        # Create technology lock
        tech_lock_path = Path("docs/design/e2e-test/technology-lock.json")
        with open(tech_lock_path, 'w') as f:
            json.dump({
                "frontend": {"framework": "React", "version": "18.2.0"},
                "backend": {"framework": "FastAPI", "version": "0.104.1"},
                "database": {"type": "PostgreSQL", "version": "15.0"},
                "deployment": {"platform": "AWS", "container": "Docker"}
            }, f)
        
        # 5. Validate workflow progress
        workflow_status = enforcer.get_workflow_status()
        assert workflow_status["current_phase"] >= 2
        assert workflow_status["completion_percentage"] > 20
        
        # 6. Test TDD enforcement
        tdd_enforcer = TDDGuardEnforcer(temp_project)
        
        # Create source file without tests (should trigger violation)
        src_file = Path("src/auth.py")
        with open(src_file, 'w') as f:
            f.write('''
def authenticate_user(username, password):
    # Authentication logic here
    return True
''')
        
        compliant, violations = tdd_enforcer.enforce_tdd_on_file_change(str(src_file), open(src_file).read())
        assert not compliant  # Should fail due to missing tests
        
        # Create corresponding test file
        test_file = Path("tests/test_auth.py")
        with open(test_file, 'w') as f:
            f.write('''
def test_authenticate_user():
    from src.auth import authenticate_user
    result = authenticate_user("test", "test")
    assert result is True
''')
        
        # Now TDD compliance should improve
        compliant, violations = tdd_enforcer.enforce_tdd_on_file_change(str(src_file), open(src_file).read())
        # May still have violations but should be less critical
        critical_violations = [v for v in violations if v.severity == "critical"]
        assert len(critical_violations) == 0
    
    def test_quality_gates_integration(self, temp_project):
        """Test quality gates integration"""
        # Create a Python file with quality issues
        src_file = Path("src/quality_test.py")
        src_file.parent.mkdir(exist_ok=True)
        
        poor_quality_code = '''
def poorly_written_function(x,y,z):
    if x==1:
        if y==2:
            if z==3:
                return "bad"
    else:
        return"worse"
'''
        
        with open(src_file, 'w') as f:
            f.write(poor_quality_code)
        
        # Test TDD enforcement
        enforcer = TDDGuardEnforcer(temp_project)
        violations = enforcer.validate_tdd_compliance(str(src_file), poor_quality_code)
        
        # Should detect multiple issues
        assert len(violations) > 0
        
        # Test issue creation integration
        issue_manager = SPARCGitIssueManager("quality-test")
        
        # Convert TDD violation to framework violation
        if violations:
            tdd_violation = violations[0]
            framework_violation = FrameworkViolation(
                violation_type="tdd_quality_violation",
                severity=tdd_violation.severity,
                phase="implementation",
                agent="tdd-guard",
                description=tdd_violation.description,
                file_path=tdd_violation.file_path,
                line_number=tdd_violation.line_number,
                resolution_steps=[tdd_violation.suggested_fix] if tdd_violation.suggested_fix else []
            )
            
            # Test issue body generation
            issue_body = issue_manager._generate_issue_body(framework_violation)
            assert tdd_violation.description in issue_body

def test_cli_interfaces():
    """Test CLI interfaces of all automation scripts"""
    scripts_dir = Path(__file__).parent.parent / "scripts"
    
    # Test each script's help/usage
    scripts = [
        "git-issue-automation.py",
        "tdd-guard-enforcer.py", 
        "sparc-workflow-enforcer.py",
        "framework-integration-hooks.py"
    ]
    
    for script in scripts:
        script_path = scripts_dir / script
        if script_path.exists():
            # Test that script can be executed
            result = subprocess.run([
                "python", str(script_path)
            ], capture_output=True, text=True)
            
            # Should show usage information (exit code 1 is expected for usage)
            assert result.returncode in [0, 1]
            assert "Usage:" in result.stdout or "usage:" in result.stdout.lower()

if __name__ == "__main__":
    # Run tests with pytest if available, otherwise run basic tests
    try:
        pytest.main([__file__, "-v"])
    except ImportError:
        print("⚠️  pytest not available, running basic tests...")
        
        # Create a temporary test instance
        test_instance = TestFrameworkIntegration()
        
        # Create temporary directory
        import tempfile
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            try:
                os.chdir(temp_dir)
                subprocess.run(["git", "init"], check=True, capture_output=True)
                subprocess.run(["git", "config", "user.email", "test@example.com"], check=True)
                subprocess.run(["git", "config", "user.name", "Test User"], check=True)
                
                print("✅ Running basic integration tests...")
                
                # Run basic tests
                test_instance.test_git_issue_automation(temp_dir)
                print("✅ Git issue automation test passed")
                
                test_instance.test_tdd_guard_enforcement(temp_dir)
                print("✅ TDD-Guard enforcement test passed")
                
                test_instance.test_workflow_enforcement(temp_dir)
                print("✅ Workflow enforcement test passed")
                
                print("✅ All basic integration tests passed!")
                
            finally:
                os.chdir(original_cwd)