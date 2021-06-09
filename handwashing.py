import pandas as pd
import matplotlib.pyplot as plt

yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')
print(yearly)

# Calculate the proportion of deaths 
yearly['proportion_deaths'] = yearly['deaths'] / yearly['births']
clinic_1 = yearly[yearly['clinic'] == 'clinic 1']
clinic_2 = yearly[yearly['clinic'] == 'clinic 2']
print(clinic_1)

# Plot the yearly proportion deaths for both clinics
ax = clinic_1.plot(x='year', y='proportion_deaths', label='Clinic 1')
clinic_2.plot(x='year', y='proportion_deaths', label='Clinic 2', ax=ax, ylabel='Proportion deaths')
plt.legend()
plt.show()

# Load monthly deaths dataset
monthly = pd.read_csv('datesets/monthly_deaths.csv', parse_dates=['date'])
monthly['proportion_deaths'] = monthly['deaths'] / monthly['births']
print(monthly.head(1))

# Plot the monthly proportion deaths of Clinic 1
ax = monthly.plot(x='date', y='proportion_deaths', ylabel='Proportion deaths')
plt.show()

# Highlight the effect of handwashing
handwashing_start = pd.to_datetime('1847-06-01') # date when handwashing was made mandatory
before_washing = monthly[monthly['date'] < handwashing_start]
after_washing = monthly[monthly['date'] >= handwashing_start]
ax = before_washing.plot(x='date', y='proportion_deaths', label='Before washing')
after_washing.plot(x='date', y='proportion_deaths', label='After washing', ax=ax, ylabel='Proportion deaths')
plt.legend()
plt.show()

# Difference in mean monthly proportion of deaths due to handwashing
mean_diff = after_washing['proportion_deaths'].mean() - before_washing['proportion_deaths'].mean()
print(mean_diff)

# A bootstrap analysis of the reduction of deaths due to handwashing
before_proportion = before_washing['proportion_deaths']
after_proportion = after_washing['proportion_deaths']

boot_mean_diff = []
for i in range(3000):
    boot_before = before_proportion.sample(frac=1, replace=True)
    boot_after = after_proportion.sample(frac=1, replace=True)
    boot_mean_diff.append(boot_after.mean() - boot_before.mean())

# Calculating a 95% confidence interval from boot_mean_diff 
confidence_interval = pd.Series(boot_mean_diff).quantile([0.025, 0.975])
print(confidence_interval)

