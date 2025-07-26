#!/bin/bash

# GitHub CLI Authentication and Configuration Setup
# This script ensures GitHub CLI is properly configured for the workflow

set -e

echo "🔧 Setting up GitHub CLI Authentication and Configuration"
echo "========================================================"

# Check if GitHub CLI is installed
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI is not installed"
    echo "Please install GitHub CLI first:"
    echo "  - macOS: brew install gh"
    echo "  - Ubuntu: sudo apt install gh"
    echo "  - Windows: winget install GitHub.cli"
    exit 1
fi

echo "✅ GitHub CLI found: $(gh --version | head -1)"

# Check authentication status
echo ""
echo "🔐 Checking GitHub authentication status..."
if gh auth status &> /dev/null; then
    echo "✅ GitHub CLI is already authenticated"
    CURRENT_USER=$(gh api user --jq .login)
    echo "   Authenticated as: $CURRENT_USER"
else
    echo "❌ GitHub CLI is not authenticated"
    echo "Starting authentication process..."
    
    # Authenticate with GitHub
    echo "Please authenticate with GitHub CLI:"
    gh auth login
    
    # Verify authentication
    if gh auth status &> /dev/null; then
        CURRENT_USER=$(gh api user --jq .login)
        echo "✅ Successfully authenticated as: $CURRENT_USER"
    else
        echo "❌ Authentication failed"
        exit 1
    fi
fi

# Set up git configuration if not already set
echo ""
echo "🔧 Configuring Git..."
if ! git config --global user.name &> /dev/null; then
    echo "Setting up git user.name..."
    git config --global user.name "$CURRENT_USER"
fi

if ! git config --global user.email &> /dev/null; then
    echo "Setting up git user.email..."
    # Get email from GitHub API
    EMAIL=$(gh api user/emails --jq '.[] | select(.primary==true) | .email')
    git config --global user.email "$EMAIL"
fi

echo "✅ Git configured:"
echo "   Name: $(git config --global user.name)"
echo "   Email: $(git config --global user.email)"

# Create issue templates directory if it doesn't exist
echo ""
echo "📝 Setting up GitHub issue templates..."
mkdir -p .github/ISSUE_TEMPLATE

# Create bug report template
cat > .github/ISSUE_TEMPLATE/bug_report.md << 'EOF'
---
name: Bug Report
about: Report a bug or issue
title: '🐛 [BUG]: '
labels: bug
assignees: ''
---

## Problem Description
**What happened?**
A clear description of the bug.

**What was expected?**
A clear description of what you expected to happen.

## Context
**Current Task:**
- Working on: [task description]
- Phase: [development phase]

**Environment:**
- Technology Stack: [from technology-lock.json]
- Documentation Used: [from /approved-docs/]
- TDD State: [RED/GREEN/REFACTOR]

## Reproduction Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Error Details
```
[Error message/stack trace if applicable]
```

## Impact Assessment
- [ ] Blocks current development
- [ ] Affects other components
- [ ] Security concern
- [ ] Performance issue
- [ ] Technology compliance violation

## Proposed Solution
[If you have ideas for fixing the issue]

## Additional Context
[Any other context, screenshots, or relevant information]
EOF

# Create feature task template
cat > .github/ISSUE_TEMPLATE/feature_task.md << 'EOF'
---
name: Feature Implementation Task
about: Track implementation of a specific feature or component
title: '[TASK]: '
labels: enhancement
assignees: ''
---

## Task Description
**Feature:** [Feature name from code-plan.md]
**Phase:** [Development phase]
**Estimated Complexity:** [Easy/Medium/Complex]

## Requirements
**From PRD.md:**
- [Requirement 1]
- [Requirement 2]

**From Design Documents:**
- [Reference to SA.md/DA.md/API.md/UX.md sections]

## Technology Constraints
**Approved Technologies (from technology-lock.json):**
- [Technology 1 v.X.X.X]
- [Technology 2 v.X.X.X]

**Documentation Sources:**
- [Reference to /approved-docs/ sections]

## TDD Implementation Plan
### Test Cases to Write First:
- [ ] [Test case 1]
- [ ] [Test case 2]
- [ ] [Test case 3]

### Implementation Steps:
1. [ ] Write failing tests
2. [ ] Verify RED state with TDD-Guard
3. [ ] Implement minimal solution
4. [ ] Verify GREEN state with TDD-Guard
5. [ ] Refactor if needed
6. [ ] Update documentation

## Acceptance Criteria
- [ ] All tests pass
- [ ] TDD-Guard shows GREEN status
- [ ] No technology violations
- [ ] Code follows approved patterns
- [ ] Documentation updated
- [ ] GitHub issue referenced in commits

## Definition of Done
- [ ] Feature implemented as specified
- [ ] All tests passing
- [ ] Code reviewed
- [ ] No technology compliance violations
- [ ] Issue properly documented and closed
EOF

# Create technology violation template
cat > .github/ISSUE_TEMPLATE/tech_violation.md << 'EOF'
---
name: Technology Violation
about: Report violation of approved technology stack
title: '🚨 TECH VIOLATION: '
labels: violation, critical
assignees: ''
---

## Violation Details
**Type:** [Import/Dependency/Version/Documentation]
**File:** [File path]
**Line:** [Line number if applicable]
**Unauthorized Technology:** [Technology name and version]

## Current Context
**Approved Alternative:** [From technology-lock.json]
**Approved Documentation:** [From /approved-docs/]
**Task Being Worked On:** [Current task]

## Violation Evidence
```[language]
[Code snippet showing the violation]
```

## Required Actions
- [ ] Remove unauthorized technology
- [ ] Replace with approved alternative
- [ ] Update all dependent code
- [ ] Verify with tech validator
- [ ] Run compliance check

## Impact Assessment
- [ ] Blocks development
- [ ] Affects multiple files
- [ ] Requires architecture review
- [ ] Security implications

## Resolution Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]

**NO FURTHER DEVELOPMENT UNTIL RESOLVED**
EOF

echo "✅ Issue templates created"

# Create GitHub labels for the project
echo ""
echo "🏷️  Setting up GitHub labels..."

# Function to create label if it doesn't exist
create_label() {
    local name="$1"
    local color="$2"
    local description="$3"
    
    if ! gh label list --json name --jq '.[].name' | grep -q "^$name$"; then
        gh label create "$name" --color "$color" --description "$description"
        echo "   Created label: $name"
    else
        echo "   Label exists: $name"
    fi
}

# Create project-specific labels
create_label "tech-violation" "d73a4a" "Technology stack compliance violation"
create_label "tdd-violation" "d73a4a" "Test-driven development process violation"
create_label "workflow-violation" "d73a4a" "Agent workflow sequence violation"
create_label "architecture-review" "b60205" "Requires solution architect review"
create_label "enforcement" "0052cc" "Enforcement and compliance related"
create_label "phase-1" "0e8a16" "Phase 1: Setup & Database"
create_label "phase-2" "0e8a16" "Phase 2: Backend APIs"
create_label "phase-3" "0e8a16" "Phase 3: Authentication"
create_label "phase-4" "0e8a16" "Phase 4: Frontend Components"
create_label "phase-5" "0e8a16" "Phase 5: Feature Implementation"
create_label "phase-6" "0e8a16" "Phase 6: Integration & Testing"
create_label "approved-tech" "28a745" "Uses only approved technologies"
create_label "tdd-compliant" "28a745" "Follows TDD methodology"

echo "✅ GitHub labels configured"

# Set up git hooks for enforcement
echo ""
echo "🪝 Setting up git hooks for enforcement..."
mkdir -p .git/hooks

# Pre-commit hook for technology validation
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash

echo "🔍 Running pre-commit technology validation..."

# Check if technology validator exists
if [[ -f "/claude-config/scripts/validate-tech-stack.py" ]]; then
    python /claude-config/scripts/validate-tech-stack.py \
        --pre-commit \
        --tech-lock technology-lock.json
    
    if [[ $? -ne 0 ]]; then
        echo "❌ Technology validation failed"
        echo "🚨 Creating GitHub issue for violation..."
        gh issue create --title "🚨 PRE-COMMIT TECH VIOLATION" \
                        --label "tech-violation,critical" \
                        --body "Technology validation failed during pre-commit check.
                        
        **Action Required:**
        1. Fix technology violations
        2. Verify compliance
        3. Retry commit
        
        **Files to check:**
        $(git diff --cached --name-only)"
        exit 1
    fi
fi

# Check for commit message issue reference
if ! grep -qE "#[0-9]+" "$1" 2>/dev/null; then
    echo "❌ Commit message must reference a GitHub issue (e.g., #123)"
    echo "🚨 Creating GitHub issue for tracking..."
    ISSUE_NUM=$(gh issue create --title "🔗 Missing Issue Reference in Commit" \
                               --label "workflow-violation" \
                               --body "Commit attempted without GitHub issue reference.
                               
        **Required:**
        - All commits must reference GitHub issues
        - Format: 'feat: description #123' or 'Closes #123'
        
        **Current commit:**
        $(cat "$1" 2>/dev/null || echo 'No commit message')" \
                               --json number \
                               --jq .number)
    echo "Please reference issue #$ISSUE_NUM in your commit message"
    exit 1
fi

echo "✅ Pre-commit validation passed"
EOF

chmod +x .git/hooks/pre-commit

# Commit message template
cat > .git/hooks/prepare-commit-msg << 'EOF'
#!/bin/bash

# Add commit message template if no message provided
if [[ -z "$(cat "$1")" ]]; then
    cat > "$1" << 'TEMPLATE'
# feat/fix/docs/style/refactor/test/chore: Brief description

# Detailed description (if needed)

# References: #123 (or Closes #123)

# Tech used: [approved-technology-1], [approved-technology-2]
# TDD status: [RED->GREEN->REFACTOR]
TEMPLATE
fi
EOF

chmod +x .git/hooks/prepare-commit-msg

echo "✅ Git hooks configured"

# Create enforcement configuration
echo ""
echo "⚙️  Creating enforcement configuration..."
cat > .enforcement-config << 'EOF'
# Enforcement Configuration
STRICT_MODE=true
AUTO_ISSUE_CREATION=true
HALT_ON_VIOLATION=true
REQUIRE_GITHUB_ISSUES=true
TDD_MANDATORY=true
TECH_LOCK_ENFORCED=true

# Paths
TECH_LOCK_FILE=technology-lock.json
APPROVED_DOCS_DIR=/approved-docs/
CONFIG_DIR=/claude-config/

# GitHub Integration
GITHUB_AUTO_LABELS=true
ISSUE_AUTO_ASSIGNMENT=true
VIOLATION_NOTIFICATIONS=true
EOF

echo "✅ Enforcement configuration created"

# Final verification
echo ""
echo "🔍 Final verification..."
if gh auth status &> /dev/null; then
    echo "✅ GitHub CLI authentication: OK"
else
    echo "❌ GitHub CLI authentication: FAILED"
    exit 1
fi

if [[ -d ".github/ISSUE_TEMPLATE" ]]; then
    echo "✅ Issue templates: OK"
else
    echo "❌ Issue templates: MISSING"
    exit 1
fi

if [[ -x ".git/hooks/pre-commit" ]]; then
    echo "✅ Git hooks: OK"
else
    echo "❌ Git hooks: MISSING"
    exit 1
fi

echo ""
echo "🎉 GitHub setup complete!"
echo "========================================================"
echo "✅ GitHub CLI authenticated as: $(gh api user --jq .login)"
echo "✅ Issue templates configured"
echo "✅ GitHub labels created"
echo "✅ Git hooks installed"
echo "✅ Enforcement configuration ready"
echo ""
echo "Next steps:"
echo "1. Ensure technology-lock.json exists (created by Solution Architect)"
echo "2. Run workflow validation: python /claude-config/scripts/enforce-workflow.py"
echo "3. Begin development following TDD methodology"
echo ""
echo "Remember: ALL problems must be tracked via GitHub issues!"
EOF