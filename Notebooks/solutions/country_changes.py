import pandas as pd

countries = pd.read_csv("data/country_populations_by_year.csv", index_col="Country Name")
populations = countries.drop("Country Code", axis=1).transpose()

# Exercise 1
pct_change_10years = populations.pct_change(10).dropna()
print("Highest % change oer 10 years is: ", pct_change_10years.max().argmax(), "with a percentage increase of", 100 * pct_change_10years.max().max())
print("This happened in", pct_change_10years["United Arab Emirates"].argmax())

# Exercise 2
absolute_growth = populations.diff().dropna()

print("Highest absolute growth in a single year is: ", absolute_growth.max().argmax(), "with an increase of", absolute_growth.max().max())
print("This happened in", absolute_growth["China"].argmax())


# Exercise 3
min_std_country, min_std_value = populations.std().argmin(), populations.std().min()
print("The most stable growth (minimum standard deviation) is", min_std_country, "with a std dev of", min_std_value)