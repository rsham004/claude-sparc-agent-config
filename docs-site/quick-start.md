---
layout: default
title: "Quick Start Guide - SPARC Framework"
description: "Get started with SPARC Framework in minutes. Clone, setup, and begin building with 9 color-coded Claude Code agents, TDD-Guard enforcement, and YOLO protocol integration."
keywords: "SPARC Framework Quick Start, Claude Code setup, AI agents installation, TDD-Guard, YOLO protocols, ProductFoundry.ai"
permalink: /quick-start/
---

# 🚀 Quick Start Guide

Get up and running with SPARC Framework in just a few minutes.

## Prerequisites

Before you begin, ensure you have:

- **Claude Code CLI** installed (`npm install -g @anthropic-ai/claude-code`)
- **Git** for version control
- **Node.js** 16+ (for Claude Code)
- Basic familiarity with command line

## 1. Clone & Setup

```bash
git clone https://github.com/rsham004/claude-sparc-agent-config.git
cd claude-sparc-agent-config
```

## 2. Initialize Your Project

### Option A: Interactive Setup (Recommended)
```bash
./setup-sparc-project.sh
```

The script will:
- 🎯 Ask for your project name
- 📁 Create directory structure  
- 🤖 Install 9 color-coded agents
- ⚙️ Configure framework rules
- 🔍 Validate environment
- 📋 Create initial Git issue

### Option B: Direct Setup
```bash
./setup-sparc-project.sh my-amazing-project
```

## 3. Start Building

Begin with the Product Manager agent:

```bash
claude "Execute Product Manager agent to create PRD for my project idea"
```

Then describe your project requirements and let SPARC guide you through the structured workflow.

## 🎨 Understanding the Agent Colors

Each agent has a unique color following Claude Code best practices:

<div class="agent-quick-reference">
  <div class="agent-item">
    <span class="color-dot blue"></span>
    <strong>🔵 Product Manager</strong> - Foundation & Strategy
  </div>
  <div class="agent-item">
    <span class="color-dot orange"></span>
    <strong>🟠 Solution Architect</strong> - Technical Architecture
  </div>
  <div class="agent-item">
    <span class="color-dot purple"></span>
    <strong>🟣 UX Designer</strong> - User Experience Design
  </div>
  <div class="agent-item">
    <span class="color-dot yellow"></span>
    <strong>🟡 Visual Style Specialist</strong> - Creative Design
  </div>
  <div class="agent-item">
    <span class="color-dot green"></span>
    <strong>🟢 Data Architect</strong> - Database Design
  </div>
  <div class="agent-item">
    <span class="color-dot red"></span>
    <strong>🔴 Senior API Developer</strong> - Backend Logic
  </div>
  <div class="agent-item">
    <span class="color-dot black"></span>
    <strong>⚫ Project Planner</strong> - Implementation Planning
  </div>
  <div class="agent-item">
    <span class="color-dot brown"></span>
    <strong>🟤 Senior Coder</strong> - TDD Implementation
  </div>
  <div class="agent-item">
    <span class="color-dot red"></span>
    <strong>🔴 TDD-Guard Tester</strong> - Quality Assurance
  </div>
</div>

## 🔄 SPARC Workflow Sequence

Follow this mandatory sequence for best results:

### Phase 0: Setup ✅
- [x] Project initialization complete

### Phase 1: Design & Architecture
1. **🔵 Product Manager** → Create comprehensive PRD
2. **🟠 Solution Architect** → Design technical architecture  
3. **🟣 UX Designer** → Create interface designs
4. **🟡 Visual Style Specialist** → Generate visual concepts
5. **🟢 Data Architect** → Design database schema
6. **🔴 Senior API Developer** → Create API specifications
7. **⚫ Project Planner** → Generate implementation plan

### Phase 2: Implementation
8. **🟤 Senior Coder** → TDD-enforced implementation with YOLO protocols
9. **🔴 TDD-Guard Tester** → Quality assurance and test enforcement

### Phase 3: Quality & Deployment
- **🚀 YOLO Protocols** → Incremental delivery with canary deployments
- **📋 Git Issues** → Track all violations and progress
- **🔄 CI/CD Pipeline** → Automated testing and deployment

## 🧪 TDD-Guard Integration

SPARC enforces test-driven development through TDD-Guard:

- ✅ **Tests First** - All code must have tests written first
- 📋 **Auto Tracking** - Violations create Git issues automatically  
- 🔒 **Quality Gates** - Agents cannot proceed without compliance
- 📊 **Complete Audit** - Full trail of decisions and changes

## 🗣️ Natural Language Commands

Use these commands to interact with your SPARC project:

```bash
# Check framework status
claude "Show current SPARC framework status and next steps"

# Execute next agent in sequence  
claude "Execute next agent in SPARC sequence"

# List blocking issues
claude "List all open blocking issues that need resolution"

# Validate current phase
claude "Validate current phase completion before proceeding"

# Generate compliance report
claude "Generate framework compliance report"
```

## 📁 Project Structure Created

After setup, you'll have:

```
your-project/
├── CLAUDE.md                    # Project memory and framework rules
├── .claude/agents/your-project/ # Agent configurations
├── docs/design/your-project/    # Design documents location
└── .git/                        # Git repository with issue tracking
```

## 🤝 Community Integration

Your project is now part of the ProductFoundry.ai ecosystem:

- 🌟 **Built with community values** - Ethical, inclusive, transparent
- 📋 **Licensed under CC BY-NC 4.0** - Open source with fair use
- 🚀 **Join weekly sessions** - Connect with other AI builders
- 📚 **Contribute back** - Share your innovations with the community

## ⚡ Quick Commands Reference

| Command | Purpose |
|---------|---------|
| `claude "Execute Product Manager agent"` | Start workflow with PRD |
| `claude "Show blocking issues"` | View current blockers |
| `claude "Validate TDD compliance"` | Check test coverage |
| `claude "Generate status report"` | Get project overview |
| `claude "@.claude/agents/PROJECT/framework-rules.md"` | Import rules |

## 🆘 Troubleshooting

### Common Issues

**Claude Code not found:**
```bash
npm install -g @anthropic-ai/claude-code
```

**Permission denied on script:**
```bash
chmod +x setup-sparc-project.sh
```

**Git not initialized:**
```bash
git init
```

**Agent not executing:**
- Ensure previous phase is complete
- Check for blocking Git issues
- Validate framework compliance

## 🎯 Next Steps

1. **Execute Product Manager** to create your PRD
2. **Follow SPARC sequence** strictly - each agent builds on the previous
3. **Resolve blocking issues** before proceeding to next phase
4. **Join ProductFoundry.ai** community for support and collaboration

---

## 🚀 Ready to Build?

Your SPARC Framework is configured and ready. Start with:

```bash
claude "I want to create a new project. Execute the Product Manager agent to help me create a comprehensive PRD."
```

Then describe your project idea and let the framework guide you through structured, high-quality development.

**Join the community:** [www.productfoundry.ai](https://www.productfoundry.ai) 🌟

<style>
.agent-quick-reference {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 0.5rem;
  margin: 2rem 0;
  padding: 1rem;
  background: #f8f9fa;
  border-radius: 8px;
}

.agent-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
}

.color-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  display: inline-block;
}

.color-dot.blue { background: #007bff; }
.color-dot.orange { background: #fd7e14; }
.color-dot.purple { background: #6f42c1; }
.color-dot.yellow { background: #ffc107; }
.color-dot.green { background: #28a745; }
.color-dot.red { background: #dc3545; }
.color-dot.black { background: #343a40; }
.color-dot.brown { background: #795548; }

table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0;
}

th, td {
  padding: 0.75rem;
  text-align: left;
  border-bottom: 1px solid #dee2e6;
}

th {
  background: #f8f9fa;
  font-weight: 600;
}

code {
  background: #f8f9fa;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-size: 0.9em;
}

pre {
  background: #f8f9fa;
  padding: 1rem;
  border-radius: 8px;
  overflow-x: auto;
}
</style>