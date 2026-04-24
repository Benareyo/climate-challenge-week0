import matplotlib.pyplot as plt
import seaborn as sns

def plot_temperature(df):
    """
    Plot temperature distribution
    """
    plt.figure()
    sns.histplot(df["temperature"], kde=True)
    plt.title("Temperature Distribution")
    plt.xlabel("Temperature")
    plt.ylabel("Frequency")
    plt.show()


def plot_relationship(df):
    """
    Plot temperature vs humidity
    """
    plt.figure()
    sns.scatterplot(x=df["temperature"], y=df["humidity"])
    plt.title("Temperature vs Humidity")
    plt.xlabel("Temperature")
    plt.ylabel("Humidity")
    plt.show()