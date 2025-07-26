# SPARC Agent Framework with TDD-Guard Enforcement

## Framework Overview

This CLAUDE.md file enforces a comprehensive development framework that combines the SPARC (Structured Product Architecture Requirement Creation) agent methodology with TDD-Guard enforcement for high-quality, test-driven development.

## Core Principles

### 1. **Mandatory Agent Workflow**
All development projects MUST follow the SPARC agent sequence:
1. **Product Manager** → Generate PRD
2. **UX Designer** → Create UI Design Document  
3. **Visual Style Specialist** → Generate visual concepts
4. **Solution Architect** → Design technical architecture
5. **Data Architect** → Create database schema
6. **Senior API Developer** → Design API specifications
7. **Project Planner** → Generate implementation plan
8. **TDD-Guard Enforcement** → Validate all code changes

### 2. **TDD-Guard Integration**
All file operations are subject to TDD-Guard validation:
- **Edit/MultiEdit/Write operations** are intercepted and analyzed
- **Test-first development** is strictly enforced
- **Over-implementation** is blocked
- **Code quality** is maintained through automated linting

### 3. **Technology Lock Enforcement**
- Only approved technologies from `technology-lock.json` may be used
- Version compliance is strictly enforced
- Documentation must come from approved sources only

### 4. **Mandatory Git Issue Management**
All problems, violations, and blockers MUST be tracked via Git issues:
- **Auto-created issues** for all framework violations
- **Continuous updates** on issue status and resolution
- **Linked issues** across related problems
- **Automated labeling** for categorization and prioritization
- **Required issue closure** before proceeding to next phase

## Agent Execution Rules

### Phase 1: Requirements & Design (MANDATORY)

#### 1.1 Product Requirements Document (PRD)
**Agent:** `01-product-manager.md`
- **TRIGGER:** User provides initial project idea
- **INPUT:** User description of project concept
- **OUTPUT:** `product_requirements.md`
- **VALIDATION:** Must include all required PRD sections before proceeding
- **GIT ISSUE:** Auto-create `design/prd-validation` issue tracking completion status

#### 1.2 User Experience Design
**Agent:** `06a-ux-designer-collaborative.md`
- **TRIGGER:** PRD completion
- **INPUT:** `product_requirements.md`
- **OUTPUT:** `ux_design.md`
- **VALIDATION:** Must include UI/UX specifications for all user stories
- **GIT ISSUE:** Auto-create `design/ux-validation` issue tracking UI/UX completeness

#### 1.3 Visual Style Generation
**Agent:** `11-visual-style-specialist.md`
- **TRIGGER:** UX Design completion
- **INPUT:** `ux_design.md`, `product_requirements.md`
- **OUTPUT:** Visual style concepts (9 distinct styles)
- **VALIDATION:** All 9 styles must be clearly differentiated
- **GIT ISSUE:** Auto-create `design/visual-styles` issue tracking 9-style generation and validation

#### 1.4 Solution Architecture
**Agent:** `02-solution-architect.md`
- **TRIGGER:** UX/Visual Design completion
- **INPUT:** PRD, UX Design, Visual Concepts
- **OUTPUT:** `architecture_guide.md`, `technology-lock.json`
- **VALIDATION:** Must specify complete technical stack with exact versions
- **GIT ISSUE:** Auto-create `design/architecture-validation` issue tracking tech stack approval and version lock

#### 1.5 Database Design
**Agent:** `04a-data-architect-sqlmodel.md`
- **TRIGGER:** Architecture Guide completion
- **INPUT:** `architecture_guide.md`, `product_requirements.md`
- **OUTPUT:** `database_design.md`
- **VALIDATION:** Must include SQLModel schemas and relationship definitions
- **GIT ISSUE:** Auto-create `design/database-schema` issue tracking schema validation and relationship integrity

#### 1.6 API Specification
**Agent:** `05a-senior-api-developer-fastapi.md`
- **TRIGGER:** Database Design completion
- **INPUT:** All previous documents
- **OUTPUT:** `api_specification.md`
- **VALIDATION:** Must define all endpoints with request/response models
- **GIT ISSUE:** Auto-create `design/api-specification` issue tracking endpoint completeness and model validation

#### 1.7 Implementation Planning
**Agent:** `07a-project-implementation-planner.md`
- **TRIGGER:** API Specification completion
- **INPUT:** All design documents
- **OUTPUT:** `implementation_plan.md`
- **VALIDATION:** Must break down into phases with difficulty ratings
- **GIT ISSUE:** Auto-create `design/implementation-plan` issue tracking phase breakdown and task validation

### Phase 2: TDD-Guard Enforcement (CONTINUOUS)

#### 2.1 Test-Driven Development Rules
**ALL CODE CHANGES MUST:**
- Write failing tests FIRST
- Implement minimal code to pass tests
- Refactor only with passing tests
- Never skip or bypass test requirements

#### 2.2 Automated Validation
**TDD-Guard automatically:**
- Intercepts Edit, MultiEdit, and Write operations
- Analyzes code changes for TDD compliance
- Blocks non-compliant operations
- Provides corrective guidance

#### 2.3 Quality Gates
**Before ANY commit:**
- All tests must pass
- Code must pass linting (ESLint)
- No TDD violations detected
- Type checking must succeed

## Enforcement Mechanisms

### Technology Compliance
```bash
# Technology usage validation
- Check imports against technology-lock.json
- Verify version compatibility
- Block unauthorized dependencies
- Redirect to approved documentation only
```

### TDD Compliance
```bash
# Test-driven development validation
- Require tests before implementation
- Block over-implementation
- Enforce red-green-refactor cycle
- Validate test coverage
```

### Agent Workflow Compliance
```bash
# SPARC sequence enforcement
- Block implementation without complete design phase
- Require all design documents before coding
- Validate agent output completeness
- Enforce proper documentation handoffs
```

## Git Issue Management System (MANDATORY)

### Automated Issue Creation
**ALL violations, blockers, and validation failures MUST trigger automatic Git issue creation:**

#### Design Phase Issues
```bash
# Issue Labels: design, validation, blocker
gh issue create --title "PRD Validation Failed" --label "design,validation,blocker" \
  --body "Missing required PRD sections: [list]. Cannot proceed to UX phase."

gh issue create --title "Architecture Tech Stack Incomplete" --label "design,architecture,blocker" \
  --body "technology-lock.json missing exact versions for: [technologies]"

gh issue create --title "Database Schema Validation Failed" --label "design,database,blocker" \
  --body "SQLModel relationships undefined: [missing relationships]"
```

#### Implementation Phase Issues
```bash
# Issue Labels: tdd, quality, blocker, implementation
gh issue create --title "TDD Violation: Missing Tests" --label "tdd,blocker,implementation" \
  --body "File: [filename] | Line: [line] | Missing test coverage before implementation"

gh issue create --title "Technology Compliance Violation" --label "compliance,blocker,technology" \
  --body "Unauthorized import: [import] | File: [filename] | Approved alternative: [suggestion]"

gh issue create --title "Quality Gate Failure" --label "quality,blocker,implementation" \
  --body "Failed checks: [lint|test|typecheck] | Cannot proceed with commit"
```

### Issue Lifecycle Management

#### 1. **Creation Triggers**
- Agent validation failures
- TDD-Guard violations
- Technology compliance breaches
- Quality gate failures
- Missing dependencies between phases

#### 2. **Issue Templates**
```markdown
# SPARC Framework Violation Template
**Phase:** [Design|Implementation]
**Agent:** [agent-name]
**Severity:** [Critical|High|Medium|Low]
**Blocker:** [Yes|No]

## Problem Description
[Detailed description of the violation]

## Current State
- [ ] Problem identified
- [ ] Investigation started
- [ ] Solution proposed
- [ ] Fix implemented
- [ ] Validation passed

## Resolution Requirements
[Specific steps needed to resolve]

## Dependencies
- Blocked by: [related issues]
- Blocks: [dependent issues]

## Framework Impact
- [ ] Affects subsequent agents
- [ ] Breaks TDD compliance
- [ ] Violates technology lock
- [ ] Impacts quality gates
```

#### 3. **Automated Updates**
```bash
# Progress tracking with automatic comments
gh issue comment [issue-number] --body "🔄 Validation re-run: [status]"
gh issue comment [issue-number] --body "✅ TDD compliance restored"
gh issue comment [issue-number] --body "❌ Additional violations found: [details]"

# Automatic labeling based on status
gh issue edit [issue-number] --add-label "in-progress"
gh issue edit [issue-number] --add-label "resolved" --remove-label "blocker"
```

#### 4. **Issue Relationships**
```bash
# Link related issues
gh issue comment [issue-number] --body "Related to #[other-issue]"
gh issue comment [issue-number] --body "Blocks #[dependent-issue]"
gh issue comment [issue-number] --body "Resolves #[parent-issue]"
```

### Issue Categories and Labels

#### Core Labels (REQUIRED)
- **Phase:** `design`, `implementation`, `validation`
- **Severity:** `critical`, `high`, `medium`, `low`
- **Type:** `blocker`, `violation`, `compliance`, `quality`
- **Component:** `tdd`, `architecture`, `database`, `api`, `ux`, `visual`

#### Status Labels (AUTO-MANAGED)
- **Lifecycle:** `new`, `in-progress`, `resolved`, `verified`
- **Agent:** `product-manager`, `ux-designer`, `solution-architect`, `data-architect`, `api-developer`, `planner`

#### Custom Labels (CONTEXT-SPECIFIC)
- **Technology:** `technology-lock`, `dependency`, `version-mismatch`
- **Testing:** `missing-tests`, `test-failure`, `coverage-low`
- **Documentation:** `missing-docs`, `incomplete-spec`, `outdated`

### Continuous Issue Monitoring

#### Real-time Validation Hooks
```bash
# Pre-agent execution
function validate_prerequisites() {
  open_blockers=$(gh issue list --label "blocker" --state open --json number | jq length)
  if [ $open_blockers -gt 0 ]; then
    echo "❌ Cannot proceed: $open_blockers blocking issues open"
    gh issue list --label "blocker" --state open
    exit 1
  fi
}

# Post-agent execution
function validate_outputs() {
  if [ validation_failed ]; then
    gh issue create --title "Agent Output Validation Failed: [agent-name]" \
      --label "design,validation,blocker" \
      --body "Output: [filename] | Missing: [requirements]"
  fi
}
```

#### Daily Issue Reports
```bash
# Generate daily framework compliance report
gh issue list --label "blocker" --state open > daily_blockers.md
gh issue list --label "tdd" --state open > tdd_violations.md
gh issue list --label "compliance" --state open > compliance_issues.md
```

### Issue Resolution Requirements

#### Phase 1 (Design) - No Open Blockers
- **PRD Issues:** All sections complete and validated
- **UX Issues:** All user stories have UI specifications
- **Architecture Issues:** Complete tech stack with versions
- **Database Issues:** All relationships and schemas defined
- **API Issues:** All endpoints with request/response models

#### Phase 2 (Implementation) - Continuous Resolution
- **TDD Issues:** Tests written before any implementation
- **Quality Issues:** All lint/type/test checks passing
- **Technology Issues:** Only approved stack components used
- **Coverage Issues:** Minimum test coverage maintained

### Enforcement Commands

#### Issue Validation
```bash
# Check blocking issues before proceeding
claude --check-blockers

# Validate issue status for phase transition
claude --validate-phase-completion --phase=[design|implementation]

# Generate compliance report
claude --issue-compliance-report

# Force issue creation for current violations
claude --create-violation-issues
```

#### Issue Resolution Tracking
```bash
# Mark issue as resolved and validate
gh issue close [issue-number] --comment "✅ Resolved: [description]"

# Verify no new issues introduced
claude --post-resolution-validation --issue=[issue-number]

# Update dependent issues
claude --update-dependent-issues --resolved=[issue-number]
```

## File Structure Requirements

### Design Documents (Phase 1 Outputs)
```
design_docs/
├── product_requirements.md      # From Product Manager
├── ux_design.md                # From UX Designer  
├── visual_concepts/             # From Visual Style Specialist
├── architecture_guide.md       # From Solution Architect
├── technology-lock.json         # From Solution Architect
├── database_design.md          # From Data Architect
├── api_specification.md        # From Senior API Developer
└── implementation_plan.md      # From Project Planner
```

### Implementation Structure (Phase 2)
```
src/
├── tests/                      # Tests MUST exist before implementation
├── models/                     # SQLModel definitions from database design
├── api/                        # FastAPI routers from API specification
├── services/                   # Business logic following architecture
└── core/                       # Configuration and utilities
```

## Agent Communication Protocol

### 1. Sequential Dependency
- Each agent MUST receive output from previous agent
- No agent may proceed without required inputs
- Missing documents trigger automatic requests

### 2. Document Validation
- All outputs validated against specified formats
- Incomplete documents block workflow progression
- Quality gates enforced at each transition

### 3. Technology Enforcement
- Context7 Enforcer monitors all technology usage
- Only approved technologies permitted
- Documentation limited to approved sources

## Development Commands

### Framework Initialization
```bash
# Initialize SPARC workflow
claude --agent="01-product-manager" --input="project_idea.txt"

# Validate design phase completion
claude --validate-design-docs

# Enable TDD-Guard for implementation
claude --enable-tdd-guard

# Check framework compliance
claude --check-compliance
```

### TDD-Guard Operations
```bash
# Run all quality checks
npm run checks                  # typecheck + lint + format + test

# TDD validation only
npm run test:tdd               # TDD compliance validation

# Quality gate validation
npm run validate:commit        # Pre-commit validation
```

## Violation Handling with Git Issue Integration

### Design Phase Violations (AUTO-ISSUE CREATION)

#### Missing PRD
- **ACTION:** Block all subsequent agents until PRD complete
- **GIT ISSUE:** `gh issue create --title "PRD Incomplete - Blocking UX Phase" --label "design,prd,blocker"`
- **RESOLUTION:** Complete all required PRD sections, update issue with checklist progress
- **VALIDATION:** Automatic issue closure when PRD validation passes

#### Incomplete Architecture
- **ACTION:** Prevent database/API design phases
- **GIT ISSUE:** `gh issue create --title "Architecture Incomplete - Missing Tech Stack" --label "design,architecture,blocker"`
- **RESOLUTION:** Complete technology-lock.json with exact versions
- **VALIDATION:** Context7 enforcer validates tech stack before issue closure

#### Technology Deviation
- **ACTION:** Block and require Solution Architect review
- **GIT ISSUE:** `gh issue create --title "Technology Compliance Violation" --label "compliance,technology,blocker"`
- **RESOLUTION:** Solution Architect approval or technology-lock.json update
- **VALIDATION:** Approved technology list updated before proceeding

### Implementation Phase Violations (AUTO-ISSUE TRACKING)

#### Missing Tests
- **ACTION:** Block all Edit/Write operations
- **GIT ISSUE:** `gh issue create --title "TDD Violation: Missing Tests for [file]" --label "tdd,blocker,missing-tests"`
- **RESOLUTION:** Write failing tests first, then minimal implementation
- **VALIDATION:** TDD-Guard confirms test-first compliance before issue closure

#### TDD Violations
- **ACTION:** Provide specific guidance and block operation
- **GIT ISSUE:** `gh issue create --title "TDD Cycle Violation: [violation-type]" --label "tdd,violation,implementation"`
- **RESOLUTION:** Follow red-green-refactor cycle correctly
- **VALIDATION:** TDD-Guard validates cycle compliance

#### Quality Failures
- **ACTION:** Prevent commits until resolved
- **GIT ISSUE:** `gh issue create --title "Quality Gate Failure: [lint|test|type]" --label "quality,blocker,implementation"`
- **RESOLUTION:** Fix all lint errors, ensure tests pass, resolve type issues
- **VALIDATION:** All quality checks must pass before issue closure

### Recovery Procedures with Issue Tracking

#### Design Issues Recovery
1. **Identify Problem:** Automatic issue creation with specific missing requirements
2. **Return to Agent:** Re-run appropriate agent with issue context
3. **Track Progress:** Update issue with completion checklist
4. **Validate Resolution:** Automatic validation triggers issue closure
5. **Unblock Workflow:** Subsequent agents can proceed once issues resolved

#### Test Issues Recovery
1. **Generate Failing Tests:** TDD-Guard guides test creation
2. **Track Implementation:** Issue updated with test/implementation progress
3. **Validate TDD Compliance:** Red-green-refactor cycle verified
4. **Close Issue:** Automatic closure when TDD compliance restored

#### Technology Issues Recovery
1. **Review Violation:** Issue details unauthorized technology usage
2. **Solution Architect Review:** SA approves alternative or updates lock file
3. **Update Documentation:** Technology-lock.json updated with approved changes
4. **Validate Compliance:** Context7 enforcer confirms compliance
5. **Resume Development:** Issue closed, development can continue

### Issue-Driven Development Workflow

#### Pre-Phase Validation
```bash
# Check for blocking issues before starting any agent
function check_phase_blockers() {
  blockers=$(gh issue list --label "blocker" --state open --json number,title)
  if [[ $(echo $blockers | jq length) -gt 0 ]]; then
    echo "❌ BLOCKED: Cannot proceed to next phase"
    echo $blockers | jq -r '.[] | "Issue #\(.number): \(.title)"'
    exit 1
  fi
}
```

#### Post-Validation Issue Updates
```bash
# Update issues after agent completion
function update_agent_issues() {
  agent_name=$1
  if [[ $validation_passed == true ]]; then
    gh issue comment --body "✅ Agent $agent_name completed successfully"
    gh issue close --comment "All requirements satisfied"
  else
    gh issue comment --body "❌ Agent $agent_name validation failed: $validation_errors"
    gh issue edit --add-label "needs-attention"
  fi
}
```

#### Continuous Issue Monitoring
```bash
# Real-time issue status dashboard
function show_framework_status() {
  echo "🔍 SPARC Framework Status:"
  echo "Design Blockers: $(gh issue list --label "design,blocker" --state open | wc -l)"
  echo "TDD Violations: $(gh issue list --label "tdd,violation" --state open | wc -l)"
  echo "Quality Issues: $(gh issue list --label "quality,blocker" --state open | wc -l)"
  echo "Tech Compliance: $(gh issue list --label "compliance,blocker" --state open | wc -l)"
  echo ""
  echo "📋 Critical Issues Requiring Immediate Attention:"
  gh issue list --label "critical,blocker" --state open --json number,title | jq -r '.[] | "🚨 Issue #\(.number): \(.title)"'
}
```

## Success Criteria with Issue Closure Requirements

### Phase 1 Complete When:
- [ ] All 7 design documents generated and validated
- [ ] Technology lock file created with exact versions  
- [ ] Implementation plan broken into executable phases
- [ ] All agent outputs cross-validated for consistency
- [ ] **ZERO open blocker issues with `design` label**
- [ ] All design phase issues resolved and closed
- [ ] Issue compliance report shows 100% phase completion

### Phase 2 Complete When:
- [ ] All planned features implemented following TDD
- [ ] 100% test coverage on critical paths
- [ ] All quality gates passing
- [ ] Code follows approved architecture patterns
- [ ] **ZERO open issues with `blocker` or `critical` labels**
- [ ] All TDD violations resolved and documented
- [ ] Technology compliance verified with zero violations
- [ ] Quality metrics meet or exceed framework standards

### Framework Completion Metrics:
- [ ] **Total Issues Created:** Documented count of all framework violations
- [ ] **Issues Resolved:** 100% closure rate for all blocker issues
- [ ] **Average Resolution Time:** Track time from issue creation to closure
- [ ] **Violation Categories:** Document most common violation types for process improvement
- [ ] **Framework Adherence:** Percentage of operations that passed without violations

## Framework Benefits

1. **Consistent Quality:** TDD-Guard ensures all code follows best practices
2. **Complete Documentation:** SPARC agents generate comprehensive design docs
3. **Technology Compliance:** Approved stack prevents dependency chaos
4. **Rapid Development:** Clear phases and validated handoffs reduce rework
5. **Maintainable Code:** Test-driven approach ensures long-term sustainability
6. **Full Transparency:** Git issues provide complete audit trail of all violations and resolutions
7. **Continuous Improvement:** Issue metrics identify process bottlenecks and common problems
8. **Accountability:** Every violation is tracked, assigned, and must be resolved before proceeding

## Critical Rules with Issue Enforcement

### NEVER:
- Skip any agent in the SPARC sequence
- Implement code without failing tests first
- Use technologies not in technology-lock.json
- Bypass TDD-Guard validation
- Proceed with incomplete design documents
- **Close issues without validation passing**
- **Proceed to next phase with open blocker issues**
- **Ignore or suppress automatic issue creation**
- **Resolve issues manually without fixing underlying problems**

### ALWAYS:
- Follow red-green-refactor TDD cycle
- Generate all design documents before implementation
- Use approved technologies with exact versions
- Validate outputs at each agent transition
- Maintain documentation throughout development
- **Create Git issues for ALL violations automatically**
- **Update issue status continuously during resolution**
- **Link related issues to show dependencies**
- **Validate issue resolution before closure**
- **Maintain complete audit trail via Git issues**

### MANDATORY ISSUE WORKFLOWS:
1. **Violation Detection** → Automatic Issue Creation
2. **Issue Assignment** → Responsible party identified
3. **Resolution Tracking** → Progress updates via comments
4. **Validation Required** → Automated verification before closure
5. **Dependency Management** → Linked issues updated when dependencies resolve
6. **Metrics Collection** → All issue data contributes to framework improvement

---

## Framework Enforcement Summary

This enhanced CLAUDE.md framework enforces disciplined, high-quality development through:

### 🤖 **Automated Agent Workflows**
- 7-stage SPARC methodology ensuring complete design before implementation
- Mandatory sequential execution with validation gates
- Cross-agent dependency management and handoff validation

### 🛡️ **TDD-Guard Integration** 
- Test-first development strictly enforced on all code changes
- Real-time violation detection and blocking
- Quality gate enforcement before commits

### 📋 **Comprehensive Git Issue Management**
- **100% violation tracking** - Every problem automatically becomes a tracked issue
- **Continuous status updates** - Real-time progress monitoring via issue comments
- **Blocker management** - Cannot proceed with open blocker issues
- **Audit trail** - Complete history of all violations and resolutions
- **Metrics collection** - Data-driven process improvement

### 🚫 **Zero-Tolerance Enforcement**
- No bypassing of framework requirements
- All violations must be resolved before proceeding
- Complete transparency through mandatory issue tracking
- Automated validation prevents human error or shortcuts

**All development MUST follow these guidelines without exception. Every violation will be tracked, every resolution will be validated, and complete compliance is required for framework success.**