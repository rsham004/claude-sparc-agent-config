# Visual Style Specialist Agent Configuration

## Overview

The Visual Style Specialist is an expert agent that generates multiple differentiated visual UI concepts based on specific style requirements. It translates abstract stylistic descriptions into concrete visual interface designs while maintaining functional consistency across all variations.

## Key Capabilities

### 1. Style Generation
- Creates 9 distinct visual styles from a single base UI structure
- Maintains consistent functionality across all style variations
- Ensures clear visual differentiation between styles
- Produces high-fidelity mockups suitable for stakeholder review

### 2. Supported Visual Styles

1. **Modern Minimal** - Clean, airy designs with pastel colors and generous white space
2. **Bold Energetic** - High-contrast, vibrant designs with dynamic layouts
3. **Calm Professional** - Muted, organized designs focused on clarity
4. **Neumorphic** - Soft UI with extruded elements and monochromatic palettes
5. **Gamified Fun** - Playful designs with bright colors and reward elements
6. **Elegant Luxury** - Premium designs with dark themes and metallic accents
7. **Retro Nostalgic** - Pixelated, vintage-inspired designs
8. **Organic Hand-drawn** - Natural, sketchy designs with textured elements
9. **Futuristic Tech** - Advanced designs with glowing elements and gradients

### 3. Technical Integration
- Works with approved UI component libraries
- Ensures all styles are implementable with existing technology stack
- Maintains accessibility standards across all variations
- Provides CSS/styling specifications for each variation

## Configuration Files

### 1. Agent Definition
- **Location**: `/SPARC/claude-config/agents/11-visual-style-specialist.md`
- **Purpose**: Defines the agent's role, responsibilities, and workflow

### 2. MCP Configuration
- **Location**: `/SPARC/claude-config/mcp-config/visual-style-specialist-config.json`
- **Purpose**: Configures the MCP server integration and validation rules

### 3. MCP Server Script
- **Location**: `/SPARC/claude-config/scripts/visual-style-mcp.py`
- **Purpose**: Python implementation of the visual style generation logic

### 4. Example Configuration
- **Location**: `/SPARC/claude-config/agents/examples/visual-style-specialist-example.md`
- **Purpose**: Demonstrates usage with a task management app example

## Workflow Integration

The Visual Style Specialist is integrated into the SPARC workflow after the UX Designer:

```
product-manager → solution-architect → context7-enforcer → data-architect → 
api-developer → ux-designer → visual-style-specialist → planner → coder-tdd
```

## Input Requirements

1. **UX.md** - Base UI structure and component specifications
2. **PRD.md** - Product requirements and target audience
3. **technology-lock.json** - Approved technology stack
4. **Style requirements** - Specific visual styles requested
5. **/approved-docs/frontend/ui-library/** - Component library documentation

## Output Deliverables

### 1. Visual-Styles.md
Contains:
- Base UI structure definition
- Detailed specifications for each style variation
- Color palettes, typography, and effects for each style
- Component styling overrides
- Implementation guidelines

### 2. Style Guide Assets
- Grid layout showing all 9 variations
- Individual screen mockups for each style
- Component style specifications
- Accessibility compliance documentation

## Validation and Enforcement

### 1. Style Differentiation
- Minimum differentiation score: 85%
- Target differentiation score: 95%
- Validates visual distinction between styles

### 2. Consistency Validation
- Ensures all mandatory elements present in each variation
- Validates functional parity across styles
- Checks responsive behavior consistency

### 3. Technical Feasibility
- Verifies implementation compatibility with approved stack
- Validates CSS/styling methodology compliance
- Ensures component library compatibility

### 4. Accessibility Compliance
- WCAG AA color contrast requirements
- 44px minimum touch targets
- Focus indicator presence
- Screen reader compatibility

## Usage Example

```bash
# Input prompt to Visual Style Specialist
Create 9 visual style variations for a mobile task management app with:
- Home screen view
- Navigation bar (Tasks, Calendar, Projects, Profile)
- Add New Task CTA button
- Task list with 3-4 sample tasks
- Daily progress indicator
- Search bar

# The agent will generate:
1. Modern Minimal version
2. Bold Energetic version
3. Calm Professional version
... (6 more variations)
```

## Best Practices

1. **Maintain Functional Consistency**
   - All UI elements must work identically across styles
   - Navigation flow remains unchanged
   - Interactive elements maintain same behavior

2. **Ensure Clear Differentiation**
   - Each style should be immediately distinguishable
   - Avoid mixing style characteristics
   - Maintain style purity throughout each variation

3. **Consider Implementation**
   - All styles must be achievable with approved tools
   - Provide realistic CSS/styling specifications
   - Consider performance impact of visual effects

4. **Prioritize Accessibility**
   - Never sacrifice accessibility for aesthetics
   - Maintain readable contrast ratios
   - Ensure all styles work with assistive technologies

## Troubleshooting

### Common Issues

1. **Insufficient Style Differentiation**
   - Solution: Increase contrast between style characteristics
   - Check: Color palettes, typography choices, effect applications

2. **Implementation Incompatibility**
   - Solution: Verify against approved UI component library
   - Check: Component overrides match library API

3. **Accessibility Failures**
   - Solution: Adjust color contrasts, increase touch targets
   - Check: Run accessibility validation on each variation

## Future Enhancements

1. **Dynamic Style Generation**
   - AI-powered style creation based on brand guidelines
   - Automatic style mixing for hybrid approaches

2. **Real-time Preview**
   - Live rendering of style variations
   - Interactive style switching demonstrations

3. **Export Capabilities**
   - Direct export to design tools (Figma, Sketch)
   - Automatic theme file generation for frameworks