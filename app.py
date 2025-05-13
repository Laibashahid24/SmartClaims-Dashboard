import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("📊 SmartClaims Dashboard")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("insurance_claims.csv", parse_dates=["claim_date"])

df = load_data()

# Raw data display
if st.checkbox("Show raw data"):
    st.write(df.head(20))

# Metrics
st.subheader("Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Claims", len(df))
col2.metric("Average Claim ($)", f"{df['claim_amount'].mean():,.2f}")
col3.metric("Approval Rate", f"{(df['claim_status'] == 'Approved').mean()*100:.1f}%")

# Visualization: Claims by Region
st.subheader("Total Claim Amount by Region")
fig1 = px.bar(df.groupby("region")["claim_amount"].sum().reset_index(),
              x="region", y="claim_amount", title="Claim Amount by Region")
st.plotly_chart(fig1)

# Claim Type Filter
st.subheader("Claim Amounts by Incident Type")
incident = st.selectbox("Choose Incident Type:", df["incident_type"].unique())
filtered = df[df["incident_type"] == incident]
fig2 = px.box(filtered, x="policy_type", y="claim_amount", color="claim_status",
              title=f"Claim Distribution for {incident} Incidents")
st.plotly_chart(fig2)

# Time Trend
st.subheader("Monthly Claim Volume")
monthly = df.set_index("claim_date").resample("M")["claim_id"].count()
fig3 = px.line(monthly, title="Monthly Claim Volume")
st.plotly_chart(fig3)
