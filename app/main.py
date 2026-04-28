import streamlit as st
import pandas as pd

st.title("🌍 Climate Dashboard - Africa")

# Load data
@st.cache_data
def load_data():
    ethiopia = pd.read_csv("ethiopia.csv")
    nigeria = pd.read_csv("nigeria.csv")
    kenya = pd.read_csv("kenya.csv")
    tanzania = pd.read_csv("tanzania.csv")
    sudan = pd.read_csv("sudan.csv")

    ethiopia["Country"] = "Ethiopia"
    nigeria["Country"] = "Nigeria"
    kenya["Country"] = "Kenya"
    tanzania["Country"] = "Tanzania"
    sudan["Country"] = "Sudan"

    df = pd.concat([ethiopia, nigeria, kenya, tanzania, sudan])

    df["Date"] = pd.to_datetime(df["YEAR"] * 1000 + df["DOY"], format="%Y%j")
    df["Year"] = df["Date"].dt.year

    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["Year"].min()),
    int(df["Year"].max()),
    (2015, 2026)
)

# Filter data
filtered_df = df[
    (df["Country"].isin(countries)) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

# -------------------------------
# 📈 Temperature Trend
# -------------------------------
st.subheader("🌡 Temperature Trend (T2M)")

temp_trend = filtered_df.groupby(["Year", "Country"])["T2M"].mean().unstack()

st.line_chart(temp_trend)

# -------------------------------
# 🌧 Precipitation Distribution
# -------------------------------
st.subheader("🌧 Precipitation Distribution")

st.write("Boxplot of rainfall (PRECTOTCORR)")

st.dataframe(filtered_df[["Country", "PRECTOTCORR"]])

# -------------------------------
# 📊 Summary Stats
# -------------------------------
st.subheader("📊 Summary Statistics")

st.write(filtered_df.describe())