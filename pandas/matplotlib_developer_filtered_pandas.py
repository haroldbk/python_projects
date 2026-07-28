import pandas  as pd
import matplotlib.pyplot as plt
import os

filename = 'pandas/developer.csv'

df = pd.read_csv(filename)
pd.set_option('display.max_columns',87)

countries=['United States','Inda','Germany','Canada','United Kingdom']

filt=(df['country'].isin(countries)) & (df['annual_salary_usd']>163600)

#print(df.loc[filt,['age','annual_salary_usd','country','education_level']])
filtered_df = df.loc[filt]

salary_by_country=(
filtered_df.groupby('country')['annual_salary_usd']
.mean()
.sort_values(ascending=True)
)

plt.figure(figsize=(10,5))
plt.barh(
    y=salary_by_country.index,
    width=salary_by_country.values,
    color='skyblue',
    edgecolor='navy'
)
plt.title('Average Annual Salary by country(filtered>$163.6k)',fontsize=14, fontweight='bold')
plt.xlabel('Average Salary (USD)',fontsize=12)
plt.ylabel('country',fontsize=12)
plt.grid(axis='x',linestyle='--',alpha=0.7)

plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc:"{:,}".format(int(x))))

plt.tight_layout()
plt.show()
