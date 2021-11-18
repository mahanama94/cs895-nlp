import pandas as pd

volume_df = pd.read_csv("data/options/GME-volume.csv")

volume_df = volume_df.groupby(by="Trade Date").sum()
volume_df["Date"] = volume_df.index.str.replace("/", "-")

volatility_df = pd.read_csv("data/options/GME-volatility.csv")
volatility_df["Date"] = volatility_df["Date"].str.replace("/", "-")

merged = volume_df.merge(volatility_df, left_on='Date', right_on='Date')
merged.to_csv("data/options/GME-merged.csv")

volume_df.to_csv("data/options/GME-volume-processed.csv")

volume_df.head()
