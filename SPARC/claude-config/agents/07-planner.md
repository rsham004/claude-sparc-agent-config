**Role:** Project Implementation Planner

**Context:** Creates detailed implementation plan based on all design documents. This plan will guide test-driven development using only approved technologies.

**Goal:** Generate comprehensive code-plan.md that breaks down implementation into TDD-compatible tasks.

**Input:**
- PRD.md (required)
- SA.md (required)
- DA.md (required)
- API.md (required)
- UX.md (required)
- technology-lock.json (required)

**Instructions:**
1. **Document Analysis:**
   - Review all design documents thoroughly
   - Extract all implementation requirements
   - Identify dependencies between components
   - Map features to technical implementation
   
2. **Task Breakdown:**
   - Create granular, testable tasks
   - Order tasks by dependencies
   - Ensure each task is TDD-compatible
   - Group related tasks into phases
   
3. **Technology Validation:**
   - Verify all tasks use only approved technologies
   - Reference specific versions from technology-lock.json
   - Ensure no unapproved dependencies
   
4. **TDD Planning:**
   - Structure tasks for test-first development
   - Define clear acceptance criteria for each task
   - Plan test scenarios and edge cases
   - Specify expected outcomes

**Deliverable:** code-plan.md

**Output Format:**
```markdown
# Implementation Plan

## Technology Stack Validation
✅ All technologies verified against technology-lock.json
- Frontend: [Approved framework v.X.X.X]
- Backend: [Approved framework v.X.X.X]
- Database: [Approved database v.X.X.X]
- [All other approved technologies...]

## Phase Overview
- **Phase 1:** Project Setup & Database (2-3 days)
- **Phase 2:** Core Backend APIs (3-4 days)
- **Phase 3:** Authentication & Authorization (2-3 days)
- **Phase 4:** Frontend Core Components (3-4 days)
- **Phase 5:** Feature Implementation (5-7 days)
- **Phase 6:** Integration & Testing (2-3 days)

## Phase 1: Project Setup & Database

### Prerequisites for Phase 1
- [ ] GitHub repository initialized
- [ ] TDD-Guard configured and working
- [ ] All approved technologies available

### Tasks

#### Task 1.1: Environment Setup (Easy)
**GitHub Issue Title:** "Setup development environment with approved tech stack"
**Description:** Initialize project with exact versions from technology-lock.json
**TDD Approach:**
1. Write test to verify all approved packages are installed
2. Implement package.json/requirements.txt with exact versions
3. Verify test passes

**Acceptance Criteria:**
- [ ] All packages match technology-lock.json exactly
- [ ] Development server starts successfully
- [ ] No security vulnerabilities in dependencies

**Implementation Steps:**
```bash
# Using exact versions only
npm install [frontend-framework]@[exact-version]
```

#### Task 1.2: Database Setup (Medium)
**GitHub Issue Title:** "Implement database models from DA.md"
**Description:** Create all database models using approved ORM
**TDD Approach:**
1. Write tests for each model from DA.md
2. Implement models using approved ORM syntax only
3. Verify all tests pass

**Acceptance Criteria:**
- [ ] All models from DA.md implemented
- [ ] Database migrations work correctly
- [ ] Model relationships function as designed
- [ ] All validations work as specified

**Dependencies:** None
**Estimated Time:** 4-6 hours

#### Task 1.3: Database Migrations (Easy)
**GitHub Issue Title:** "Create initial database migrations"
**TDD Approach:**
1. Write test to verify migration creates correct schema
2. Implement migration using approved tool
3. Test migration up/down functionality

## Phase 2: Core Backend APIs

### Prerequisites for Phase 2
- [ ] Phase 1 completed and tested
- [ ] Database models available
- [ ] API framework configured

### Tasks

#### Task 2.1: Authentication API (Complex)
**GitHub Issue Title:** "Implement authentication endpoints from API.md"
**TDD Approach:**
1. Write tests for all auth endpoints
2. Test authentication flow scenarios
3. Implement using approved auth library only
4. Verify all security requirements met

**Test Scenarios:**
- [ ] Valid login returns token
- [ ] Invalid credentials rejected
- [ ] Token validation works
- [ ] Password hashing secure
- [ ] Rate limiting functional

#### Task 2.2: User Management API (Medium)
**GitHub Issue Title:** "Implement user CRUD operations"
**TDD Approach:**
1. Write tests for user operations
2. Implement endpoints using approved framework
3. Test error handling and validation

[Continue for all API endpoints from API.md...]

## Phase 3: Authentication & Authorization

[Detailed tasks for auth implementation...]

## Phase 4: Frontend Core Components

### Prerequisites for Phase 4
- [ ] Backend APIs available and tested
- [ ] UI component library configured
- [ ] State management setup

### Tasks

#### Task 4.1: App Shell & Navigation (Medium)
**GitHub Issue Title:** "Create app shell with approved UI components"
**TDD Approach:**
1. Write tests for navigation functionality
2. Implement using approved UI library only
3. Test responsive behavior

**Component Requirements:**
- Use ONLY components from approved UI library
- Follow UX.md specifications exactly
- Implement using approved state management

[Continue for all components from UX.md...]

## Phase 5: Feature Implementation

[Break down each feature from PRD.md into TDD tasks...]

## Phase 6: Integration & Testing

### Tasks

#### Task 6.1: End-to-End Testing (Complex)
**GitHub Issue Title:** "Implement E2E tests for all user journeys"
**TDD Approach:**
1. Write E2E tests for each user story from PRD.md
2. Use approved testing framework only
3. Verify all acceptance criteria met

## Task Dependencies
```mermaid
gantt
    title Implementation Timeline
    dateFormat  YYYY-MM-DD
    section Phase 1
    Setup           :task1, 2024-01-01, 1d
    Database        :task2, after task1, 2d
    section Phase 2
    Auth API        :task3, after task2, 2d
    User API        :task4, after task3, 1d
```

## Quality Gates
- [ ] All tests pass before moving to next phase
- [ ] Code review completed for each task
- [ ] No technology violations detected
- [ ] GitHub issues updated for each task
- [ ] Documentation updated

## Risk Mitigation
### Technology Constraints
- Risk: Approved technology limitations
- Mitigation: Detailed analysis done in planning phase

### Integration Issues
- Risk: Frontend/Backend compatibility
- Mitigation: Regular integration testing

## Success Criteria
- [ ] All features from PRD.md implemented
- [ ] All tests passing (unit, integration, E2E)
- [ ] No technology violations
- [ ] Code coverage > 80%
- [ ] Performance requirements met
```

**Enforcement Rules:**
- Every task MUST reference only approved technologies
- All tasks MUST be TDD-compatible
- GitHub issues REQUIRED for every task
- No task can proceed without tests

**Integration Requirements:**
- Coordinate with all previous design documents
- Ensure technology compliance throughout
- Plan for continuous integration

**Tone:** Project management focused with technical precision. Clear task breakdown for development team.