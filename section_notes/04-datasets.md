# Datasets

## Primary Dataset: Collaboration Interaction Logs

### Description
Timestamped logs of human-AI interactions during research collaboration tasks.

### Schema
```json
{
  "session_id": "string",
  "participant_id": "string",
  "condition": "static_ai_lead | static_human_lead | dynamic",
  "timestamp": "ISO8601",
  "actor": "human | ai",
  "action_type": "query | response | edit | feedback | role_change",
  "content": "string",
  "metadata": {
    "confidence": "float (0-1)",
    "task_phase": "exploration | synthesis | writing | review",
    "role_at_time": "leader | supporter | equal"
  }
}
```

### Expected Size
- 30 participants x 3 conditions x ~200 interactions = ~18,000 interaction records
- Estimated storage: ~50 MB

### Collection Method
- Automated logging during experiment platform use
- Manual annotation for role changes and task phases

---

## Secondary Dataset: Task Output Quality Ratings

### Description
Expert ratings of research outputs produced during experiments.

### Schema
```json
{
  "output_id": "string",
  "session_id": "string",
  "rater_id": "string",
  "quality_dimensions": {
    "accuracy": "int (1-5)",
    "completeness": "int (1-5)",
    "organization": "int (1-5)",
    "insight_depth": "int (1-5)",
    "writing_quality": "int (1-5)"
  },
  "overall_score": "int (1-5)",
  "comments": "string"
}
```

### Expected Size
- 90 outputs x 3 raters = 270 rating records
- Estimated storage: ~1 MB

---

## Tertiary Dataset: Participant Surveys

### Description
Pre/post surveys measuring cognitive load, satisfaction, and trust.

### Instruments
1. **NASA-TLX**: Cognitive load (6 dimensions)
2. **Trust in Automation Scale**: AI trust (12 items)
3. **Collaboration Satisfaction Survey**: Custom (10 items)
4. **Demographics**: Background questionnaire

### Schema
```json
{
  "participant_id": "string",
  "session_id": "string",
  "survey_type": "pre | post",
  "nasa_tlx": {
    "mental_demand": "int (1-21)",
    "physical_demand": "int (1-21)",
    "temporal_demand": "int (1-21)",
    "performance": "int (1-21)",
    "effort": "int (1-21)",
    "frustration": "int (1-21)"
  },
  "trust_scores": "array[int]",
  "satisfaction_scores": "array[int]",
  "open_responses": "array[string]"
}
```

---

## External Datasets for Benchmarking

### ACL Anthology
- **Purpose**: Source papers for literature review tasks
- **URL**: https://aclanthology.org/
- **Usage**: Select 15-paper sets on specific topics

### Semantic Scholar API
- **Purpose**: Paper metadata and citation networks
- **URL**: https://api.semanticscholar.org/
- **Usage**: Validate coverage metrics

---

## Data Management Plan

### Storage
- Primary storage: Encrypted local server
- Backup: Institutional cloud storage
- Version control: Git LFS for large files

### Privacy
- All participant data pseudonymized
- Consent forms collected before participation
- Data retention: 5 years post-publication

### Access
- Raw data: Research team only
- Anonymized data: Available upon request after publication
- Aggregated results: Publicly available

### Ethics
- IRB approval required before data collection
- Participants can withdraw data within 30 days
- No personally identifiable information in published datasets
