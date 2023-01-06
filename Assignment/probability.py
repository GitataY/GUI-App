import random

# Set the number of iterations
n_iter = 10000

# Set the number of countries and cities
n_countries = 10
n_cities = 10

# Set the minimum and maximum values for the country and city numbers
min_value = 1
max_value = 20

# Keep track of how many times we score two or more points
count = 0

# Repeat the simulation n_iter times
for i in range(n_iter):
    # Generate two lists of random numbers
    countries = [random.randint(min_value, max_value) for i in range(n_countries)]
    cities = [random.randint(min_value, max_value) for i in range(n_cities)]

    # Count the number of matches between the two lists
    matches = 0
    for country in countries:
        if country in cities:
            matches += 1

    # If we score two or more points, increment the count
    if matches >= 2:
        count += 1

# Calculate the probability of scoring two or more points
probability = count / n_iter

# Print the result
print(f'The probability of scoring two or more points is {probability}')
