import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def plot_temperature(df):
    plt.figure()
    sns.histplot(df["temperature"], kde=True)
    plt.title("Temperature Distribution")
    st.pyplot(plt)


def plot_relationship(df):
    plt.figure()
    sns.scatterplot(x=df["temperature"], y=df["humidity"])
    plt.title("Temperature vs Humidity")
    st.pyplot(plt)