# 🏥 TriGuard

## AI-Powered Calibrated Risk Triage for Essential Medicine Supply Chains

TriGuard is an AI-powered decision support system developed for the **AI for Public Good – Sustainable & Resilient Supply Chains Hackathon** organized by **Manipal University Jaipur**.

Instead of only predicting whether a supply chain disruption may occur, TriGuard estimates a **calibrated disruption probability** and converts it into actionable operational recommendations for healthcare planners responsible for essential medicine distribution.

---

# Problem Statement

Healthcare supply chains frequently experience disruptions caused by supplier delays, transportation issues, weather events, inventory shortages, and sudden demand spikes.

For essential medicines, delayed intervention may directly impact patient care. Traditional prediction systems often produce probability scores that are difficult for planners to interpret and trust.

TriGuard addresses this challenge by combining machine learning with calibrated probability estimation and an operational triage engine.

---

# Key Features

✅ Predict disruption risk using Machine Learning

✅ Probability Calibration (Isotonic Calibration)

✅ Operational Decision Support

✅ Explainable AI Recommendations

✅ Essential Medicine Supply Chain Focus

✅ Interactive Streamlit Dashboard

✅ Human-in-the-loop Decision Making

---

# System Workflow

```
Historical Supply Chain Data
            │
            ▼
 Synthetic Data Generation
            │
            ▼
 Feature Engineering Pipeline
            │
            ▼
 Random Forest Classifier
            │
            ▼
 Probability Calibration
            │
            ▼
 Risk Probability
            │
            ▼
 Decision Intelligence Engine
            │
            ▼
Monitor → Review → Escalate → Intervene Now
            │
            ▼
 Streamlit Dashboard
```

---

# Technology Stack

| Component | Technology |
|------------|------------|
| Programming Language | Python |
| Machine Learning | Random Forest |
| Calibration | Isotonic Calibration |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Model Persistence | Joblib |
| Dashboard | Streamlit |
| Version Control | Git & GitHub |

---

# Project Structure

```
triguard-round2/

│
├── app/
│     app.py
│
├── data/
│     processed/
│
├── outputs/
│     models/
│     predictions/
│
├── src/
│     data_generation.py
│     train_model.py
│     predict.py
│     triage_logic.py
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

# Machine Learning Pipeline

1. Generate synthetic healthcare supply chain dataset

2. Preprocess categorical and numerical variables

3. Train Random Forest classifier

4. Calibrate prediction probabilities using Isotonic Calibration

5. Generate disruption probability

6. Convert probability into operational triage recommendations

7. Display results through Streamlit

---

# Model Performance

| Metric | Value |
|---------|--------|
| Accuracy | 70% |
| ROC-AUC | 0.73 |
| Calibration | Isotonic Regression |
| Prediction Type | Binary Classification |

---

# Operational Triage

| Risk Level | Recommendation |
|------------|----------------|
| Low | Monitor |
| Medium | Review |
| High | Escalate to Planner |
| Very High | Immediate Intervention |

---

# Future Improvements

- Real-time ERP integration
- Live supplier monitoring
- GIS-based disruption visualization
- Explainable AI using SHAP values
- Time-series forecasting integration
- Multi-state deployment

---

# Team

**Team Name:** ERROR 1238

**Member 1:** Somya Saini

**Member 2:** Vaanya Kumawat

---

# Hackathon

AI for Public Good – Sustainable & Resilient Supply Chains

Manipal University Jaipur