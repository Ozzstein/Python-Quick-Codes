
import pandas as pd

# Exercise 1
forbes = pd.read_csv("/data/forbes1964.csv", index_col='rank')

# Exercise 2
print("Counts (use a loop to see them all)")
print(forbes.groupby("country").apply(len))

# Exercise 3
summed_values = forbes.groupby("country").apply(sum)
profits = summed_values['profits']
assets = summed_values['assets']
roi = profits / assets
print("Best ROI")
best = roi.argmax(), roi.max()
print(best)