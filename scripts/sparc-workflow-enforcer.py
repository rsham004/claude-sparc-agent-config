#!/usr/bin/env python3
"""
SPARC Workflow Enforcement System
Validates agent sequence compliance and document completeness
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import re

@dataclass
class AgentStatus:
    """Represents the status of a SPARC agent"""
    name: str
    phase: int
    completed: bool
    output_file: Optional[str] = None
    validation_score: float = 0.0
    completion_time: Optional[datetime] = None
    dependencies_met: bool = False

@dataclass
class WorkflowViolation:
    """Represents a SPARC workflow violation"""
    agent: str
    violation_type: str
    description: str
    severity: str
    blocking: bool = True
    resolution_steps: List[str] = None

class SPARCWorkflowEnforcer:
    """Enforces SPARC agent workflow sequence and validation"""
    
    def __init__(self, project_name: str = "", design_docs_path: str = "docs/design"):
        self.project_name = project_name
        self.design_docs_path = Path(design_docs_path) / project_name if project_name else Path(design_docs_path)
        
        # Define SPARC agent sequence with dependencies
        self.agent_sequence = [
            {
                "name": "product-manager",
                "phase": 1,
                "output_file": "product_requirements.md",
                "dependencies": [],
                "required_sections": [
                    "Elevator Pitch", "Who is this app for", "Functional Requirements",
                    "User Stories", "User Interface Overview", "Success Metrics",
                    "Constraints & Assumptions", "Roadmap Overview"
                ]
            },
            {
                "name": "solution-architect", 
                "phase": 2,
                "output_file": "architecture_guide.md",
                "dependencies": ["product-manager"],
                "required_sections": [
                    "Architecture Overview", "Technology Stack", "System Design",
                    "Security Considerations", "Performance Requirements", "Deployment Strategy"
                ]
            },
            {
                "name": "ux-designer",
                "phase": 3,
                "output_file": "ux_design.md",
                "dependencies": ["product-manager", "solution-architect"],
                "required_sections": [
                    "User Interface Design", "User Experience Flow", "Responsive Design",
                    "Accessibility", "Wireframes", "Component Specifications"
                ]
            },
            {
                "name": "visual-style-specialist",
                "phase": 4,
                "output_file": "visual_concepts.md",
                "dependencies": ["ux-designer"],
                "required_sections": [
                    "Visual Style Concepts", "Color Palettes", "Typography",
                    "Visual Elements", "Brand Guidelines", "Implementation Notes"
                ]
            },
            {
                "name": "data-architect",
                "phase": 5,
                "output_file": "database_design.md",
                "dependencies": ["solution-architect", "ux-designer"],
                "required_sections": [
                    "Database Schema", "Entity Relationships", "Data Models",
                    "Performance Considerations", "Migration Strategy", "Security"
                ]
            },
            {
                "name": "senior-api-developer",
                "phase": 6,
                "output_file": "api_specification.md",
                "dependencies": ["data-architect", "solution-architect"],
                "required_sections": [
                    "API Overview", "Endpoint Specifications", "Request/Response Models",
                    "Authentication", "Error Handling", "Rate Limiting"
                ]
            },
            {
                "name": "project-planner",
                "phase": 7,
                "output_file": "implementation_plan.md",
                "dependencies": ["senior-api-developer", "visual-style-specialist"],
                "required_sections": [
                    "Implementation Phases", "Task Breakdown", "Timeline",
                    "Resource Requirements", "Risk Assessment", "Success Criteria"
                ]
            },
            {
                "name": "senior-coder",
                "phase": 8,
                "output_file": "implementation_status.md",
                "dependencies": ["project-planner"],
                "required_sections": [
                    "Implementation Progress", "Code Quality Metrics", "TDD Compliance",
                    "Performance Metrics", "Security Validation", "Integration Status"
                ]
            },
            {
                "name": "tdd-guard-tester",
                "phase": 9,
                "output_file": "testing_report.md",
                "dependencies": ["senior-coder"],
                "required_sections": [
                    "Test Coverage Report", "Quality Assurance Results", "Performance Tests",
                    "Security Tests", "Integration Tests", "Deployment Validation"
                ]
            }
        ]
    
    def get_agent_status(self, agent_name: str) -> AgentStatus:
        """Get current status of a specific agent"""
        agent_config = next((a for a in self.agent_sequence if a["name"] == agent_name), None)
        if not agent_config:
            raise ValueError(f"Unknown agent: {agent_name}")
        
        output_path = self.design_docs_path / agent_config["output_file"]
        
        status = AgentStatus(
            name=agent_name,
            phase=agent_config["phase"],
            completed=output_path.exists(),
            output_file=str(output_path) if output_path.exists() else None
        )
        
        if status.completed:
            # Validate document completeness
            status.validation_score = self._validate_document_completeness(
                output_path, agent_config["required_sections"]
            )
            status.completion_time = datetime.fromtimestamp(output_path.stat().st_mtime)
        
        # Check dependencies
        status.dependencies_met = self._check_dependencies_met(agent_config["dependencies"])
        
        return status
    
    def _validate_document_completeness(self, file_path: Path, required_sections: List[str]) -> float:
        """Validate that document contains all required sections"""
        if not file_path.exists():
            return 0.0
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sections_found = 0
            for section in required_sections:
                # Look for section headers in various formats
                patterns = [
                    f"# {section}",
                    f"## {section}",
                    f"### {section}",
                    f"**{section}**",
                    f"{section}:",
                    section.lower().replace(" ", "")
                ]
                
                if any(pattern.lower() in content.lower() for pattern in patterns):
                    sections_found += 1
            
            return sections_found / len(required_sections)
        
        except Exception:
            return 0.0
    
    def _check_dependencies_met(self, dependencies: List[str]) -> bool:
        """Check if all dependency agents have completed"""
        for dep_agent in dependencies:
            dep_status = self.get_agent_status(dep_agent)
            if not dep_status.completed or dep_status.validation_score < 0.8:
                return False
        return True
    
    def validate_agent_execution_readiness(self, agent_name: str) -> Tuple[bool, List[WorkflowViolation]]:
        """Validate if agent can be executed based on workflow rules"""
        violations = []
        
        agent_config = next((a for a in self.agent_sequence if a["name"] == agent_name), None)
        if not agent_config:
            violations.append(WorkflowViolation(
                agent=agent_name,
                violation_type="unknown_agent",
                description=f"Agent '{agent_name}' is not part of SPARC workflow",
                severity="critical"
            ))
            return False, violations
        
        # Check dependencies
        for dep_agent in agent_config["dependencies"]:
            dep_status = self.get_agent_status(dep_agent)
            
            if not dep_status.completed:
                violations.append(WorkflowViolation(
                    agent=agent_name,
                    violation_type="missing_dependency",
                    description=f"Dependency '{dep_agent}' has not completed",
                    severity="critical",
                    resolution_steps=[f"Execute {dep_agent} agent first", "Ensure output document is generated"]
                ))
            
            elif dep_status.validation_score < 0.8:
                violations.append(WorkflowViolation(
                    agent=agent_name,
                    violation_type="incomplete_dependency",
                    description=f"Dependency '{dep_agent}' document is incomplete ({dep_status.validation_score:.1%})",
                    severity="high",
                    resolution_steps=[f"Complete all required sections in {dep_status.output_file}"]
                ))
        
        # Check for technology lock compliance (if applicable)
        if agent_name in ["data-architect", "senior-api-developer", "senior-coder"]:
            tech_lock_violations = self._check_technology_lock_compliance()
            violations.extend(tech_lock_violations)
        
        # Determine if execution can proceed
        blocking_violations = [v for v in violations if v.blocking and v.severity in ["critical", "high"]]
        
        return len(blocking_violations) == 0, violations
    
    def _check_technology_lock_compliance(self) -> List[WorkflowViolation]:
        """Check technology lock file compliance"""
        violations = []
        
        tech_lock_path = self.design_docs_path / "technology-lock.json"
        if not tech_lock_path.exists():
            violations.append(WorkflowViolation(
                agent="solution-architect",
                violation_type="missing_technology_lock",
                description="technology-lock.json file not found",
                severity="critical",
                resolution_steps=["Solution Architect must create technology-lock.json"]
            ))
        else:
            try:
                with open(tech_lock_path) as f:
                    tech_lock = json.load(f)
                
                required_fields = ["frontend", "backend", "database", "deployment"]
                for field in required_fields:
                    if field not in tech_lock:
                        violations.append(WorkflowViolation(
                            agent="solution-architect",
                            violation_type="incomplete_technology_lock",
                            description=f"Missing '{field}' specification in technology-lock.json",
                            severity="medium",
                            blocking=False
                        ))
            except json.JSONDecodeError:
                violations.append(WorkflowViolation(
                    agent="solution-architect",
                    violation_type="invalid_technology_lock",
                    description="technology-lock.json is not valid JSON",
                    severity="high"
                ))
        
        return violations
    
    def get_workflow_status(self) -> Dict:
        """Get complete workflow status"""
        status = {
            "project_name": self.project_name,
            "current_phase": 0,
            "completion_percentage": 0,
            "agents": {},
            "next_action": None,
            "blocking_issues": [],
            "ready_for_implementation": False
        }
        
        completed_phases = 0
        total_phases = len(self.agent_sequence)
        
        for agent_config in self.agent_sequence:
            agent_status = self.get_agent_status(agent_config["name"])
            status["agents"][agent_config["name"]] = {
                "phase": agent_status.phase,
                "completed": agent_status.completed,
                "validation_score": agent_status.validation_score,
                "dependencies_met": agent_status.dependencies_met,
                "output_file": agent_status.output_file
            }
            
            if agent_status.completed and agent_status.validation_score >= 0.8:
                completed_phases += 1
                status["current_phase"] = max(status["current_phase"], agent_status.phase)
        
        status["completion_percentage"] = (completed_phases / total_phases) * 100
        
        # Determine next action
        for agent_config in self.agent_sequence:
            agent_status = self.get_agent_status(agent_config["name"])
            if not agent_status.completed:
                ready, violations = self.validate_agent_execution_readiness(agent_config["name"])
                if ready:
                    status["next_action"] = f"Execute {agent_config['name']} agent"
                    break
                else:
                    status["blocking_issues"].extend([
                        f"{v.agent}: {v.description}" for v in violations if v.blocking
                    ])
                    if not status["next_action"]:
                        status["next_action"] = f"Resolve blocking issues for {agent_config['name']}"
                    break
        
        # Check if ready for implementation
        design_agents = [a for a in self.agent_sequence if a["phase"] <= 7]
        design_complete = all(
            self.get_agent_status(a["name"]).completed and 
            self.get_agent_status(a["name"]).validation_score >= 0.8
            for a in design_agents
        )
        status["ready_for_implementation"] = design_complete
        
        return status
    
    def validate_phase_completion(self, phase: int) -> Tuple[bool, List[WorkflowViolation]]:
        """Validate that a specific phase is complete"""
        violations = []
        
        phase_agents = [a for a in self.agent_sequence if a["phase"] == phase]
        if not phase_agents:
            violations.append(WorkflowViolation(
                agent="workflow",
                violation_type="invalid_phase",
                description=f"Phase {phase} does not exist",
                severity="critical"
            ))
            return False, violations
        
        for agent_config in phase_agents:
            agent_status = self.get_agent_status(agent_config["name"])
            
            if not agent_status.completed:
                violations.append(WorkflowViolation(
                    agent=agent_config["name"],
                    violation_type="incomplete_agent",
                    description=f"Agent has not generated output document",
                    severity="critical"
                ))
            
            elif agent_status.validation_score < 0.8:
                violations.append(WorkflowViolation(
                    agent=agent_config["name"],
                    violation_type="incomplete_document",
                    description=f"Document only {agent_status.validation_score:.1%} complete",
                    severity="high"
                ))
        
        return len(violations) == 0, violations
    
    def generate_compliance_report(self) -> str:
        """Generate comprehensive compliance report"""
        status = self.get_workflow_status()
        
        report = [
            "# SPARC Framework Compliance Report",
            f"**Project:** {self.project_name or 'Unknown'}",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Overall Progress:** {status['completion_percentage']:.1f}%",
            "",
            "## Agent Status Overview",
            ""
        ]
        
        for agent_name, agent_info in status["agents"].items():
            emoji = "✅" if agent_info["completed"] else "❌"
            score = f"{agent_info['validation_score']:.1%}" if agent_info["completed"] else "N/A"
            
            report.append(f"{emoji} **{agent_name.replace('-', ' ').title()}** (Phase {agent_info['phase']})")
            report.append(f"   - Completed: {agent_info['completed']}")
            report.append(f"   - Validation Score: {score}")
            report.append(f"   - Dependencies Met: {agent_info['dependencies_met']}")
            if agent_info["output_file"]:
                report.append(f"   - Output: {agent_info['output_file']}")
            report.append("")
        
        if status["blocking_issues"]:
            report.extend([
                "## Blocking Issues",
                ""
            ])
            for issue in status["blocking_issues"]:
                report.append(f"❌ {issue}")
            report.append("")
        
        if status["next_action"]:
            report.extend([
                "## Next Action Required",
                f"🎯 {status['next_action']}",
                ""
            ])
        
        report.extend([
            "## Implementation Readiness",
            f"{'✅ Ready for Implementation' if status['ready_for_implementation'] else '❌ Design Phase Incomplete'}",
            ""
        ])
        
        return "\n".join(report)
    
    def create_workflow_issue_if_needed(self) -> Optional[str]:
        """Create Git issue if workflow violations exist"""
        # Check for critical violations
        violations = []
        
        for agent_config in self.agent_sequence:
            ready, agent_violations = self.validate_agent_execution_readiness(agent_config["name"])
            violations.extend([v for v in agent_violations if v.severity in ["critical", "high"]])
        
        if not violations:
            return None
        
        # Create issue using git-issue-automation.py
        try:
            from pathlib import Path
            import sys
            
            # Add scripts directory to path
            scripts_dir = Path(__file__).parent
            sys.path.insert(0, str(scripts_dir))
            
            from git_issue_automation import SPARCGitIssueManager, FrameworkViolation
            
            issue_manager = SPARCGitIssueManager(self.project_name)
            
            # Create consolidated issue for workflow violations
            violation_descriptions = [f"- {v.description}" for v in violations]
            
            framework_violation = FrameworkViolation(
                violation_type="workflow_compliance",
                severity="critical",
                phase="design",
                agent="workflow-enforcer",
                description=f"SPARC workflow violations detected:\n" + "\n".join(violation_descriptions),
                resolution_steps=[v.resolution_steps[0] if v.resolution_steps else "Resolve violation" for v in violations]
            )
            
            return issue_manager.create_violation_issue(framework_violation)
        
        except Exception as e:
            print(f"Warning: Could not create workflow issue: {e}")
            return None

def main():
    """CLI interface for workflow enforcement"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python sparc-workflow-enforcer.py <command> [args...]")
        print("Commands:")
        print("  status [project_name]")
        print("  validate-agent <agent_name> [project_name]") 
        print("  validate-phase <phase_number> [project_name]")
        print("  compliance-report [project_name]")
        print("  check-readiness <agent_name> [project_name]")
        sys.exit(1)
    
    command = sys.argv[1]
    project_name = sys.argv[2] if len(sys.argv) > 2 and not command.startswith("validate-") else ""
    
    enforcer = SPARCWorkflowEnforcer(project_name)
    
    if command == "status":
        status = enforcer.get_workflow_status()
        print(f"Project: {status['project_name'] or 'Default'}")
        print(f"Progress: {status['completion_percentage']:.1f}%")
        print(f"Current Phase: {status['current_phase']}")
        print(f"Next Action: {status['next_action'] or 'All phases complete'}")
        
        if status["blocking_issues"]:
            print("\nBlocking Issues:")
            for issue in status["blocking_issues"]:
                print(f"  ❌ {issue}")
    
    elif command == "validate-agent":
        if len(sys.argv) < 3:
            print("Usage: validate-agent <agent_name> [project_name]")
            sys.exit(1)
        
        agent_name = sys.argv[2]
        project_name = sys.argv[3] if len(sys.argv) > 3 else ""
        enforcer = SPARCWorkflowEnforcer(project_name)
        
        ready, violations = enforcer.validate_agent_execution_readiness(agent_name)
        
        if ready:
            print(f"✅ {agent_name} ready for execution")
        else:
            print(f"❌ {agent_name} blocked by violations:")
            for violation in violations:
                print(f"  • {violation.description}")
                if violation.resolution_steps:
                    for step in violation.resolution_steps:
                        print(f"    → {step}")
    
    elif command == "validate-phase":
        if len(sys.argv) < 3:
            print("Usage: validate-phase <phase_number> [project_name]")
            sys.exit(1)
        
        phase = int(sys.argv[2])
        project_name = sys.argv[3] if len(sys.argv) > 3 else ""
        enforcer = SPARCWorkflowEnforcer(project_name)
        
        complete, violations = enforcer.validate_phase_completion(phase)
        
        if complete:
            print(f"✅ Phase {phase} complete")
        else:
            print(f"❌ Phase {phase} incomplete:")
            for violation in violations:
                print(f"  • {violation.agent}: {violation.description}")
    
    elif command == "compliance-report":
        report = enforcer.generate_compliance_report()
        print(report)
    
    elif command == "check-readiness":
        if len(sys.argv) < 3:
            print("Usage: check-readiness <agent_name> [project_name]")
            sys.exit(1)
        
        agent_name = sys.argv[2]
        project_name = sys.argv[3] if len(sys.argv) > 3 else ""
        enforcer = SPARCWorkflowEnforcer(project_name)
        
        ready, violations = enforcer.validate_agent_execution_readiness(agent_name)
        
        if ready:
            print("✅ READY")
        else:
            print("❌ BLOCKED")
            sys.exit(1)
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()