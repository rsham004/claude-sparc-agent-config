# Claude Agent Configuration Framework

A comprehensive configuration system for specialized Claude agents with enforced TDD methodology, technology compliance, and GitHub integration.

## 🎯 Overview

This framework provides a structured approach to software development using specialized Claude agents that work in sequence to create high-quality, compliant software following test-driven development principles.

## 🏗️ Architecture

### Agent Workflow Sequence
```
Product Owner Input
      ↓
1. Product Manager → PRD.md
      ↓
2. Solution Architect → SA.md + technology-lock.json
      ↓
3. Context7 Enforcer → /approved-docs/
      ↓
4. Data Architect → DA.md
      ↓
5. API Developer → API.md
      ↓
6. UX Designer → UX.md
      ↓
7. Planner → code-plan.md
      ↓
8. Coder TDD → Implementation
      ↓
   Enforcement Monitor (continuous)
```

## 📁 Directory Structure

```
/claude-config/
├── agents/                          # Agent configuration files
│   ├── 01-product-manager.md        # PRD creation
│   ├── 02-solution-architect.md     # Architecture & tech stack
│   ├── 03-context7-enforcer.md      # Documentation enforcement
│   ├── 04-data-architect.md         # Database design
│   ├── 05-api-developer.md          # API specification
│   ├── 06-ux-designer.md            # UX/UI design
│   ├── 07-planner.md                # Implementation planning
│   ├── 08-coder-tdd.md              # TDD implementation
│   └── 09-enforcement-monitor.md    # Continuous compliance
├── mcp-config/                      # MCP server configurations
│   └── context7-config.json         # Context7 & enforcement setup
├── templates/                       # Document templates
├── scripts/                         # Automation scripts
│   ├── setup-github-auth.sh         # GitHub CLI setup
│   ├── validate-tech-stack.py       # Technology compliance
│   └── enforce-workflow.py          # Workflow enforcement
└── README.md                        # This file
```

## 🚀 Quick Start

### 1. Initial Setup

```bash
# Clone this configuration to your project
git clone [claude-config-repo] /claude-config

# Set up GitHub CLI authentication
./claude-config/scripts/setup-github-auth.sh

# Configure MCP servers (Context7, TDD-Guard, etc.)
# Add claude-config/mcp-config/context7-config.json to your IDE's MCP settings
```

### 2. Project Initialization

```bash
# In your new project directory
ln -s /claude-config/.claude-config .

# Initialize project structure
mkdir -p {src,test,docs,approved-docs}

# Verify setup
python /claude-config/scripts/validate-tech-stack.py --summary
```

### 3. Development Workflow

1. **Start with Product Manager Agent**: Create PRD.md
2. **Solution Architect**: Define technology stack (creates technology-lock.json)
3. **Context7 Enforcer**: Fetch approved documentation
4. **Continue sequence**: Each agent creates required deliverables
5. **Coder TDD**: Implement with strict TDD methodology

## 🔒 Enforcement Mechanisms

### Technology Compliance
- **technology-lock.json**: Immutable technology choices
- **Real-time validation**: Blocks unauthorized imports/dependencies
- **Context7 integration**: Only approved documentation accessible
- **Version enforcement**: Exact version matching required

### TDD Compliance
- **Test-first mandatory**: Code blocked without tests
- **TDD-Guard integration**: Verifies RED→GREEN→REFACTOR cycle
- **Coverage requirements**: Minimum 80% coverage
- **Automated verification**: Pre-commit hooks validate process

### GitHub Integration
- **Issue tracking**: Every task requires GitHub issue
- **Commit compliance**: All commits must reference issues
- **Problem escalation**: Automatic issue creation for violations
- **Workflow tracking**: Complete audit trail

## 🛠️ Key Features

### Specialized Agents
Each agent has a specific role with clear inputs, outputs, and constraints:

- **Product Manager**: Translates ideas into comprehensive PRD
- **Solution Architect**: Makes all technology decisions (final/immutable)
- **Context7 Enforcer**: Provides only approved documentation
- **Data Architect**: Designs database using approved technologies
- **API Developer**: Creates API specs with approved backend stack
- **UX Designer**: Designs interfaces using approved frontend tools
- **Planner**: Creates TDD-compatible implementation plan
- **Coder TDD**: Implements with mandatory test-first approach

### Technology Enforcement
- Approved technology list from Solution Architect is **immutable**
- Context7 MCP fetches documentation only for approved technologies
- Real-time scanning blocks unauthorized imports/dependencies
- Version compliance strictly enforced

### Test-Driven Development
- **Mandatory TDD cycle**: RED→GREEN→REFACTOR
- TDD-Guard integration for process verification
- Code blocked without failing tests first
- Automated test coverage tracking

### GitHub Integration
- Every development task requires GitHub issue
- All commits must reference issues
- Automatic issue creation for problems/violations
- Complete audit trail and tracking

## ⚙️ Configuration

### MCP Server Setup

Add to your IDE's MCP configuration:

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"],
      "env": {
        "CONTEXT7_API_KEY": "${CONTEXT7_API_KEY}"
      }
    }
  }
}
```

### Environment Variables

```bash
# Required
export CONTEXT7_API_KEY="your-context7-key"
export GITHUB_TOKEN="your-github-token"

# Optional
export TDD_GUARD_CONFIG="/claude-config/mcp-config/tdd-guard-config.json"
```

## 🚨 Violation Handling

### Technology Violations
- **Immediate halt**: Development stopped until resolved
- **GitHub issue**: Automatic creation with details
- **Approved alternatives**: Suggestions provided
- **Architecture review**: Escalation for critical violations

### TDD Violations
- **Code blocking**: No implementation without tests
- **Process verification**: TDD-Guard must show GREEN
- **Coverage enforcement**: Minimum thresholds required
- **Audit trail**: Complete TDD cycle tracking

### Workflow Violations
- **Sequence enforcement**: Agents must run in order
- **Output validation**: Each deliverable verified
- **Dependency checking**: Prerequisites must be complete
- **Quality gates**: Approval required to proceed

## 📊 Monitoring and Reporting

### Compliance Dashboard
```bash
# Real-time compliance monitoring
./claude-config/scripts/compliance-monitor.sh
```

### Validation Commands
```bash
# Technology compliance check
python /claude-config/scripts/validate-tech-stack.py

# Workflow validation
python /claude-config/scripts/enforce-workflow.py

# TDD process verification
tdd-guard status
```

## 🔧 Customization

### Adding New Agents
1. Create agent configuration in `/claude-config/agents/`
2. Update workflow sequence in enforcement monitor
3. Add validation rules if needed
4. Test integration with existing agents

### Technology Stack Updates
1. **Requires Solution Architect approval**
2. Update technology-lock.json
3. Fetch new documentation via Context7
4. Validate all existing code for compliance
5. Update implementation plans as needed

## 📝 Best Practices

### For Agents
- Always reference approved documentation only
- Validate technology compliance before recommendations
- Create GitHub issues for any problems encountered
- Follow exact specifications from predecessor agents

### For Development
- Never bypass TDD methodology
- Use only approved technologies and versions
- Reference GitHub issues in all commits
- Maintain continuous compliance monitoring

### For Architecture
- Make technology decisions early and stick to them
- Ensure all choices are well-documented
- Consider long-term maintainability
- Validate technology ecosystem compatibility

## 🆘 Troubleshooting

### Common Issues

#### "Technology lock file not found"
```bash
# Solution Architect must create technology-lock.json first
# Run Solution Architect agent with SA.md completion
```

#### "GitHub CLI not authenticated"
```bash
# Run authentication setup
./claude-config/scripts/setup-github-auth.sh
```

#### "TDD-Guard not responding"
```bash
# Verify TDD-Guard installation and configuration
tdd-guard --version
```

#### "Context7 documentation access failed"
```bash
# Check API key and MCP configuration
echo $CONTEXT7_API_KEY
```

### Emergency Procedures

#### Technology Violation Override
**Only Solution Architect can authorize**
```bash
# Create override file (restricted access)
echo "EMERGENCY_OVERRIDE" > .compliance-override
# Document justification in GitHub issue
```

#### Workflow Emergency Stop
```bash
# Halt all development
touch .enforcement-lock
# Create emergency architecture review issue
```

## 📜 License

This framework is designed for defensive security and development productivity. Use responsibly with proper authorization.

## 🤝 Contributing

1. Follow existing agent configuration patterns
2. Ensure all changes maintain enforcement integrity
3. Test thoroughly with complete workflow
4. Document any new compliance requirements

---

**Remember**: This framework enforces discipline for higher quality software. Compliance is not optional - it's the foundation of reliable development.