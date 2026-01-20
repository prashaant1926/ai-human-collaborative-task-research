# Experiment 1: Collaboration Structure Comparison

## Research Question

**Does dynamic role allocation between humans and AI produce higher quality research outputs and greater efficiency compared to static role allocation in literature review tasks?**

## Background & Motivation

Current AI research assistants typically implement fixed interaction patterns: either the AI generates and the human evaluates, or the human directs and the AI executes. This static approach may underutilize the complementary strengths of humans and AI across different phases of research tasks.

Prior work (Horvitz 1999, Amershi et al. 2019) suggests that adaptive sharing of control improves interaction quality, but this has not been validated for complex research collaboration tasks.

## Hypothesis

**Primary Hypothesis:** Dynamic role allocation will produce 20% higher quality research outputs (as measured by expert ratings) compared to static role allocation conditions.

**Secondary Hypotheses:**
- Dynamic allocation reduces time-to-completion by 15-25%
- Dynamic allocation reduces cognitive load (NASA-TLX scores) by at least 1 standard deviation
- Participants report higher satisfaction with dynamic allocation

## Experimental Design

### Variables

- **Independent Variable:** Collaboration structure
  - Static-AI-Lead: AI generates summaries and analyses, human reviews and approves
  - Static-Human-Lead: Human directs all actions, AI executes specific requests
  - Dynamic: Role shifts based on task phase, confidence levels, and participant preference

- **Dependent Variables:**
  - Output quality (expert rating, 1-5 scale across 5 dimensions)
  - Time to completion (minutes)
  - Cognitive load (NASA-TLX, 6 dimensions)
  - Collaboration satisfaction (custom 10-item scale)

- **Control Variables:**
  - Paper set difficulty (pre-balanced)
  - Time limit (90 minutes per condition)
  - AI model and parameters (fixed)
  - Task instructions (standardized)

- **Confounding Factors:**
  - Participant prior experience with AI tools
  - Topic familiarity
  - Learning effects across conditions

### Methodology

1. **Baseline Setup:**
   - Static-AI-Lead condition serves as primary baseline
   - AI initiates all actions, suggests structure, generates summaries
   - Human provides approval/rejection and final edits only

2. **Treatment Conditions:**
   - Static-Human-Lead: Human requests specific information, AI responds reactively
   - Dynamic: System suggests role transitions based on:
     - Task phase (exploration vs. synthesis vs. writing)
     - AI confidence levels (high confidence = AI leads)
     - User engagement signals (low engagement = prompt role switch)

3. **Data Collection:**
   - Automated interaction logging (timestamps, actions, content)
   - Pre/post surveys per condition
   - Final output artifact collection
   - Optional think-aloud during subset of sessions

4. **Sample Size:**
   - N = 30 participants
   - Within-subject design (all participants complete all conditions)
   - Counter-balanced order using Latin square
   - Power analysis: 80% power to detect medium effect (d=0.5) at α=0.05

## Evaluation Metrics

### Primary Metrics

- **Overall Quality Score:** Mean of 5 quality dimensions (1-5 scale)
  - Accuracy: Correctness of claims and citations
  - Completeness: Coverage of relevant papers and themes
  - Organization: Logical structure and flow
  - Insight: Depth of synthesis and novel connections
  - Writing: Clarity and readability

- **Time to Completion:** Minutes from task start to submission

### Secondary Metrics

- NASA-TLX subscales (mental demand, temporal demand, effort, frustration, performance, physical demand)
- Collaboration satisfaction (10-item custom scale)
- Interaction pattern metrics (role switches, turn length, initiative ratio)

### Statistical Tests

- **Primary:** Repeated-measures ANOVA for quality and time
- **Post-hoc:** Tukey HSD for pairwise condition comparisons
- **Secondary:** Repeated-measures MANOVA for NASA-TLX subscales
- **Significance Level:** α = 0.05
- **Effect Size:** Report η² (partial eta-squared)

## Implementation Milestones

### Phase 1: Setup (Week 1)
- [ ] Finalize 3 paper sets (15 papers each, different topics)
- [ ] Validate paper set difficulty equivalence with pilot
- [ ] Configure AI assistant for each condition
- [ ] Build experiment platform with logging
- [ ] Create survey instruments
- [ ] Submit IRB protocol

### Phase 2: Pilot Study (Week 2)
- [ ] Recruit 5 pilot participants
- [ ] Run full protocol with each
- [ ] Identify and fix issues
- [ ] Calibrate timing estimates
- [ ] Train expert raters

### Phase 3: Main Data Collection (Weeks 3-6)
- [ ] Recruit 30 participants
- [ ] Schedule sessions (allow 2-3 hours per participant)
- [ ] Run 7-8 participants per week
- [ ] Monitor data quality throughout
- [ ] Collect expert ratings

### Phase 4: Analysis (Week 7)
- [ ] Clean and validate data
- [ ] Run statistical analyses
- [ ] Generate visualizations
- [ ] Write results section

## Success Criteria

### Minimum Success
- 25+ participants complete all conditions
- Inter-rater reliability ICC > 0.70
- All conditions have sufficient interaction data

### Target Success
- Significant main effect of condition on quality (p < 0.05)
- Dynamic condition outperforms both static conditions
- Effect size η² > 0.06 (medium effect)

### Stretch Goals
- Effect size η² > 0.14 (large effect)
- Identify specific task phases where dynamic allocation helps most
- Develop predictive model of optimal role transitions

## Risk Mitigation

| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|---------------------|
| Insufficient participants | Medium | High | Over-recruit by 20%; offer competitive compensation |
| Low inter-rater reliability | Medium | High | Training session for raters; calibration on pilot outputs |
| Learning effects confound results | Medium | Medium | Counter-balanced design; include order as covariate |
| AI service disruption | Low | High | Backup session slots; local caching of responses |
| Participant dropout mid-study | Medium | Medium | Compensate proportionally; recruit extras |

## Resources Required

### Computational
- **Hardware:** Standard laptop/desktop sufficient
- **AI API:** GPT-4 or Claude API access
- **Estimated API Cost:** ~$500-1000 for all sessions
- **Storage:** ~5 GB for logs and outputs

### Data
- **Primary Dataset:** 3 curated paper sets from ACL Anthology
- **Paper Topics:** To be determined (different domains to avoid expertise effects)

### Human Resources
- 30 participants (graduate students, compensated $50)
- 3 expert raters (compensated $200 each)
- Research team time: ~100 hours total

### Dependencies
- Experiment platform (web-based, custom built)
- AI API integration
- Survey platform (Qualtrics or similar)
- Analysis tools (Python: pandas, scipy, statsmodels)

## Timeline

| Week | Task | Deliverable |
|------|------|-------------|
| 1 | Platform development, paper set curation | Working prototype |
| 2 | Pilot study, IRB approval | Validated protocol |
| 3-4 | Data collection phase 1 | 15 participants complete |
| 5-6 | Data collection phase 2 | 30 participants complete |
| 7 | Analysis and visualization | Results report |

## Notes

- Consider video recording sessions (with consent) for qualitative analysis
- May want exit interviews to understand participant experience
- Dynamic condition algorithm will need careful tuning in pilot
- Plan for exploratory analysis of interaction patterns
