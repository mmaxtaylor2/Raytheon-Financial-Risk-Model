import pandas as pd

# Load the fundamentals file created earlier
df = pd.read_csv("data/financials.csv", index_col=0)

# Standardize column names for easier access
df.columns = [col.replace(" ", "_").replace("/", "_") for col in df.columns]

# Construct a comps table
comps = pd.DataFrame({
    "EV/EBITDA": df["EV_EBITDA"].round(2),
    "P/FCF": df["P_FCF"].fillna("N/A"),  # handle missing values cleanly
    "5Y Revenue CAGR (%)": (df["5Y_Revenue_CAGR"] * 100).round(1),
    "Market Cap ($B)": (df["Market_Cap"] / 1e9).round(1),
})

# Label the sector benchmark
comps.loc["ITA", "Comment"] = "Sector benchmark"

# Export cleaned comps table
comps.to_csv("data/comps_table_clean.csv")

print("Comps table created and saved to: data/comps_table_clean.csv")
print()
print(comps)

