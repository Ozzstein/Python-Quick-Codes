# Load OECD Countries
with open("data/oecd_stats.csv") as inf:
    oecd_countries = set()
    next(inf)  # Skip header
    for line in inf:
        country = line.split(",")[0]
        oecd_countries.add(country)
        
print(oecd_countries)

# Load European countries
with open("data/Countries-Continents.csv") as inf:
    european_countries = set()
    next(inf)
    for line in inf:
        if line.startswith("Europe"):
            country = line.split(",")[1].strip()  # Remove newlines as well
            european_countries.add(country)
print(european_countries)

print(european_countries & oecd_countries)