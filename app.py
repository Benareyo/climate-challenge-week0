import streamlit as st
import pandas as pd
from src.visualizer import plot_temperature, plot_relationship

st.title("🌍 Climate Data Analyzer")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Data Preview")
    st.write(df.head())

    # 🔍 Show columns
    st.write("Columns in your dataset:", df.columns.tolist())

    # 🧹 Clean column names
    df.columns = df.columns.str.strip().str.lower()

    columns = df.columns.tolist()

    # ✅ Prevent selecting same column twice
    temp_col = st.selectbox("Select Temperature Column", columns)

    hum_col = st.selectbox(
        "Select Humidity Column",
        [col for col in columns if col != temp_col]
    )

    # 🎯 Filter
    st.subheader("🔎 Filter Data")

    min_temp = st.slider(
        "Minimum Temperature",
        int(df[temp_col].min()),
        int(df[temp_col].max())
    )

    filtered_df = df[df[temp_col] >= min_temp]

    st.write("Filtered Data")
    st.write(filtered_df)

    # ✅ Rename properly
    renamed_df = filtered_df.rename(columns={
        temp_col: "temperature",
        hum_col: "humidity"
    })

    st.write("Renamed columns:", renamed_df.columns.tolist())

    # 📈 Plots

    st.subheader("📉 Temperature Distribution")
    plot_temperature(renamed_df)

    st.subheader("📊 Temperature vs Humidity")
    plot_relationship(renamed_df)


    st.subheader("📊 Insights")

    avg_temp = renamed_df["temperature"].mean()
    avg_hum = renamed_df["humidity"].mean()

    st.write(f"🌡️ Average Temperature: {avg_temp:.2f}")
    st.write(f"💧 Average Humidity: {avg_hum:.2f}")

    # Correlation
    correlation = renamed_df["temperature"].corr(renamed_df["humidity"])

    st.write(f"🔗 Correlation between Temperature and Humidity: {correlation:.2f}")

    # Interpretation
    if correlation > 0:
        st.success("As temperature increases, humidity also tends to increase.")
    elif correlation < 0:
        st.warning("As temperature increases, humidity tends to decrease.")
    else:
        st.info("No strong relationship between temperature and humidity.")