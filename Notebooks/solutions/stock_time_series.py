import pandas as pd

ts = pd.read_hdf("/data/AAPL.h5")

# Exercise 1
print("Per year volumes:")
print(ts['Volume'].resample("A").sum())

# Exercise 2
increase = ts["Close"] - ts["Open"]
print("The maximum increase of", increase["2005":"2010"].max(), "happened on", increase["2005":"2010"].argmax())

# Exercise 3
adj_increase = ts["Adj Close"].resample("A").diff().dropna()
print("The maximum annual increase of the Adj Close was", adj_increase.max(), "and happened in", adj_increase.argmax().year)