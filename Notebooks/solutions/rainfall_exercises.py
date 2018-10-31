import pandas as pd
rain = pd.read_csv(filename, header=None, names=['date', 'rainfall'],
                   parse_dates=['date'], dayfirst=True,
                   index_col='date')

# Exercise 1
def most_rain_since(amount):
    # Computes the previous date it rained at least this much
    return (rain["rainfall"] > amount).index.max()

most_rain_since(2500)


# Exercise 2
rolling_week_rainfall = rain.rolling(7)['rainfall'].apply(sum)
print("The 7 dryest days ended on {} with a total rainfall of just {} points!".format(rolling_week_rainfall.argmin(),
                                                                                     rolling_week_rainfall.min()))


# Harder Exercise 2
monthly_average = rain.groupby(rain.index.month).mean()['rainfall']
rain["MoreThanMonthlyAverage"] = rain['rainfall'] > monthly_average.ix[rain.index.month].values
print("Days with more rain than the overall monthly average:")
print(rain[rain["MoreThanMonthlyAverage"]].head())  # Remove head() to see them all

# Harder Exercise 3
print("Days with more rain than the average for its current month:")
current_monthly_average = rain.groupby([rain.index.year, rain.index.month]).mean()['rainfall']
rain["MoreThanCurrentMonth"] = rain['rainfall'] > current_monthly_average.ix[zip(rain.index.year, rain.index.month)].values
print(rain.head())