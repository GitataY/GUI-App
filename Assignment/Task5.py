import random

# Number of simulations to run
N = 10000

# Number of countries and cities
n = 10

# Count the number of times we score at least 2 points
count = 0

# Iterate over the simulations
for i in range(N):
    # Randomly shuffle the country names and city names
    countries = list(range(1, n + 1))
    cities = list(range(1, n + 1)) + list(range(1, n + 1))
    random.shuffle(countries)
    random.shuffle(cities)

    # Count the number of correct matches
    score = 0
    for country in countries:
        if country in cities:
            score += 1

    # Check if we scored at least two points
    if score >= 2:
        count += 1

# Print the estimated probability
print(count / N)
