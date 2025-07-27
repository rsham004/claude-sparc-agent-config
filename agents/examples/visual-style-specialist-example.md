# Visual Style Specialist Example Configuration

## Example Project: Task Management Mobile App

### Input Prompt
```
Create 9 distinct visual style variations for a mobile task management application.

Application Context:
- Task management and productivity app
- Target audience: Professionals and students
- Key features: Task lists, calendar integration, project tracking

Core UI Elements (Required in all variations):
- Home screen view
- Navigation bar with 4 icons (Tasks, Calendar, Projects, Profile)
- Primary CTA button for "Add New Task"
- Task list showing 3-4 sample tasks
- Progress indicator showing daily completion
- Search bar at top

Visual Styles Required:
1. Modern Minimal
2. Bold Energetic 
3. Calm Professional
4. Neumorphic
5. Gamified Fun
6. Elegant Luxury
7. Retro Nostalgic
8. Organic Hand-drawn
9. Futuristic Tech
```

### Expected Output Structure

```markdown
# Task Management App - Visual Style Concepts

## Base Structure (Consistent Across All Styles)

### Screen Layout
```
┌─────────────────────────┐
│    [Search Bar]         │
├─────────────────────────┤
│ Today's Progress: 75%   │
├─────────────────────────┤
│ Tasks                   │
│ □ Review project docs   │
│ ✓ Team standup meeting  │
│ □ Update API endpoints  │
│ □ Client presentation   │
├─────────────────────────┤
│    [+ Add New Task]     │
├─────────────────────────┤
│ Tasks | Cal | Proj | Me │
└─────────────────────────┘
```

## Style Implementations

### 1. Modern Minimal
- **Background**: #FAFAFA
- **Primary**: #6366F1 (Soft indigo)
- **Text**: #1F2937
- **Cards**: White with 4px border-radius, subtle shadow
- **Navigation**: Floating tab bar with line indicators
- **CTA Button**: Rounded (24px), soft gradient
- **Typography**: Inter, 16px base, 1.5 line-height
- **Icons**: Outlined, 2px stroke weight
- **Progress**: Thin line with rounded ends

### 2. Bold Energetic
- **Background**: #0F172A
- **Primary**: #F97316 (Vibrant orange)
- **Accent**: #14B8A6 (Teal)
- **Cards**: Sharp corners, bold 4px colored borders
- **Navigation**: Fixed bottom, high contrast
- **CTA Button**: Rectangle, hard shadow offset
- **Typography**: Montserrat Bold, high contrast
- **Icons**: Filled, geometric shapes
- **Progress**: Thick bar with percentage overlay

### 3. Calm Professional
- **Background**: #F8FAFC
- **Primary**: #475569 (Slate)
- **Secondary**: #94A3B8
- **Cards**: 1px border, no shadow, 4px radius
- **Navigation**: Classic tab bar, subtle highlights
- **CTA Button**: Understated, thin border
- **Typography**: Roboto, regular weight
- **Icons**: Balanced, 1.5px stroke
- **Progress**: Segmented dots indicator

### 4. Neumorphic
- **Background**: #E0E5EC
- **Text**: #5A6B7B
- **Cards**: Extruded effect with dual shadows
- **Navigation**: Inset tabs with soft edges
- **CTA Button**: Pressed/raised states
- **Typography**: SF Pro Display
- **Icons**: Soft embossed effect
- **Progress**: Inset track with raised indicator

### 5. Gamified Fun
- **Background**: Linear gradient (#667EEA to #764BA2)
- **Primary**: #F687B3 (Pink)
- **Accent**: #48BB78 (Green for success)
- **Cards**: Bouncy animations, star decorations
- **Navigation**: Playful icons with badges
- **CTA Button**: Pulsing animation, coin icon
- **Typography**: Fredoka One, playful
- **Icons**: Cartoon style with expressions
- **Progress**: XP bar with level indicator

### 6. Elegant Luxury
- **Background**: #0A0A0A
- **Primary**: #D4AF37 (Gold)
- **Text**: #F5F5F5
- **Cards**: Minimal, gold accent line
- **Navigation**: Subtle, premium feel
- **CTA Button**: Gold outline, letter-spacing
- **Typography**: Playfair Display (headers), Lato (body)
- **Icons**: Thin line, elegant
- **Progress**: Discrete dots, gold active

### 7. Retro Nostalgic
- **Background**: #2A2A2A with scanlines
- **Primary**: #FF00FF (Magenta)
- **Secondary**: #00FFFF (Cyan)
- **Cards**: Pixel borders, 8-bit style
- **Navigation**: Retro game menu style
- **CTA Button**: Pixelated with "PUSH" text
- **Typography**: Press Start 2P
- **Icons**: 16x16 pixel art
- **Progress**: Classic loading bar

### 8. Organic Hand-drawn
- **Background**: Paper texture (#FFF8E7)
- **Primary**: #8B4513 (Brown ink)
- **Accent**: #228B22 (Forest green)
- **Cards**: Hand-drawn borders, sketch style
- **Navigation**: Doodle icons
- **CTA Button**: Circular, hand-lettered
- **Typography**: Kalam (handwritten)
- **Icons**: Sketched, imperfect lines
- **Progress**: Hand-drawn progress circle

### 9. Futuristic Tech
- **Background**: #0A0A0A with grid overlay
- **Primary**: #00D9FF (Cyan glow)
- **Accent**: #FF00AA (Neon pink)
- **Cards**: Holographic effect, sharp angles
- **Navigation**: HUD-style interface
- **CTA Button**: Glowing edges, scan animation
- **Typography**: Orbitron, tech display font
- **Icons**: Geometric, animated
- **Progress**: Circular tech meter with data
```

### Implementation Notes

1. **Component Library Mapping**
   - All styles use base components from approved UI library
   - Style variations applied through theming system
   - No custom components required

2. **Accessibility Maintained**
   - All color combinations meet WCAG AA standards
   - Focus states preserved across all styles
   - Semantic HTML structure unchanged

3. **Responsive Behavior**
   - Styles adapt to screen sizes while maintaining identity
   - Touch targets remain consistent (44px minimum)
   - Layout reflows preserve visual hierarchy

4. **Performance Considerations**
   - Styles use CSS variables for easy switching
   - No heavy animations that impact performance
   - Image assets optimized for each style theme
```