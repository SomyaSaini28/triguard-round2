import streamlit as st
import sys
import os

# Add src folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from predict import predict_single_case

# --------------------------
# PAGE CONFIG
# --------------------------
st.set_page_config(
    page_title="TriGuard",
    page_icon="🏥",
    layout="wide"
)

# --------------------------
# CUSTOM CSS
# --------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.block-container {
    padding-top: 2rem;
}

.metric-box {
    background-color: #f5f8ff;
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #dce8ff;
}

.footer {
    text-align:center;
    color:gray;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# SIDEBAR
# --------------------------

st.sidebar.title("🏥 TriGuard")

st.sidebar.success("AI for Public Good Hackathon")

st.sidebar.markdown("""
### Team

**ERROR 1238**

**Members**

- Somya Saini
- Vaanya Kumawat

---

### AI Components

✅ Predictive Analytics

✅ Probability Calibration

✅ Decision Support

---

### Problem Statement

**PS2 – Calibrated Uncertainty Quantification for Supply Chain Risk Triage**
""")

# --------------------------
# HEADER
# --------------------------

st.markdown("""
# 🏥 TriGuard

### AI-Powered Calibrated Risk Triage for Essential Medicine Supply Chains

Predict disruption risk before medicine stockouts occur and recommend operational actions for planners.
""")

st.divider()

# --------------------------
# INPUT
# --------------------------

st.header("📦 Supply Chain Case Details")

col1, col2, col3 = st.columns(3)

with col1:

    medicine_name = st.selectbox(
        "Medicine Name",
        [
            "Insulin",
            "Amoxicillin",
            "Ceftriaxone",
            "ORS",
            "Oxytocin",
            "Rabies Vaccine",
            "Pentavalent Vaccine",
            "Paracetamol Injection",
            "Salbutamol",
            "Iron Folic Acid",
            "Anti-snake Venom",
            "Adrenaline Injection"
        ]
    )

    medicine_criticality = st.slider(
        "Medicine Criticality",
        1,
        5,
        4
    )

    cold_chain_required = st.selectbox(
        "Cold Chain Required",
        [0,1]
    )

    supplier_id = st.selectbox(
        "Supplier ID",
        [f"S{i}" for i in range(1,11)]
    )

    destination_facility = st.selectbox(
        "Destination Facility",
        [
            "District Hospital Jaipur",
            "District Hospital Ajmer",
            "District Hospital Jodhpur",
            "CHC Bikaner",
            "CHC Udaipur",
            "PHC Sikar",
            "PHC Alwar",
            "Medical College Kota"
        ]
    )

with col2:

    supplier_on_time_rate = st.slider(
        "Supplier On-Time Rate",
        0.40,
        0.99,
        0.80
    )

    supplier_fill_rate = st.slider(
        "Supplier Fill Rate",
        0.50,
        1.00,
        0.85
    )

    lead_time_days = st.slider(
        "Lead Time (Days)",
        2,
        12,
        6
    )

    lead_time_variability = st.slider(
        "Lead Time Variability",
        0.0,
        8.0,
        2.5
    )

    route_delay_days = st.slider(
        "Route Delay (Days)",
        0.0,
        10.0,
        1.5
    )

with col3:

    weather_risk_score = st.slider(
        "Weather Risk Score",
        0,
        10,
        4
    )

    demand_spike_factor = st.slider(
        "Demand Spike Factor",
        0.5,
        2.5,
        1.0
    )

    current_stock_days = st.slider(
        "Current Stock Days",
        1,
        25,
        8
    )

    warehouse_utilization = st.slider(
        "Warehouse Utilization (%)",
        50,
        100,
        75
    )

    safety_stock_gap = st.slider(
        "Safety Stock Gap",
        0,
        8,
        2
    )

st.divider()

# --------------------------
# BUTTON
# --------------------------

if st.button("🚀 Assess Risk", use_container_width=True):

    case_dict = {
        "medicine_name": medicine_name,
        "medicine_criticality": medicine_criticality,
        "cold_chain_required": cold_chain_required,
        "supplier_id": supplier_id,
        "destination_facility": destination_facility,
        "supplier_on_time_rate": supplier_on_time_rate,
        "supplier_fill_rate": supplier_fill_rate,
        "lead_time_days": lead_time_days,
        "lead_time_variability": lead_time_variability,
        "route_delay_days": route_delay_days,
        "weather_risk_score": weather_risk_score,
        "demand_spike_factor": demand_spike_factor,
        "current_stock_days": current_stock_days,
        "warehouse_utilization": warehouse_utilization,
        "safety_stock_gap": safety_stock_gap
    }

    result = predict_single_case(case_dict)

    risk = result["risk_probability"]

    triage = result["triage_action"]

    st.header("📊 Risk Assessment")

    st.progress(float(risk))

    st.write(f"## Risk Probability: {risk*100:.1f}%")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Prediction",
        "Disruption" if result["predicted_label"] else "No Disruption"
    )

    c2.metric(
        "Risk Score",
        f"{risk*100:.1f}%"
    )

    c3.metric(
        "Triage",
        triage
    )

    st.divider()

    if risk >= 0.75:

        st.error("🔴 CRITICAL RISK — Immediate intervention required.")

    elif risk >= 0.60:

        st.warning("🟠 HIGH RISK — Escalate to supply planner.")

    elif risk >= 0.35:

        st.info("🟡 MODERATE RISK — Review during planning cycle.")

    else:

        st.success("🟢 LOW RISK — Continue monitoring.")

    st.subheader("🤖 AI Explanation")

    st.write(
        "The model identified the following factors contributing to the predicted disruption risk:"
    )

    reasons = []

    if supplier_on_time_rate < 0.75:
        reasons.append("• Supplier on-time performance is low.")

    if supplier_fill_rate < 0.80:
        reasons.append("• Supplier fill rate is below expected level.")

    if current_stock_days < 5:
        reasons.append("• Current stock is critically low.")

    if weather_risk_score > 6:
        reasons.append("• Weather risk is elevated.")

    if demand_spike_factor > 1.3:
        reasons.append("• Demand spike is significant.")

    if route_delay_days > 3:
        reasons.append("• Route delays are high.")

    if cold_chain_required == 1 and route_delay_days > 2:
        reasons.append("• Cold-chain shipment may be affected by delays.")

    if len(reasons)==0:
        reasons.append("• No major operational red flags detected.")

    for r in reasons:
        st.write(r)

    st.subheader("📋 Recommended Operational Response")

    if triage=="INTERVENE NOW":

        st.error("""
Immediately intervene.

• Expedite shipment

• Contact supplier

• Trigger emergency replenishment

• Notify district planner
""")

    elif triage=="ESCALATE TO PLANNER":

        st.warning("""
Escalate this case.

• Review inventory

• Monitor supplier

• Consider alternate transportation
""")

    elif triage=="REVIEW":

        st.info("""
Review this shipment during planning cycle.

• Continue monitoring

• Verify inventory status
""")

    else:

        st.success("""
No immediate action required.

Continue monitoring routinely.
""")

st.divider()

st.markdown(
"""
<div class="footer">
TriGuard • AI for Public Good – Sustainable & Resilient Supply Chains<br>
Team ERROR 1238
</div>
""",
unsafe_allow_html=True
)