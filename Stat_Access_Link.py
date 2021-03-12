import pandas as pd

# Load the dataset
df = pd.read_csv('stat_access_link.csv')
# Replace tags and protocol parts with '' to extract pure url
df['Stats_Access_Link'] = df['Stats_Access_Link'].str.replace('<url>https://','')
df['Stats_Access_Link'] = df['Stats_Access_Link'].str.replace('</url>','')
df['Stats_Access_Link'] = df['Stats_Access_Link'].str.replace('<url>http://','')
df['Stats_Access_Link'] = df['Stats_Access_Link'].str.lower()# string to lowercase
print(df.head(5))
