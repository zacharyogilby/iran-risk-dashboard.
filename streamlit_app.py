
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Iran Conflict Risk Dashboard", layout="wide")

st.title("🇮🇷 Iran Conflict Risk Dashboard")
st.markdown("Live scenario tracker based on evolving regional developments")

# Initial scenario probabilities
scenarios = {
    "Cold containment / hybrid war": 60,
    "Wider conventional war": 28,
    "Nuclear breakout": 11,
    "Regime change / shift": 6,
    "Return to diplomacy": 5
}

st.sidebar.header("⚠️ Event Triggers")

# Event toggles
proxy_strikes = st.sidebar.slider("Hezbollah/Proxy Strike Intensity", 0, 10, 2)
direct_missile_attack = st.sidebar.checkbox("Iran fires ballistic missile at U.S./Israel")
un_restraint = st.sidebar.checkbox("UN passes ceasefire resolution")
nuclear_activity = st.sidebar.checkbox("IAEA reports resumed enrichment")
internal_unrest = st.sidebar.checkbox("Mass protests in Tehran")

# Adjust probabilities based on toggles
if proxy_strikes > 5:
    scenarios["Wider conventional war"] += 5
    scenarios["Cold containment / hybrid war"] -= 3

if direct_missile_attack:
    scenarios["Wider conventional war"] += 10
    scenarios["Return to diplomacy"] -= 2

if un_restraint:
    scenarios["Return to diplomacy"] += 5
    scenarios["Wider conventional war"] -= 2

if nuclear_activity:
    scenarios["Nuclear breakout"] += 8
    scenarios["Cold containment / hybrid war"] -= 3

if internal_unrest:
    scenarios["Regime change / shift"] += 6

# Normalize values to total 100%
total = sum(scenarios.values())
for key in scenarios:
    scenarios[key] = round((scenarios[key] / total) * 100, 2)

# Display results
st.subheader("📊 Current Risk Profile")
labels = list(scenarios.keys())
values = list(scenarios.values())

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(labels, values)
ax.set_xlim(0, 100)
ax.invert_yaxis()
ax.set_xlabel("Probability (%)")
ax.set_title("Iran Conflict Scenario Forecast")
st.pyplot(fig)

st.markdown("---")
st.markdown("Built by ChatGPT for live risk tracking. Adjust the triggers on the left to model new developments.")
