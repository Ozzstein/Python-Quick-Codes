# Dict format is {key1: value1, ...}
capitals = {'Australia': 'Canberra', 'Singapore': 'Singapore', 'USA': 'Washington, DC', 'Somalia': 'Mogadishu'}

# Method 1 for looping
for country in capitals:
    print("The capital of", country, "is", capitals[country])

# Method 2
for (country, capital) in capitals.items():
    print("The capital of", country, "is", capital)
