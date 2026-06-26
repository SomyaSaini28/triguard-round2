# TriGuard – Calibrated Risk Triage for Essential Medicine Supply Chains

## Team Details
- **Team Name:** ERROR 1238
- **Hackathon:** AI for Public Good – Sustainable & Resilient Supply Chains
- **Institution:** Manipal University Jaipur
- **Member 1:** Somya Saini
- **Member 2:** Vaanya Kumawat

---

## Problem Statement
Essential medicine supply chains are vulnerable to disruptions caused by supplier delays, low fill rates, route delays, demand spikes, weather risks, and stock shortages. In public health systems, such disruptions can lead to medicine stockouts at hospitals and primary care centers, directly affecting patient care.

The challenge is not only to detect risk, but to prioritize which supply chain cases require immediate intervention, escalation, review, or monitoring.

---

## Solution Overview
**TriGuard** is an AI-powered calibrated risk triage system for essential medicine supply chains.

It predicts the probability of supply disruption for a medicine shipment / replenishment case and then converts that risk into an operational triage action such as:

- **INTERVENE NOW**
- **ESCALATE TO PLANNER**
- **REVIEW**
- **MONITOR**

The system combines:
1. **Machine Learning risk prediction**
2. **Probability calibration**
3. **Operational triage rules**
4. **Interactive Streamlit prototype for case-level assessment**

---

## Key Features
- Predicts **disruption risk probability** for a supply chain case
- Uses **calibrated probabilities** for more reliable risk interpretation
- Converts model output into **actionable triage decisions**
- Includes a **Streamlit prototype** for interactive testing
- Designed for **essential medicine supply chain monitoring**

---

## AI Approach Used
TriGuard primarily uses:
- **Predictive Analytics / Classification**
- **Probability Calibration**
- **Rule-based Decision Support**

### Why this approach?
The problem is about **anticipating future disruptions** from structured supply chain features such as:
- supplier performance
- lead time
- route delays
- weather risk
- stock levels
- demand spikes

Therefore, a **predictive risk model** is appropriate.  
Since operational teams need interpretable and usable risk scores, we calibrate model probabilities and then map them to triage actions.

---

## Project Structure

```bash
triguard-round2/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│       └── supply_chain_cases.csv
│
├── docs/
│   └── round2_document_draft.txt
│
├── notebooks/
│
├── outputs/
│   ├── models/
│   │   └── triguard_calibrated_model.pkl
│   ├── predictions/
│   │   └── sample_predictions.csv
│   └── charts/
│
├── src/
│   ├── data_generation.py
│   ├── train_model.py
│   ├── predict.py
│   └── calibrate_model.py
│
├── README.md
└── requirements.txt