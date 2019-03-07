import pandas as pd
import researchpy as rp
from scipy import stats

df = pd.read_csv("mental-heath-in-tech.csv")

#print(df.info())
#print(df.head())

#print(rp.summary_cat(df[['Do you currently have a mental health disorder?', 'Would you have been willing to discuss a mental health issue with your direct supervisor(s)?' ]]))

def drop_maybe(series):
    if series.lower() == 'yes' or series.lower() == 'no':
        return series
    else:
        return

df['current_mental_disorder'] = df['Do you currently have a mental health disorder?'].apply(drop_maybe)
df['willing_discuss_mh_supervisor'] = df['Would you have been willing to discuss a mental health issue with your direct supervisor(s)?']

print(rp.summary_cat(df[['current_mental_disorder', 'willing_discuss_mh_supervisor']]))
print("\n **************************** \n")
print(df[['current_mental_disorder', 'willing_discuss_mh_supervisor']].info())
print("\n **************************** \n")
print(pd.crosstab(df['willing_discuss_mh_supervisor'], df['current_mental_disorder']))

crosstab = pd.crosstab(df['willing_discuss_mh_supervisor'], df['current_mental_disorder'])

print("\n **************************** \n")
print(stats.chi2_contingency(crosstab))

# The H0 (Null Hypothesis): There is no relationship between variable one and variable two
# The H1 (Alternative Hypothesis): There is a relationship between variable 1 and variable 2
# If the p-value is significant, you can reject the null hypothesis and claim that the findings support the alternative hypothesis

# ******** Assumptions **********
# When testing the data, the cells should be counts of cases and not percentages. It is okay to convert to percentages after testing the data
# The levels (groups) of the variables being tested are mutually exclusive
# Each participant contributes to only one cell within the Chi-square table
# The groups being tested must be independent
# The value of expected cells should be greater than 5 for at least 20% of the cells

# p < 0.05 => we can reject the null hypothesis

# Chi-square Test of Independence Post Hoc Testing: Bonferroni-adjusted method

dummies = pd.get_dummies(df['willing_discuss_mh_supervisor'])
dummies.drop(["I don't know"], axis= 1, inplace= True)
print("\n **************************** \n")
print(dummies.head())
print("\n **************************** \n")

for series in dummies:
    nl = "\n"
    crosstab = pd.crosstab(dummies[f"{series}"], df['current_mental_disorder'])
    print(crosstab, nl)
    chi2, p, dof, expected = stats.chi2_contingency(crosstab)
    print(f"Chi2 value= {chi2}{nl}p-value= {p}{nl}Degrees of freedom= {dof}{nl}")




