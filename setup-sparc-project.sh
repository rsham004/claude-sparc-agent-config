#!/bin/bash
# SPARC Framework Project Setup Script
# Automated installation and configuration for new projects

set -e  # Exit on error

# Colors for output (ProductFoundry.ai branding)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
ORANGE='\033[0;33m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# ProductFoundry.ai brand colors
FOUNDRY_BLUE='\033[38;5;39m'
FOUNDRY_GREEN='\033[38;5;46m'
FOUNDRY_PURPLE='\033[38;5;129m'

# Framework paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SPARC_AGENTS_DIR="$SCRIPT_DIR/agents"

# Print colored output
print_status() {
    echo -e "${BLUE}🔍 $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Display ProductFoundry.ai banner
show_banner() {
    echo -e "${FOUNDRY_BLUE}${BOLD}"
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                              ║"
    echo -e "║   ${WHITE}🌟 SPARC Framework - Built by ProductFoundry.ai Community 🌟${FOUNDRY_BLUE}          ║"
    echo "║                                                                              ║"
    echo -e "║   ${FOUNDRY_GREEN}🚀 Where AI Builders Collaborate to Shape the Future${FOUNDRY_BLUE}                      ║"
    echo -e "║   ${FOUNDRY_PURPLE}🤝 Open Source • Community Driven • Ethically Built${FOUNDRY_BLUE}                      ║"
    echo -e "║   ${WHITE}📍 Join us: www.productfoundry.ai${FOUNDRY_BLUE}                                         ║"
    echo "║                                                                              ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    echo ""
}

# Main setup function
setup_sparc_project() {
    show_banner
    
    echo -e "${FOUNDRY_BLUE}${BOLD}"
    echo "🎯 SPARC Framework Project Setup"
    echo "================================="
    echo -e "${NC}"
    
    # Step 1: Get project name
    if [ -z "$1" ]; then
        echo "Please provide a project name:"
        read -p "📝 Project name: " PROJECT_NAME
    else
        PROJECT_NAME="$1"
    fi
    
    # Validate project name
    if [[ ! "$PROJECT_NAME" =~ ^[a-zA-Z0-9_-]+$ ]]; then
        print_error "Project name must contain only letters, numbers, underscores, and hyphens"
        exit 1
    fi
    
    print_status "Setting up SPARC framework for: $PROJECT_NAME"
    
    # Step 2: Create directory structure
    print_status "Creating project directory structure..."
    
    mkdir -p ".claude/agents/$PROJECT_NAME"
    mkdir -p ".claude/config/$PROJECT_NAME"
    mkdir -p "docs/design/$PROJECT_NAME"
    mkdir -p "docs/agents/$PROJECT_NAME"
    
    print_success "Created project directories"
    echo "   📁 .claude/agents/$PROJECT_NAME/ (Agent configurations)"
    echo "   📁 .claude/config/$PROJECT_NAME/ (Framework configuration)"
    echo "   📁 docs/design/$PROJECT_NAME/ (Design documents)"
    echo "   📁 docs/agents/$PROJECT_NAME/ (Agent documentation)"
    
    # Step 3: Install SPARC agents
    print_status "Installing SPARC agents..."
    
    # Define core SPARC agents with color coding (Claude Code best practices)
    declare -A agents=(
        ["colored/01-product-manager.md"]="🔵 Product Requirements Document generation"
        ["colored/02-solution-architect.md"]="🟠 Technical architecture design"  
        ["colored/06-ux-designer.md"]="🟣 User interface design"
        ["colored/11-visual-style-specialist.md"]="🟡 Visual concept generation"
        ["colored/04-data-architect.md"]="🟢 Database schema design"
        ["colored/05-senior-api-developer.md"]="🔴 API specification design"
        ["colored/07-project-planner.md"]="⚫ Implementation planning"
        ["colored/10-prompt-engineer.md"]="🟤 AI prompt optimization"
    )
    
    # Agent descriptions with ProductFoundry.ai branding
    declare -A agent_descriptions=(
        ["colored/01-product-manager.md"]="Foundation & Strategy"
        ["colored/02-solution-architect.md"]="Architecture & Technical Foundation"  
        ["colored/06-ux-designer.md"]="User Experience & Interface Design"
        ["colored/11-visual-style-specialist.md"]="Creative & Visual Design"
        ["colored/04-data-architect.md"]="Data & Database Design"
        ["colored/05-senior-api-developer.md"]="API Development & Backend Logic"
        ["colored/07-project-planner.md"]="Implementation Planning & Coordination"
        ["colored/10-prompt-engineer.md"]="AI Optimization & Enhancement"
    )
    
    agent_count=0
    for agent_file in "${!agents[@]}"; do
        # Try multiple possible source locations
        source_file=""
        for possible_source in \
            "$SPARC_AGENTS_DIR/agents/$agent_file" \
            "$SPARC_AGENTS_DIR/$agent_file" \
            "./$agent_file"; do
            if [ -f "$possible_source" ]; then
                source_file="$possible_source"
                break
            fi
        done
        
        if [ -n "$source_file" ]; then
            # Copy with original filename (remove colored/ prefix)
            target_file=$(basename "$agent_file")
            cp "$source_file" ".claude/agents/$PROJECT_NAME/$target_file"
            echo -e "   ${agents[$agent_file]} - ${FOUNDRY_PURPLE}${agent_descriptions[$agent_file]}${NC}"
            ((agent_count++))
        else
            print_warning "Agent not found: $agent_file"
        fi
    done
    
    if [ $agent_count -eq 0 ]; then
        print_error "No SPARC agents found. Please ensure agents are available in:"
        echo "   - $SPARC_AGENTS_DIR/"
        echo "   - Current directory"
        exit 1
    fi
    
    # Step 4: Create framework rules
    print_status "Creating framework rules..."
    
    cat > ".claude/agents/$PROJECT_NAME/framework-rules.md" << EOF
# SPARC Framework Rules for $PROJECT_NAME

## Mandatory Workflow Sequence
0. **Project Initialization** → Setup and validation (COMPLETED ✅)
1. **Product Manager** → PRD Generation
2. **Solution Architect** → Technical Architecture
3. **UX Designer** → UI Design Document  
4. **Visual Style Specialist** → Visual Concepts
5. **Data Architect** → Database Schema
6. **Senior API Developer** → API Specification
7. **Project Planner** → Implementation Plan
8. **TDD-Guard** → Implementation with test-first validation

Additional Agent Available:
- **Prompt Engineer** → AI prompt optimization (use as needed)

## Critical Enforcement Rules
- ❌ NO agent may proceed without required inputs from previous agent
- 📋 ALL violations MUST create Git issues automatically
- 🧪 TDD-Guard validation required for all code changes
- 🔒 Technology lock compliance mandatory
- 📝 Complete documentation required at each phase

## Project Context
- **Project:** $PROJECT_NAME
- **Framework:** SPARC with TDD-Guard
- **Agent Directory:** .claude/agents/$PROJECT_NAME
- **Initialized:** $(date)
- **Status:** Ready for Phase 1 (Product Manager)

## Import Main Framework
@../../../CLAUDE.md

## Next Steps
1. Run: \`claude "Execute Product Manager agent to create PRD"\`
2. Provide project idea and requirements
3. Follow SPARC sequence strictly
4. Resolve all blocking issues before proceeding

---
*Auto-generated by SPARC Framework Setup*
EOF
    
    print_success "Framework rules created"
    
    # Step 5: Create project-specific CLAUDE.md
    print_status "Creating project-specific CLAUDE.md..."
    
    cat > "CLAUDE.md" << EOF
# $PROJECT_NAME - SPARC Development Framework

## Project Overview
**Project Name:** $PROJECT_NAME  
**Framework:** SPARC with TDD-Guard Enforcement  
**Initialized:** $(date)  
**Agent Directory:** .claude/agents/$PROJECT_NAME/  

This project follows the SPARC (Structured Product Architecture Requirement Creation) methodology with Test-Driven Development enforcement.

## Current Phase Status
- [x] Phase 0: Project initialization complete ✅
- [ ] Phase 1: Requirements gathering (Product Manager)
- [ ] Phase 2: User experience design (UX Designer)  
- [ ] Phase 3: Visual style generation (Visual Style Specialist)
- [ ] Phase 4: Technical architecture (Solution Architect)
- [ ] Phase 5: Database design (Data Architect)
- [ ] Phase 6: API specification (Senior API Developer)
- [ ] Phase 7: Implementation planning (Project Planner)
- [ ] Phase 8: TDD implementation and validation

## Framework Rules Import
@.claude/agents/$PROJECT_NAME/framework-rules.md

## Design Documents Location
All design documents will be created in: \`docs/design/$PROJECT_NAME/\`

## Development Guidelines
- **Test-First:** All code must have tests written first
- **Agent Workflow:** Follow SPARC sequence strictly  
- **Issue Tracking:** All violations create Git issues automatically
- **Technology Lock:** Only approved technologies permitted
- **Documentation:** Maintain design docs throughout development

## Quick Commands
- **Start Workflow:** \`claude "Execute Product Manager agent to create PRD"\`
- **Check Status:** \`claude "Show current SPARC framework status"\`
- **Show Blockers:** \`claude "List all open blocking issues"\`
- **Validate Phase:** \`claude "Validate current phase completion"\`
- **Next Step:** \`claude "What is the next required step in SPARC workflow?"\`

## Next Steps
🚀 **Ready to begin!** Run the Product Manager agent:
\`\`\`bash
claude "I want to create a new project. Execute the Product Manager agent to help me create a comprehensive PRD."
\`\`\`

Then provide your project idea and requirements.

---
*Generated by SPARC Framework on $(date)*
EOF
    
    print_success "Project-specific CLAUDE.md created"
    
    # Step 6: Initialize Git (if not exists)
    if [ ! -d ".git" ]; then
        print_status "Initializing Git repository..."
        git init
        print_success "Git repository initialized"
    else
        print_success "Git repository already exists"
    fi
    
    # Step 7: Validate environment
    print_status "Validating environment..."
    
    # Check Claude Code CLI
    if command -v claude &> /dev/null; then
        print_success "Claude Code CLI available"
    else
        print_warning "Claude Code CLI not found"
        echo "   Install with: npm install -g @anthropic-ai/claude-code"
    fi
    
    # Check Node.js
    if command -v node &> /dev/null; then
        node_version=$(node --version)
        print_success "Node.js available: $node_version"
    else
        print_warning "Node.js not found (required for Claude Code)"
    fi
    
    # Step 8: Create initial Git issue for project setup
    if command -v gh &> /dev/null && [ -d ".git" ]; then
        print_status "Creating initial project setup issue..."
        
        gh issue create \
            --title "SPARC Framework Setup Complete for $PROJECT_NAME" \
            --label "setup,sparc,initialization" \
            --body "## Project Initialization Complete

**Project:** $PROJECT_NAME  
**Framework:** SPARC with TDD-Guard  
**Initialized:** $(date)  

### Setup Results
- ✅ Directory structure created
- ✅ $agent_count SPARC agents installed
- ✅ Framework rules configured
- ✅ Project-specific CLAUDE.md created
- ✅ Git repository ready

### Next Steps
1. Execute Product Manager agent to create PRD
2. Follow SPARC workflow sequence
3. Ensure all blocking issues resolved before proceeding

### Framework Status
Ready to begin Phase 1: Requirements gathering

---
*Auto-generated by SPARC Framework Setup Script*" \
            2>/dev/null && print_success "Initial setup issue created" || print_warning "Could not create setup issue (GitHub CLI not configured)"
    fi
    
    # Step 9: Final validation and summary
    print_status "Final validation..."
    
    # Count installed agents
    installed_agents=$(ls -1 ".claude/agents/$PROJECT_NAME/" 2>/dev/null | wc -l)
    
    echo ""
    echo -e "${FOUNDRY_GREEN}${BOLD}🎉 SPARC Framework Setup Complete!${NC}"
    echo -e "${FOUNDRY_BLUE}${'='*50}${NC}"
    echo ""
    echo -e "${WHITE}📊 Setup Summary:${NC}"
    echo -e "   ${FOUNDRY_BLUE}Project:${NC} $PROJECT_NAME"
    echo -e "   ${FOUNDRY_GREEN}Agents Installed:${NC} $installed_agents"
    echo -e "   ${FOUNDRY_PURPLE}Framework:${NC} SPARC with TDD-Guard"
    echo -e "   ${FOUNDRY_GREEN}Status:${NC} Ready for development"
    echo ""
    echo -e "${FOUNDRY_GREEN}🚀 Next Steps:${NC}"
    echo -e "   ${WHITE}1.${NC} Run: ${FOUNDRY_BLUE}claude \"Execute Product Manager agent to create PRD\"${NC}"
    echo -e "   ${WHITE}2.${NC} Describe your project idea and requirements"
    echo -e "   ${WHITE}3.${NC} Follow the SPARC workflow sequence"
    echo -e "   ${WHITE}4.${NC} Resolve any blocking issues before proceeding"
    echo ""
    echo -e "${FOUNDRY_PURPLE}📁 Key Files Created:${NC}"
    echo -e "   ${WHITE}•${NC} CLAUDE.md (Project memory)"
    echo -e "   ${WHITE}•${NC} .claude/agents/$PROJECT_NAME/ (Agent configurations)"
    echo -e "   ${WHITE}•${NC} docs/design/$PROJECT_NAME/ (Design documents location)"
    echo ""
    echo -e "${FOUNDRY_BLUE}✨ Framework Features:${NC}"
    echo -e "   ${WHITE}•${NC} Color-coded agent workflow (Claude Code best practices)"
    echo -e "   ${WHITE}•${NC} Git issue tracking for all violations"
    echo -e "   ${WHITE}•${NC} TDD-Guard enforcement"
    echo -e "   ${WHITE}•${NC} Technology compliance validation"
    echo -e "   ${WHITE}•${NC} Complete audit trail"
    echo ""
    echo -e "${FOUNDRY_GREEN}🤝 ProductFoundry.ai Community:${NC}"
    echo -e "   ${WHITE}•${NC} Built by AI Builders collaborating together"
    echo -e "   ${WHITE}•${NC} Join our weekly sessions: ${FOUNDRY_BLUE}www.productfoundry.ai${NC}"
    echo -e "   ${WHITE}•${NC} Share your builds and learn from others"
    echo -e "   ${WHITE}•${NC} Licensed under Creative Commons BY-NC 4.0"
    echo ""
    
    return 0
}

# Script execution
if [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    # Script is being executed directly
    setup_sparc_project "$@"
fi