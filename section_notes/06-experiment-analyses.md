# Experiment Analyses

## Analysis Plan

This document outlines the statistical analyses to be performed on experiment data.

---

## Experiment 1: Collaboration Structure Comparison

### Primary Analysis: Condition Effects on Quality

**Hypothesis**: Dynamic role allocation produces higher quality outputs than static allocation.

**Statistical Test**: Repeated-measures ANOVA
- **IV**: Condition (static_ai_lead, static_human_lead, dynamic)
- **DV**: Overall quality score (1-5)
- **Within-subject factor**: Participant

**Post-hoc Tests**: Tukey HSD for pairwise comparisons

**Expected Results Format**:
```
Condition         Mean (SD)    95% CI
-----------------------------------------
Static AI Lead    3.2 (0.8)    [2.9, 3.5]
Static Human Lead 3.4 (0.7)    [3.1, 3.7]
Dynamic           3.9 (0.6)    [3.6, 4.2]

F(2, 58) = X.XX, p = .XXX, eta-squared = .XX
```

### Secondary Analysis: Efficiency

**Hypothesis**: Dynamic allocation reduces time to completion.

**Statistical Test**: Repeated-measures ANOVA
- **DV**: Time to completion (minutes)

### Secondary Analysis: Cognitive Load

**Hypothesis**: Dynamic allocation reduces cognitive load.

**Statistical Test**: Repeated-measures MANOVA
- **DVs**: NASA-TLX subscales (6 dimensions)

### Exploratory Analyses

1. **Interaction patterns**: Sequence analysis of action types
2. **Role transition frequency**: Count and timing of role changes
3. **Quality dimension breakdown**: Which dimensions benefit most from dynamic allocation

---

## Experiment 3: Knowledge Accumulation

### Primary Analysis: Learning Curves

**Hypothesis**: Accumulated context accelerates performance improvement.

**Statistical Test**: Mixed-effects linear model
- **Fixed effects**: Session (1-5), Condition (fresh, accumulated), Session x Condition
- **Random effects**: Participant (intercept and slope)

**Model Specification**:
```
performance ~ session * condition + (1 + session | participant)
```

### Secondary Analysis: Trust Development

**Hypothesis**: Trust increases more rapidly with accumulated context.

**Statistical Test**: Same mixed-effects structure
- **DV**: Trust in Automation Scale score

---

## Inter-Rater Reliability

For quality ratings:
- **Metric**: Intraclass Correlation Coefficient (ICC)
- **Target**: ICC > 0.70 (good agreement)
- **If low**: Rater calibration session, resolve discrepancies

---

## Planned Visualizations

### Figure 1: Quality by Condition
- Box plots with individual data points
- Significance brackets for pairwise comparisons

### Figure 2: Time by Condition
- Bar chart with error bars (95% CI)

### Figure 3: NASA-TLX Profile
- Radar chart showing 6 dimensions across conditions

### Figure 4: Learning Curves
- Line plot: Session (x) vs. Performance (y)
- Separate lines for Fresh vs. Accumulated conditions
- Shaded error bands

### Figure 5: Interaction Patterns
- Sankey diagram showing action type sequences
- Separate diagrams for each condition

---

## Results Template

### Experiment 1 Results

#### Quality Scores

| Metric | Static AI | Static Human | Dynamic | F | p | eta-sq |
|--------|-----------|--------------|---------|---|---|--------|
| Overall | - | - | - | - | - | - |
| Accuracy | - | - | - | - | - | - |
| Completeness | - | - | - | - | - | - |
| Organization | - | - | - | - | - | - |
| Insight | - | - | - | - | - | - |

#### Pairwise Comparisons

| Comparison | Difference | 95% CI | p (adjusted) |
|------------|------------|--------|--------------|
| Dynamic vs Static AI | - | - | - |
| Dynamic vs Static Human | - | - | - |
| Static Human vs Static AI | - | - | - |

---

## Analysis Code Location

All analysis scripts will be stored in:
- `experiments/exp1_structure/analysis/`
- `experiments/exp3_accumulation/analysis/`

### Required Libraries
- Python: pandas, scipy, statsmodels, pingouin, matplotlib, seaborn
- R (alternative): lme4, emmeans, ggplot2

---

## Interpretation Guidelines

### Effect Size Benchmarks (eta-squared)
- Small: 0.01
- Medium: 0.06
- Large: 0.14

### Practical Significance
Even if statistically significant, consider:
- Is the effect size meaningful for practitioners?
- Does it justify implementation complexity?
- Are there cost/benefit tradeoffs?

---

## Contingency Plans

### If no significant main effect:
1. Examine individual differences (moderators)
2. Analyze interaction patterns qualitatively
3. Report as null result with power analysis

### If unexpected patterns emerge:
1. Document exploratory findings separately
2. Generate new hypotheses for follow-up
3. Do not p-hack or HARKing
