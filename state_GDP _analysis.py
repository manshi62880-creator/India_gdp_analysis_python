import pandas as pd

# load dataset
df = pd.read_csv("/storage/emulated/0/Download/Indias GDP (Statewise).csv")

# view first rows
print(df.head())

# check columns
print(df.columns)

import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("/storage/emulated/0/Download/Indias GDP (Statewise).csv")

# sort by GDP (Billion USD)
df_sorted = df.sort_values(by='Nominal GDP(Billion USD)', ascending=False)

# top 10 states
top10 = df_sorted.head(10)
df['State_UT'] = df['State_UT'].str.strip()
df = df[~df['State_UT'].str.contains('Andaman', case=False)]
df_sorted = df.sort_values(by='Nominal GDP(Billion USD)', ascending=False)
top10 = df_sorted.head(10)


plot Graph 1
plt.figure(figsize=(12,6))
plt.bar(top10['State_UT'], top10['Nominal GDP(Billion USD)'])
plt.xticks(rotation=25)
plt.title("Top 10 Indian States by Nominal GDP (USD Billion )")
plt.xlabel("States")
plt.ylabel("GDP (Billion USD)")

plt.tight_layout()
plt.show()

population = {
    'Maharashtra': 124000000,
    'Tamil Nadu': 78000000,
    'Gujarat': 70000000,
    'Karnataka': 68000000,
    'Uttar Pradesh': 240000000,
    'West Bengal': 100000000,
    'Rajasthan': 81000000,
    'Telangana': 40000000,
    'Andhra Pradesh': 53000000,
    'Madhya Pradesh': 85000000
}
df['Population'] = df['State_UT'].map(population)
df['Per Capita GDP'] = (df['Nominal GDP(Billion USD)'] * 1e9) / df['Population']
df_sorted_pc = df.sort_values(by='Per Capita GDP', ascending=False)
top10_pc = df_sorted_pc.head(10)

#graph2
show_total = False
show_per_capita = True

plt.figure(figsize=(12,6))

plt.bar(top10_pc['State_UT'], top10_pc['Per Capita GDP'])

plt.title("Per Capita GDP by State (USD)", fontsize=14, weight='bold')
plt.xlabel("States")
plt.ylabel("Per Capita GDP (USD)")

plt.xticks(rotation=40, ha='right')

plt.tight_layout()
plt.show()

for i, v in enumerate(top10_pc['Per Capita GDP']):
    plt.text(i, v + 50, f"{int(v)}", ha='center', fontsize=9)
    top10_pc = top10_pc.sort_values(by="Per Capita GDP", ascending=False)
    
    
    #import matplotlib.pyplot as plt

plt.figure(figsize=(12,10))

# Graph 1 : Total GDP
plt.subplot(2,1,1)
plt.bar(top10['State_UT'], top10['Nominal GDP(Billion USD)'])
plt.title("Top States by Total GDP (Billion USD)", weight='bold')
plt.ylabel("GDP (Billion USD)")
plt.xticks(rotation=40, ha='right')

# Graph 2 : Per Capita GDP
plt.subplot(2,1,2)
plt.bar(top10_pc['State_UT'], top10_pc['Per Capita GDP'])
plt.title("Top States by Per Capita GDP (USD)", weight='bold')
plt.ylabel("Per Capita GDP (USD)")
plt.xticks(rotation=40, ha='right')

plt.tight_layout()
plt.show()
    
   



   

