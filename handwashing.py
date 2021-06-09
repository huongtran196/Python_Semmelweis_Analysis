import pandas as pd
yearly = pd.read_csv('datasets/yearly_deaths_by_clinic.csv')
print(yearly)

# Calculate the proportion of deaths 
yearly['proportion_deaths'] = yearly['deaths'] / yearly['births']
clinic_1 = yearly[yearly['clinic'] == 'clinic 1']
clinic_2 = yearly[yearly['clinic'] == 'clinic 2']
print(clinic_1)

