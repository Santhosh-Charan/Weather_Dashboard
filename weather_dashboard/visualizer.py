import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_weather(records: list[dict], save_path: str = "dashboard.png"):
    df = pd.DataFrame(records)
    sns.set(style="whitegrid")

    fig, ax1 = plt.subplots(figsize=(10,6))
    ax2 = ax1.twinx()

    sns.barplot(x="city", y="humidity", data=df, alpha=0.4, color="tab:blue", ax=ax2)
    sns.lineplot(x="city", y="temp", data=df, marker="o", color="tab:red", ax=ax1)

    ax1.set_ylabel("Temperature (°C)", color="tab:red")
    ax2.set_ylabel("Humidity (%)", color="tab:blue")
    plt.title("Weather Comparison Across Cities")
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close(fig)  # Close the figure to prevent display in IDLE
