import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Getting the initial data
consumer_data = pd.read_csv('Consumer_Shopping_Trends_2026.csv')
print(consumer_data.head())
print("This dataset has ", len(consumer_data), " rows(observations), and ", len(consumer_data.columns), " columns")


# Checking for value types and missing values
print(consumer_data.isnull().sum())
print(consumer_data.dtypes)

## Exploring the data
# Outliers
def print_outliers(data):
    print("\n Min and max values:")
    for col in data.columns:
        print(f"  {col}: min = {data[col].min()}, max = {data[col].max()}")

print_outliers(consumer_data)


# media and mean of monthly income
def income(income):
    avg_income = income.mean()
    median_income = income.median()
    return avg_income, median_income

avg_income, median_income = income(consumer_data['monthly_income'])
print(f"Average income: {avg_income:,.2f}")
print(f"Median income:  {median_income:,.2f}\n")


# median and mean of monthly spend
def spend(spend):
    avg_spend = spend.mean()
    median_spend = spend.median()
    return avg_spend, median_spend
avg_spend, median_spend = spend(consumer_data['avg_online_spend']+consumer_data['avg_store_spend'])
print(f"Average spend: {avg_spend:,.2f}")
print(f"Median spend:  {median_spend:,.2f}\n")


## Answering questions
# Are more sales on average made online or in stores(offline)?
def online_vs_offline(online, store):
    avg_online = online.mean()
    avg_store = store.mean()
    difference = avg_online - avg_store
    return avg_online, avg_store, difference

online_spend, store_spend, difference = online_vs_offline(
    consumer_data['avg_online_spend'],
    consumer_data['avg_store_spend']
)

print(f"Average online spend:  {online_spend:,.2f}")
print(f"Average store spend:   {store_spend:,.2f}")
print(f"Difference:            {difference:,.2f}")

# Are men, women, or other more loyal to brands on average?
def loyalty_by_gender(data):
    grouped = data.groupby('gender')['brand_loyalty_score'].mean()
    most_loyal = grouped.idxmax()

    for gender, score in grouped.items():
        print(f"  {gender}: {score:.2f}")

    print(f"\nMost loyal group on average: {most_loyal}")

    return grouped

loyalty_by_gender(consumer_data)

# How does delivery fee sensitivity affect spending habits?
def deliv_fee_vs_spending(data):                        # missing colon fixed
    grouped = data.groupby('delivery_fee_sensitivity')['avg_online_spend'].mean()

    global_avg = consumer_data['avg_online_spend'].mean()
    avg_low_sensitivity  = grouped[grouped.index <= 3].mean()
    avg_mid_sensitivity  = grouped[(grouped.index >= 4) & (grouped.index <= 6)].mean()
    avg_high_sensitivity = grouped[grouped.index >= 7].mean()


    print(f"\nGlobal average online spend:          {global_avg:,.2f}")
    print(f"Avg spend - Low sensitivity (1-3):    {avg_low_sensitivity:,.2f}")
    print(f"Avg spend - Mid sensitivity (4-6):    {avg_mid_sensitivity:,.2f}")
    print(f"Avg spend - High sensitivity (7-10):  {avg_high_sensitivity:,.2f}\n")

    return global_avg, avg_low_sensitivity, avg_mid_sensitivity, avg_high_sensitivity

deliv_fee_vs_spending(consumer_data)

# How does city tier affect your spending? More store, more online?
def city_tier_pref(data):
    grouped_online = data.groupby('city_tier')['avg_online_spend'].mean()
    grouped_store  = data.groupby('city_tier')['avg_store_spend'].mean()

    tier_one_online   = grouped_online["Tier 1"]
    tier_one_store    = grouped_store["Tier 1"]
    tier_two_online   = grouped_online["Tier 2"]
    tier_two_store    = grouped_store["Tier 2"]
    tier_three_online = grouped_online["Tier 3"]
    tier_three_store  = grouped_store["Tier 3"]

    for tier in ["Tier 1", "Tier 2", "Tier 3"]:
        print(f"{tier}:")
        print(f"  Online: {grouped_online[tier]:,.2f}")
        print(f"  Store:  {grouped_store[tier]:,.2f}")
        print(f"  Difference (online - store): {grouped_online[tier] - grouped_store[tier]:,.2f}\n")

    return grouped_online, grouped_store

city_tier_pref(consumer_data)


# And how does city tier affect your income, is one tier richer than the other?

def city_tier_income(data):
    grouped = data.groupby('city_tier')['monthly_income'].mean()

    tier_one_income = grouped["Tier 1"]
    tier_two_income = grouped["Tier 2"]
    tier_three_income = grouped["Tier 3"]
    for tier in ["Tier 1", "Tier 2", "Tier 3"]:
        print(f"{tier} average income:")
        print(f"  Monthly income: ${grouped[tier]:,.2f}")
    return grouped
city_tier_income(consumer_data)


# What age group earns the most?
def income_by_age(data):
    grouped = data.groupby('age')['monthly_income'].mean()

    average_income = grouped.mean()  # fix 1
    adult_teens = grouped[grouped.index < 20].mean()  # fix 2
    young_adults = grouped[(grouped.index >= 20) & (grouped.index <= 25)].mean()
    adults = grouped[(grouped.index >= 26) & (grouped.index <= 45)].mean()
    middle_aged = grouped[(grouped.index >= 46) & (grouped.index <= 64)].mean()
    elderly = grouped[(grouped.index >= 65) & (grouped.index <= 120)].mean()

    print(f"\nIncomes per age group:")
    print(f"  Average income:                            {average_income:,.2f}\n")
    print(f"  Adult teens average income (<20):          {adult_teens:,.2f}")
    print(f"  Young adults average income (>= 20, <=25): {young_adults:,.2f}")
    print(f"  Adults average income (>= 26, <=45):       {adults:,.2f}")
    print(f"  Middle aged average income (>= 46, <=64):  {middle_aged:,.2f}")
    print(f"  Elderly average income (>= 65, <=120):     {elderly:,.2f}")

    return average_income, adult_teens, young_adults, adults, middle_aged, elderly


income_by_age(consumer_data)

# Making graphs of findings
fig, axes = plt.subplots(3, 2, figsize=(14, 16))
fig.suptitle("Consumer Shopping Trends 2026", fontsize=16, fontweight='bold')

# 1. Online vs Offline spend
online_spend, store_spend, _ = online_vs_offline(
    consumer_data['avg_online_spend'],
    consumer_data['avg_store_spend']
)
axes[0, 0].bar(['Online', 'In-Store'], [online_spend, store_spend], color=['steelblue', 'coral'])
axes[0, 0].set_title('Average Online vs In-Store Spend')
axes[0, 0].set_ylabel('Average Spend')
min_val = min(online_spend, store_spend)
axes[0, 0].set_ylim(min_val * 0.9, max(online_spend, store_spend) * 1.1)

# 2. Brand loyalty by gender
grouped_loyalty = loyalty_by_gender(consumer_data)
axes[0, 1].bar(grouped_loyalty.index, grouped_loyalty.values, color='mediumpurple')
axes[0, 1].set_title('Brand Loyalty Score by Gender')
axes[0, 1].set_ylabel('Average Loyalty Score')
min_val = min(loyalty_by_gender(consumer_data))
axes[0, 1].set_ylim(min_val * 0.9, max(loyalty_by_gender(consumer_data)) * 1.1)

# 3. Delivery fee sensitivity vs spending
global_avg, avg_low, avg_mid, avg_high = deliv_fee_vs_spending(consumer_data)
axes[1, 0].bar(['Low (1-3)', 'Mid (4-6)', 'High (7-10)'], [avg_low, avg_mid, avg_high], color=['green', 'gold', 'tomato'])
axes[1, 0].axhline(y=global_avg, color='black', linestyle='--', label='Global avg')
axes[1, 0].set_title('Delivery Fee Sensitivity vs Online Spend')
axes[1, 0].set_ylabel('Average Online Spend')
axes[1, 0].legend()
min_val = min(global_avg, avg_low, avg_mid, avg_high)
axes[1, 0].set_ylim(min_val * 0.90, max(global_avg, avg_low, avg_mid, avg_high) * 1.1)

# 4. City tier - online vs store spend
grouped_online, grouped_store = city_tier_pref(consumer_data)
x = np.arange(len(grouped_online.index))
width = 0.35
axes[1, 1].bar(x - width/2, grouped_online.values, width, label='Online', color='steelblue')
axes[1, 1].bar(x + width/2, grouped_store.values, width, label='In-Store', color='coral')
axes[1, 1].set_title('City Tier: Online vs In-Store Spend')
axes[1, 1].set_ylabel('Average Spend')
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(grouped_online.index)
axes[1, 1].legend()
axes[1, 1].set_ylim(74000, max(grouped_online.max(), grouped_store.max()) * 1.01)

# 5. City tier income
grouped_city_income = city_tier_income(consumer_data)
axes[2, 0].bar(grouped_city_income.index, grouped_city_income.values, color='teal')
axes[2, 0].set_title('Average Monthly Income by City Tier')
axes[2, 0].set_ylabel('Average Income')
min_val = min(grouped_city_income)
axes[2, 0].set_ylim(min_val * 0.9, max(grouped_city_income) * 1.1)

# 6. Income by age group
average_income, adult_teens, young_adults, adults, middle_aged, elderly = income_by_age(consumer_data)
age_groups = ['Teens\n(<20)', 'Young Adults\n(20-25)', 'Adults\n(26-45)', 'Middle Aged\n(46-64)', 'Elderly\n(65+)']
age_incomes = [adult_teens, young_adults, adults, middle_aged, elderly]
axes[2, 1].bar(age_groups, age_incomes, color='slateblue')
axes[2, 1].axhline(y=average_income, color='black', linestyle='--', label='Overall avg')
axes[2, 1].set_title('Average Income by Age Group')
axes[2, 1].set_ylabel('Average Income')
axes[2, 1].legend()
min_age_val = min(age_incomes)
axes[2, 1].set_ylim(min_age_val * 0.9, max(age_incomes) * 1.1)
min_val = min(average_income, adults, young_adults, middle_aged, elderly)
axes[2, 1].set_ylim(min_val * 0.9, max(average_income, adult_teens, young_adults, adults, middle_aged, elderly) * 1.1)

plt.tight_layout()
plt.savefig('consumer_trends.png', dpi=150, bbox_inches='tight')
plt.show()