# Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance

**Authors**: Bansal, G., Nushi, B., Kamar, E., Weld, D. S., Lasecki, W. S., & Horvitz, E.
**Venue**: HCOMP 2019
**Citation**: Bansal et al. (2019)

## Problem

Does AI accuracy alone determine human-AI team performance, or do human factors like mental models play a significant role?

## Assumption in Prior Work

Improving AI accuracy is the primary lever for improving human-AI team performance. Human understanding of AI was considered secondary.

## Key Insight

Humans' mental models of AI capabilities are as important as actual AI accuracy for team performance. Accurate mental models enable appropriate reliance on AI.

## Technical Overview

### Experimental Design
- Task: Image classification with AI assistance
- Manipulation: AI accuracy level AND transparency of AI limitations
- Measures: Team accuracy, reliance patterns, calibration

### Key Findings

1. **Mental model accuracy matters**: Users with accurate mental models of AI limitations made better decisions about when to follow AI recommendations

2. **Overreliance when mental models poor**: Users who didn't understand AI limitations over-relied on AI even when it was wrong

3. **Complementary performance**: Best team performance when users understood both AI strengths AND weaknesses

4. **Transparency helps**: Showing AI confidence and explaining limitations improved mental model accuracy

## Validation

- Controlled experiments with 300+ participants
- Multiple AI accuracy conditions
- Quantitative measures of reliance and performance

## Impact & Relevance to Our Work

**For our research:**
- Supports need for transparency about AI capabilities in each role
- Dynamic role allocation should include signals about AI confidence
- Accumulated context may help build more accurate mental models over time

**Gap we address:**
- Study focused on single-session classification tasks
- We extend to complex, multi-session research collaboration
- We examine how mental models develop over extended interaction
