# Experiment Runs

## Overview

This document tracks the execution of experiments defined in `03-experiment-ideas.md`.

---

## Pilot Study: Protocol Validation

### Status: PLANNED

### Objective
Validate experimental protocol before full study.

### Plan
- **Participants**: 5 graduate students (not in main study pool)
- **Duration**: 1 week
- **Focus**:
  - Task clarity and timing
  - Platform usability
  - Data collection pipeline

### Checklist
- [ ] Recruit pilot participants
- [ ] Set up experiment platform
- [ ] Configure logging system
- [ ] Prepare task materials (paper sets)
- [ ] Create condition randomization schedule
- [ ] Test survey instruments
- [ ] Dry run with research assistant

---

## Experiment 1: Collaboration Structure Comparison

### Status: NOT STARTED

### Pre-requisites
- [ ] IRB approval obtained
- [ ] Pilot study completed
- [ ] Platform finalized
- [ ] Participant recruitment complete

### Execution Plan

#### Phase 1: Setup (Week 1)
- [ ] Finalize paper sets for 3 topics
- [ ] Configure AI assistant for each condition
- [ ] Set up logging infrastructure
- [ ] Test full pipeline end-to-end

#### Phase 2: Data Collection (Weeks 2-5)
- [ ] Schedule participant sessions
- [ ] Run sessions (10 per week)
- [ ] Monitor data quality
- [ ] Address any issues

#### Phase 3: Rating Collection (Week 6)
- [ ] Recruit expert raters (n=3)
- [ ] Blind outputs for rating
- [ ] Collect quality ratings
- [ ] Calculate inter-rater reliability

### Session Log Template

| Session ID | Participant | Condition | Date | Duration | Notes |
|------------|-------------|-----------|------|----------|-------|
| S001 | P001 | dynamic | - | - | - |
| S002 | P001 | static_ai | - | - | - |
| S003 | P001 | static_human | - | - | - |

---

## Experiment 3: Knowledge Accumulation Study

### Status: NOT STARTED

### Pre-requisites
- [ ] Experiment 1 completed (informs design)
- [ ] Longitudinal platform features implemented
- [ ] Session memory system configured

### Execution Plan

#### Phase 1: Participant Recruitment (Week 1)
- [ ] Recruit 20 participants for 5-session commitment
- [ ] Schedule all sessions in advance

#### Phase 2: Data Collection (Weeks 2-4)
- [ ] Run Session 1 for all participants
- [ ] 2-3 day gap
- [ ] Run Session 2 for all participants
- [ ] Continue pattern through Session 5

#### Phase 3: Analysis (Week 5)
- [ ] Analyze performance trajectories
- [ ] Compare conditions
- [ ] Conduct follow-up interviews

---

## Run Notes

### Technical Setup

**Platform Requirements:**
- Web-based experiment interface
- Real-time interaction logging
- AI assistant integration (API-based)
- Survey delivery system

**AI Configuration:**
- Model: To be determined based on capability needs
- Temperature: 0.7 for generation, 0.3 for analysis
- Context window: Full session history

**Logging Format:**
```
[timestamp] [session_id] [actor] [action_type] content
```

### Known Issues & Solutions

| Issue | Solution | Status |
|-------|----------|--------|
| Session timeout | Auto-save every 30 seconds | Planned |
| AI latency | Loading indicators, async processing | Planned |
| Browser compatibility | Test on Chrome, Firefox, Safari | Planned |

---

## Data Quality Checks

After each session:
- [ ] Verify all interactions logged
- [ ] Check survey completion
- [ ] Validate timestamps
- [ ] Backup session data
- [ ] Note any anomalies
