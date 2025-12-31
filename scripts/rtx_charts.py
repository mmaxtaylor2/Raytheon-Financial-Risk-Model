import pandas as pd
import matplotlib.pyplot as plt

# Load the price data generated earlier
prices = pd.read_csv("data/prices.csv", index_col=0, parse_dates=True)

# RTX vs Sector Benchmark (ITA)
def chart_rtx_vs_ita():
    subset = prices[["RTX", "ITA"]]
    subset = (subset / subset.iloc[0]) * 100  # normalize
    subset.plot(figsize=(10, 5), title="RTX vs ITA (Sector Benchmark)")
    plt.xlabel("Date")
    plt.ylabel("Indexed Performance (Base = 100)")
    plt.tight_layout()
    plt.savefig("data/rtx_vs_ita.png")
    plt.close()

# RTX vs Peer Set (LMT, NOC, GD)
def chart_rtx_vs_peers():
    peers = prices[["RTX", "LMT", "NOC", "GD"]]
    peers = (peers / peers.iloc[0]) * 100
    peers.plot(figsize=(10, 5), title="RTX vs Defense Peers")
    plt.xlabel("Date")
    plt.ylabel("Indexed Performance (Base = 100)")
    plt.tight_layout()
    plt.savefig("data/rtx_vs_peers.png")
    plt.close()

if __name__ == "__main__":
    print("Building charts...")
    chart_rtx_vs_ita()
    chart_rtx_vs_peers()
    print("Charts generated:")
    print(" - data/rtx_vs_ita.png")
    print(" - data/rtx_vs_peers.png")

