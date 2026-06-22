import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Engineering College Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("engg_colleges.csv")
df = load_data()

# Title
st.title("🎓 Engineering College Dashboard")
st.markdown("Analyze engineering colleges, branches, fees, placements, and rankings.")

# Sidebar Filters
st.sidebar.header("Filters")

selected_branch = st.sidebar.multiselect(
    "Select Branch",
    options=df["Branch"].unique(),
    default=df["Branch"].unique()
)

selected_city = st.sidebar.multiselect(
    "Select City",
    options=df["City"].unique(),
    default=df["City"].unique()
)

filtered_df = df[
    (df["Branch"].isin(selected_branch)) &
    (df["City"].isin(selected_city))
]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Colleges", filtered_df["College Name"].nunique())
col2.metric("Average Fees", f"₹{int(filtered_df['Fees'].mean()):,}")
col3.metric("Average Placement %", f"{filtered_df['Placement %'].mean():.1f}%")
col4.metric("Highest Package", f"₹{filtered_df['Highest Package'].max()} LPA")

st.divider()

# Placement Analysis
col1, col2 = st.columns(2)

with col1:
    fig = px.bar(
        filtered_df,
        x="College Name",
        y="Placement %",
        color="Placement %",
        title="Placement Percentage by College"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(
        filtered_df,
        x="College Name",
        y="Highest Package",
        color="Highest Package",
        title="Highest Package Offered"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Branch Distribution
col1, col2 = st.columns(2)

with col1:
    fig = px.pie(
        filtered_df,
        names="Branch",
        title="Branch Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.scatter(
        filtered_df,
        x="Fees",
        y="Placement %",
        size="Highest Package",
        color="Branch",
        hover_name="College Name",
        title="Fees vs Placement %"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# Ranking Chart
fig = px.bar(
    filtered_df.sort_values("Rank"),
    x="College Name",
    y="Rank",
    color="City",
    title="College Ranking"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# Data Table
st.subheader("College Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# Download Option
csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Data",
    data=csv,
    file_name="filtered_college_data.csv",
    mime="text/csv"
)
