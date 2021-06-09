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
plt.show()