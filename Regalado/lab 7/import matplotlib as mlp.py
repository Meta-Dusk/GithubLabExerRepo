import matplotlib-pyplot as plt 
import pandas as pd

# Read CS file
df • pd.read_csv('breadprice.csv') # Replace with your actual file name

# Set 'Year' as the index
df. set_index("Year', inplace=true)

# Convert all date to numeric, handling missing values 
df = df.apply(pd. to numeric, errors»' coerce*)

# Plot data
plt. figure(figsize»(10, 6)) 
for year in df.index:
    plt.plot(df.columns, df.loc[year), markers'o', labelestr(year))

# Labels and title
plt.xlabel ("Month")
plt.ylabel ("Bread Average")
plt.title(Monthly Bread Prices Over the Years")
plt.legend (title="Year", bbox_to_anchor=(1.05, 1), loc= upper left') 
plt.grid(True)

#Show plot 
pit .show()
