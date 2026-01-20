# Guidelines for Human-AI Interaction

**Authors**: Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P., ... & Horvitz, E.
**Venue**: CHI 2019
**Citation**: Amershi et al. (2019)

## Problem

How should AI-powered systems be designed to support effective human-AI interaction?

## Assumption in Prior Work

Prior work provided fragmented, product-specific design advice without systematic principles applicable across AI systems.

## Key Insight

Human-AI interaction can be systematized into 18 design guidelines organized across four temporal phases of interaction.

## Technical Overview

### The 18 Guidelines (grouped by phase):

**Initially (before interaction)**
1. Make clear what the system can do
2. Make clear how well the system can do what it can do

**During interaction**
3. Time services based on context
4. Show contextually relevant information
5. Match relevant social norms
6. Mitigate social biases
7. Support efficient invocation
8. Support efficient dismissal
9. Support efficient correction
10. Scope services when in doubt
11. Make clear why the system did what it did

**When wrong**
12. Support efficient dismissal
13. Support efficient correction
14. Scope services when in doubt
15. Make clear why the system did what it did

**Over time**
16. Remember recent interactions
17. Learn from user behavior
18. Update and adapt cautiously
19. Encourage granular feedback
20. Convey the consequences of user actions
21. Provide global controls
22. Notify users about changes

## Validation

- Analyzed 150+ AI products
- Validated guidelines with design practitioners
- Showed guidelines improve design quality in user studies

## Impact & Relevance to Our Work

**For our research:**
- Guidelines 16-17 (remember interactions, learn from behavior) directly support our hypothesis about accumulated context
- Guidelines 3-4 (timing, contextual information) inform dynamic role allocation design
- We extend these general guidelines to research-specific collaboration tasks

**Gap we address:**
- Guidelines are general-purpose; we provide research-task-specific design principles
- Guidelines focus on AI as tool; we examine AI as collaborative partner
