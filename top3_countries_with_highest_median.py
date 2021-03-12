import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# Load the dataset
df = pd.read_csv('country_vaccination_stats.csv')
# Get minimum value of column 'daily_vaccinations
# Fill the missing data (impute) in daily_vaccinations column per country
# Group the data by number of rows: once and more than once by country
df1 = df[df.groupby('country')["country"].transform('count') == 1] # For example, Kuwait
df2 = df[df.groupby('country')["country"].transform('count') > 1] # For example, Argentina
df1['daily_vaccinations'] = df1['daily_vaccinations'].fillna(0) # Fill the NaN values with "0" in 'daily_vaccinations' column
df2["daily_vaccinations"] = df2.groupby("country")["daily_vaccinations"].transform(lambda x: x.fillna(x.min())) # Fill the NaN values with min value in 'daily_vaccinations' column by relevant country

frames = [df2, df1] # list of this frames
df= pd.concat(frames) # merge df1 and df2 updated dataframes

# Get top-3 countries with highest median daily vaccination numbers
df=df.groupby(by='country')['daily_vaccinations'].median().sort_values(ascending=False).index[:3]
print(df)

'''
top-3 countries:
'United States', 'China', 'India' 
'''
