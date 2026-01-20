# Experiment 3: Knowledge Accumulation Over Time

## Research Question

**How does accumulated context across multiple sessions affect human-AI collaboration effectiveness in research tasks?**

## Background & Motivation

Most AI assistants start each interaction fresh, losing valuable context from previous sessions. Transactive memory theory (Wegner 1987) suggests that effective teams develop shared understanding of "who knows what." We hypothesize that AI systems that retain session context can develop similar shared understanding with human collaborators.

Experiment 1 examines role allocation within sessions; this experiment examines how collaboration evolves across sessions.

## Hypothesis

**Primary Hypothesis:** Participants in the accumulated context condition will complete tasks 30% faster by session 5 compared to fresh context condition, due to reduced coordination overhead and established working patterns.

**Secondary Hypotheses:**
- Trust (measured by Trust in Automation Scale) increases more rapidly with accumulated context
- Quality improvements across sessions are steeper with accumulated context
- Participants develop more efficient communication patterns with accumulated context

## Experimental Design

### Variables

- **Independent Variables:**
  - Context condition (between-subjects): Fresh vs. Accumulated
  - Session number (within-subjects): 1, 2, 3, 4, 5

- **Dependent Variables:**
  - Task completion time (minutes)
  - Output quality (expert rating)
  - Trust in Automation Scale score
  - Interaction efficiency (words per task unit)
  - Satisfaction rating

- **Control Variables:**
  - Task difficulty (equivalent across sessions)
  - Session spacing (2-3 days between)
  - AI model and base capabilities

### Conditions

1. **Fresh Context:** Each session begins with no memory of previous sessions. AI acts as if meeting participant for first time.

2. **Accumulated Context:** AI retains:
   - Summary of previous session tasks and outcomes
   - Participant's expressed preferences and working style
   - Established terminology and conventions
   - Previous successful interaction patterns

### Methodology

1. **Session Structure:**
   - Each session: 60-minute research task
   - Tasks: Literature synthesis on related sub-topics
   - Sessions spaced 2-3 days apart

2. **Task Design:**
   - Session 1: Explore topic area, identify key themes
   - Session 2: Deep dive on theme A
   - Session 3: Deep dive on theme B
   - Session 4: Synthesize themes A and B
   - Session 5: Draft research summary

3. **Context Accumulation (for accumulated condition):**
   - End of each session: AI generates session summary
   - Start of next session: AI receives previous summaries
   - AI can reference past decisions and patterns

4. **Sample Size:**
   - N = 20 participants (10 per condition)
   - Between-subjects for condition
   - Power: 80% to detect session × condition interaction

## Evaluation Metrics

### Primary Metric
- **Task Completion Time:** Minutes to complete standardized task milestones

### Secondary Metrics
- **Quality Score:** Expert rating of session output (1-5)
- **Trust Scale:** Jian et al. Trust in Automation Scale (12 items)
- **Interaction Efficiency:** Total words exchanged per quality point
- **Pattern Establishment:** Coded instances of reference to established conventions

### Statistical Analysis

**Primary Analysis:** Mixed-effects linear model
```
completion_time ~ session * condition + (1 + session | participant)
```

**Secondary Analyses:**
- Same model structure for quality, trust
- Mediation analysis: Does trust mediate efficiency gains?
- Qualitative coding of accumulated context usage

## Implementation Milestones

### Phase 1: Preparation (Week 1)
- [ ] Design 5-session task sequence
- [ ] Build context accumulation system
- [ ] Create session summary templates
- [ ] Validate task difficulty equivalence

### Phase 2: Recruitment (Week 2)
- [ ] Recruit 20 participants
- [ ] Schedule all 5 sessions per participant
- [ ] Random assignment to conditions
- [ ] Participant briefing

### Phase 3: Data Collection (Weeks 3-5)
- [ ] Run sessions according to schedule
- [ ] Monitor completion and dropout
- [ ] Collect post-session surveys
- [ ] Quality check context accumulation

### Phase 4: Analysis (Week 6)
- [ ] Run mixed-effects models
- [ ] Generate learning curve visualizations
- [ ] Conduct post-hoc interviews (subset)
- [ ] Write up findings

## Success Criteria

### Minimum Success
- 16+ participants complete all 5 sessions
- Clear learning curve in both conditions
- Reliable measurement of all DVs

### Target Success
- Significant session × condition interaction (p < 0.05)
- Accumulated condition shows 30% greater improvement by session 5
- Trust increases faster in accumulated condition

### Stretch Goals
- Identify specific mechanisms of accumulated context benefit
- Develop design guidelines for context persistence
- Quantify optimal context summarization approach

## Risk Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Participant dropout across sessions | High | High | Over-recruit; incentivize completion bonus |
| Context accumulation failure | Medium | High | Robust summarization; manual backup |
| Session scheduling conflicts | Medium | Medium | Flexible scheduling windows |
| Task difficulty variation | Medium | Medium | Pilot test; adjust as needed |

## Resources Required

### Computational
- AI API with custom system prompts
- Context storage system
- Session scheduling platform

### Human Resources
- 20 participants × 5 sessions × 60 min = 100 participant-hours
- Compensation: $30/session + $50 completion bonus = $200/participant total
- Total participant compensation: $4,000
- Expert raters for quality assessment

### Data Management
- Secure storage for session transcripts
- Anonymization of participant data
- Context summary database

## Timeline

| Week | Task | Deliverable |
|------|------|-------------|
| 1 | Task design, system build | Protocol ready |
| 2 | Recruitment, scheduling | 20 participants enrolled |
| 3 | Sessions 1-2 for all participants | Session data |
| 4 | Sessions 3-4 for all participants | Session data |
| 5 | Session 5, wrap-up interviews | Complete dataset |
| 6 | Analysis | Results report |

## Dependencies

- **Requires Experiment 1 completion:** Findings from Exp 1 inform task design and AI configuration
- **Platform:** Can reuse Exp 1 platform with context module added

## Notes

- Consider exit interviews to understand subjective experience
- May want to analyze actual context usage (how often AI references past)
- Potential confound: Task familiarity vs. collaboration familiarity
- Could extend to 10 sessions for longer-term dynamics if resources permit
