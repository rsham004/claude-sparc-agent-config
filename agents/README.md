# SPARC Framework Agents

This directory contains the core SPARC (Structured Product Architecture Requirement Creation) agents for structured development workflows.

## Agent Overview

### Core Workflow Agents
The following agents must be executed in sequence for proper SPARC methodology:

1. **01-product-manager.md** - Product Requirements Document generation
2. **02-solution-architect.md** - Technical architecture design
3. **06-ux-designer.md** - User interface design
4. **11-visual-style-specialist.md** - Visual concept generation
5. **04-data-architect.md** - Database schema design
6. **05-senior-api-developer.md** - API specification design
7. **07-project-planner.md** - Implementation planning

### Utility Agents
Additional agents available for specialized tasks:

- **10-prompt-engineer.md** - AI prompt optimization (use as needed)

## Quick Start

1. **Download Framework:**
   ```bash
   git clone https://github.com/rsham004/claude-sparc-agent-config.git
   cd claude-sparc-agent-config
   ```

2. **Setup New Project:**
   ```bash
   ./setup-sparc-project.sh my-project-name
   ```

3. **Start Development:**
   ```bash
   claude "Execute Product Manager agent to create PRD"
   ```

## Framework Features

- **Sequential Dependency Management**: Each agent requires inputs from previous agents
- **Git Issue Integration**: All violations automatically create tracking issues
- **TDD-Guard Enforcement**: Test-driven development validation on all code changes
- **Technology Lock Compliance**: Only approved technologies permitted
- **Complete Audit Trail**: Full transparency through automated issue tracking

## Agent Structure

Each agent includes:
- **Role Definition**: Clear responsibility and context
- **Input Requirements**: Expected documents and information
- **Process Instructions**: Step-by-step execution guide
- **Output Format**: Structured deliverable specification
- **Quality Standards**: Validation and compliance requirements
- **Integration Requirements**: Coordination with other agents

---

*Part of the SPARC Framework - Structured Product Architecture Requirement Creation*