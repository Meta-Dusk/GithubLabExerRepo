import csv
import matplotlib.pyplot as plt

years = []
prices = []

# read and clean the csv file
with open("breadprice.csv") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        try:
            year = int(row[0])
            price = float(row[1])
            years.append(year)
            prices.append(price)
        except ValueError:
            continue

# plot the data
plt.plot(years, prices, marker='o')
plt.title("Average Price of Bread by Year")
plt.xlabel("Year")
plt.ylabel("Price (USD)")
plt.grid(True)
plt.show()
