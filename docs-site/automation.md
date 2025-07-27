---
layout: default
title: "Automation Features - SPARC Framework"
description: "Complete automation backbone with Git issue tracking, TDD-Guard enforcement, workflow validation, and quality gates that actually work."
keywords: "SPARC automation, Git issues, TDD-Guard, workflow enforcement, quality gates, Claude Code automation"
permalink: /automation/
---

# 🤖 Complete Automation Backbone

SPARC Framework features a comprehensive automation system that transforms development from manual processes into enforced, quality-guaranteed workflows.

## 🚀 What's Automated

### ✅ **Git Issue Management**
- **Automatic creation** for all framework violations
- **Progress tracking** with real-time updates
- **Issue closure validation** ensuring actual resolution
- **Dependency mapping** showing blocked agents and phases

### ✅ **TDD-Guard Enforcement**
- **File operation interception** analyzing all code changes
- **Real-time violation blocking** preventing non-compliant commits
- **Test coverage validation** with 90% minimum threshold
- **Complexity analysis** preventing over-implementation

### ✅ **Workflow Validation**
- **Agent dependency checking** ensuring proper sequence
- **Document completeness scoring** validating all required sections
- **Phase transition gates** blocking progression with incomplete work
- **Technology lock compliance** enforcing approved stacks

### ✅ **Quality Gates**
- **Pre-commit validation** blocking until all standards met
- **CI/CD integration** with GitHub Actions
- **Automated testing** ensuring all automation works
- **Performance monitoring** tracking framework effectiveness

## 🛠️ Automation Scripts

### Git Issue Automation (`scripts/git-issue-automation.py`)

Handles all framework violation tracking:

```bash
# Check for blocking issues
python scripts/git-issue-automation.py check-blockers

# Create violation issue
python scripts/git-issue-automation.py create-violation \
  "missing_tests" "critical" "implementation" "tdd-guard" \
  "Source file lacks corresponding test coverage"

# Validate phase completion
python scripts/git-issue-automation.py validate-phase design

# Update issue progress
python scripts/git-issue-automation.py update-issue 123 \
  "🔄 Working on resolution - 50% complete"

# Close resolved issue
python scripts/git-issue-automation.py close-issue 123 \
  "All tests implemented and passing"
```

### TDD-Guard Enforcer (`scripts/tdd-guard-enforcer.py`)

Enforces test-driven development:

```bash
# Validate individual file
python scripts/tdd-guard-enforcer.py validate-file src/auth.py

# Check commit readiness
python scripts/tdd-guard-enforcer.py validate-commit

# Run tests with coverage
python scripts/tdd-guard-enforcer.py check-coverage

# Run full test suite
python scripts/tdd-guard-enforcer.py run-tests
```

### Workflow Enforcer (`scripts/sparc-workflow-enforcer.py`)

Validates SPARC agent sequence:

```bash
# Check overall status
python scripts/sparc-workflow-enforcer.py status my-project

# Validate agent readiness
python scripts/sparc-workflow-enforcer.py check-readiness product-manager

# Validate phase completion
python scripts/sparc-workflow-enforcer.py validate-phase 1

# Generate compliance report
python scripts/sparc-workflow-enforcer.py compliance-report
```

### Framework Integration Hooks (`scripts/framework-integration-hooks.py`)

Claude Code integration points:

```bash
# Install hooks for Claude Code
python scripts/framework-integration-hooks.py install-hooks

# Manual hook testing
python scripts/framework-integration-hooks.py pre-commit
python scripts/framework-integration-hooks.py agent-execution product-manager design
```

## 🔄 Automated Workflows

### Pre-File Edit Validation

Every file modification is checked for:
- TDD compliance (tests exist before implementation)
- Workflow readiness (agent dependencies met)
- Technology lock compliance (only approved tools)

### Post-File Edit Enforcement

After file changes:
- TDD violations automatically create Git issues
- Workflow violations block agent progression
- Quality scores updated in real-time

### Pre-Commit Quality Gates

Before any commit:
1. **Test Suite Execution** - All tests must pass
2. **Coverage Validation** - Minimum 90% coverage required
3. **TDD Compliance** - No implementations without tests
4. **Workflow Validation** - All agent dependencies satisfied
5. **Technology Compliance** - Only approved stack components

### CI/CD Pipeline Automation

GitHub Actions automatically:
- Validates framework structure
- Tests all automation scripts
- Checks documentation quality
- Verifies agent file consistency
- Creates issues for failures

## 📊 Real-Time Monitoring

### Framework Status Dashboard

```bash
# Complete status overview
python scripts/sparc-workflow-enforcer.py status

# Output example:
# Project: my-awesome-app
# Progress: 67.5%
# Current Phase: 6
# Next Action: Execute Senior API Developer agent
# Blocking Issues: 0
```

### Quality Metrics Tracking

```bash
# TDD compliance check
python scripts/tdd-guard-enforcer.py validate-commit

# Output example:
# ✅ Tests Passed: True
# ✅ Coverage: 94.2%
# ✅ TDD Violations: 0
# ✅ Repository ready for commit
```

### Issue Management

```bash
# Check all blocking issues
python scripts/git-issue-automation.py check-blockers

# Output example:
# ❌ 2 blocking issues found:
#   • Issue #45: PRD Incomplete - Blocking UX Phase
#   • Issue #46: Missing Tests - Blocking Commit
```

## 🛡️ Enforcement Levels

### **CRITICAL** - Blocks All Operations
- Missing tests for source code
- Agent execution without dependencies
- Commits with failing tests
- Technology violations

### **HIGH** - Creates Issues, May Block
- Incomplete design documents
- Low test coverage (< 90%)
- Complex functions (> 20 lines)
- Missing required sections

### **MEDIUM** - Tracked, Guidance Provided
- Code style violations
- Documentation inconsistencies
- Performance concerns
- Best practice suggestions

### **LOW** - Informational Only
- Optimization opportunities
- Enhancement suggestions
- Community recommendations

## 🔧 Configuration

### Automation Settings

Create `.claude/hooks/config.json`:

```json
{
  "tdd_guard_enabled": true,
  "workflow_enforcement": true,
  "auto_issue_creation": true,
  "quality_gates": true,
  "technology_lock_enforcement": true,
  "coverage_threshold": 90,
  "max_function_length": 20,
  "max_complexity": 5
}
```

### Technology Lock Example

`docs/design/PROJECT/technology-lock.json`:

```json
{
  "frontend": {
    "framework": "React",
    "version": "18.2.0",
    "ui_library": "Material-UI"
  },
  "backend": {
    "framework": "FastAPI",
    "version": "0.104.1",
    "orm": "SQLModel"
  },
  "database": {
    "type": "PostgreSQL",
    "version": "15.0"
  },
  "deployment": {
    "platform": "AWS",
    "container": "Docker",
    "orchestration": "ECS"
  }
}
```

## 🎯 Getting Started with Automation

### 1. Enable Full Automation

```bash
# After project setup
python scripts/framework-integration-hooks.py install-hooks
```

### 2. Validate Current Status

```bash
# Check what needs attention
python scripts/sparc-workflow-enforcer.py status
python scripts/git-issue-automation.py check-blockers
```

### 3. Start Workflow with Enforcement

```bash
# Begin with automatic validation
claude "Execute Product Manager agent with full automation enabled"
```

### 4. Monitor Progress

Use the automation scripts to track progress and resolve violations as they're automatically detected.

## 📈 Benefits of Full Automation

### **Zero Manual Tracking**
- All violations automatically become Git issues
- Progress tracked in real-time
- No forgotten quality checks

### **Enforced Standards**
- Cannot proceed without meeting requirements
- Quality gates prevent technical debt
- Consistent code quality across team

### **Complete Audit Trail**
- Every decision documented
- Full history of violations and resolutions
- Compliance reporting for stakeholders

### **Faster Development**
- Issues caught immediately
- Clear guidance for resolution
- Automated testing and validation

## 🚨 Troubleshooting Automation

### Common Issues

**Automation script not found:**
```bash
chmod +x scripts/*.py
python -m pip install --upgrade pip
```

**Git CLI not configured:**
```bash
gh auth login
git config user.name "Your Name"
git config user.email "you@example.com"
```

**Hooks not working:**
```bash
python scripts/framework-integration-hooks.py install-hooks
```

**Tests failing:**
```bash
python scripts/tdd-guard-enforcer.py run-tests
# Fix issues shown in output
```

---

## 🎉 Ready for Full Automation?

Enable complete automation in your SPARC project:

```bash
# Install all automation hooks
python scripts/framework-integration-hooks.py install-hooks

# Verify automation status
python scripts/sparc-workflow-enforcer.py status

# Begin automated development
claude "Start SPARC workflow with full automation enforcement"
```

The automation backbone ensures every aspect of your development follows SPARC methodology with zero compromise on quality.

**[← Back to Quick Start]({{ '/quick-start/' | relative_url }})** | **[View Documentation]({{ '/documentation/' | relative_url }})**