# Consumer-Shopping-Trends-Analysis
An analysis of shopping trends, using Python

The data is from: https://www.kaggle.com/datasets/minahilfatima12328/consumer-shopping-trends-analysis

## Content

The collection includes details about the purchasing habits and shopping habits of consumers. Age, income, internet usage, online orders, store visits, spending patterns, brand loyalty, and shopping preferences are just a few of the behavioural and demographic factors that are included. These factors aid in the analysis of how various customers engage with traditional and virtual retail settings.


## Context

The purpose of this dataset is to investigate contemporary consumer decision making and shopping trends. It can be applied to machine learning, data analysis, and visualization projects to comprehend how lifestyle, digital engagement, and demography affect consumer behavior. The dataset is helpful for conducting data driven research on consumer insights, e-commerce trends, and retail analytics.


## Take-aways
**Overall spending and income**
The average income (131,704) and average total spend (150,216) tell an interesting story — people are spending more than their average monthly income suggests they should. The fact that median and mean are very close for both income and spend indicates the data is evenly distributed with no extreme outliers skewing the results, which makes the findings more reliable.

**Online vs in-store spending**
In-store spending edges out online spending by about 1,107 on average. This is a relatively small difference (~1.5%), suggesting the customer base is nearly equally split between channels. For a business, this means investing in both online and physical presence equally, rather than prioritising one over the other.

**Brand loyalty by gender**
The differences are very small (5.49 to 5.58 out of 10), meaning gender is likely not a meaningful predictor of brand loyalty in this dataset. All three groups score around the midpoint of the scale, suggesting moderate loyalty across the board. A business shouldn't tailor loyalty programmes specifically by gender based on this data.

**Delivery fee sensitivity**
Counterintuitively, high sensitivity customers (7-10) spend almost as much online (74,562) as low sensitivity customers (75,123). The mid sensitivity group actually spends the least (73,919). This suggests delivery fee sensitivity does not strongly influence how much people spend online — customers who care about delivery fees still spend roughly the same amount.

**City tier spending**
In-store spending consistently beats online spending across all three tiers, and the gap actually grows from Tier 1 (-629) to Tier 3 (-1,590). This means the preference for physical shopping strengthens in lower tiers, which could reflect less trust in online shopping or fewer online shopping options in those areas. A business expanding into Tier 3 cities should prioritise physical stores over online infrastructure.

**City tier income**
Income is remarkably consistent across tiers (131,003 to 132,908), meaning city tier does not predict wealth in this dataset. The spending behaviour differences between tiers are therefore driven by preference, not purchasing power.

**Income by age group**
Young adults (20-25) earn the most on average (134,122) while elderly (65+) earn the least ($130,104). However, the range across all groups is only about 5,000, which is quite narrow. Age is therefore not a strong predictor of income in this dataset either. The one actionable insight is that teenagers (<20) earn slightly less, so premium products may be less accessible to that group.

**Overall conclusion**
The most striking finding across all results is how small the differences are between groups. This dataset describes a fairly homogeneous consumer base in terms of income and spending habits, regardless of gender, age, or city tier. The biggest differentiator in behaviour is city tier preference for online vs in-store shopping, which is the most actionable insight for business decisions.


# The print outcomes
 Min and max values:
  age: min = 18, max = 79
  monthly_income: min = 15005, max = 249989
  daily_internet_hours: min = 1.0, max = 12.0
  smartphone_usage_years: min = 1, max = 14
  social_media_hours: min = 0.0, max = 6.0
  online_payment_trust_score: min = 1, max = 10
  tech_savvy_score: min = 1, max = 10
  monthly_online_orders: min = 0, max = 49
  monthly_store_visits: min = 0, max = 19
  avg_online_spend: min = 523, max = 149996
  avg_store_spend: min = 542, max = 149972
  discount_sensitivity: min = 1, max = 10
  return_frequency: min = 0, max = 9
  avg_delivery_days: min = 1, max = 7
  delivery_fee_sensitivity: min = 1, max = 10
  free_return_importance: min = 1, max = 10
  product_availability_online: min = 1, max = 10
  impulse_buying_score: min = 1, max = 10
  need_touch_feel_score: min = 1, max = 10
  brand_loyalty_score: min = 1, max = 10
  environmental_awareness: min = 1, max = 10
  time_pressure_level: min = 1, max = 10

Average income: 131,704.28
Median income:  131,916.00

Average spend: 150,216.56
Median spend:  149,918.00

Average online spend:  74,554.93
Average store spend:   75,661.63
Difference:            -1,106.70


What gender is most loyal to brands on average?
  Female: 5.49
  Male: 5.53
  Other: 5.58
Most loyal group on average: Other


Global average online spend:          74,554.93
Avg spend - Low sensitivity (1-3):    75,123.40
Avg spend - Mid sensitivity (4-6):    73,919.57
Avg spend - High sensitivity (7-10):  74,562.03

Tier 1:
  Online: 74,520.52
  Store:  75,149.96
  Difference (online - store): -629.44

Tier 2:
  Online: 74,907.78
  Store:  76,012.24
  Difference (online - store): -1,104.46

Tier 3:
  Online: 74,244.91
  Store:  75,835.05
  Difference (online - store): -1,590.14

Tier 1 average income:
  Monthly income: $131,003.10
Tier 2 average income:
  Monthly income: $132,908.24
Tier 3 average income:
  Monthly income: $131,235.11

Incomes per age group:
  Average income:                            131,722.06

  Adult teens average income (<20):          128,946.85
  Young adults average income (>= 20, <=25): 134,122.18
  Adults average income (>= 26, <=45):       131,742.19
  Middle aged average income (>= 46, <=64):  132,512.28
  Elderly average income (>= 65, <=120):     130,104.24
