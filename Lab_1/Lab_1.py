import pandas as pd
movies = pd.read_table('movies.dat', sep='::', encoding='ISO-8859-1', engine='python')
ratings = pd.read_table('ratings.dat', sep='::', encoding='ISO-8859-1', engine='python')
user = pd.read_table('users.dat', sep='::', encoding='ISO-8859-1', engine='python')
print("Table: Movies\n", movies)
print("Table: Ratings\n", ratings)
print("Table: User\n", user)
table = ratings.merge(movies, right_on='MovieID', left_on='MovieID')
full_table = table.merge(user, right_on='UserID', left_on='UserID')
print("Full Table:\n", full_table)

age1 = full_table.query("Age >= 1 & Age <= 17")
age18 = full_table.query("Age >= 18 & Age <= 24")
age25 = full_table.query("Age >= 25 & Age <= 34")
age35 = full_table.query("Age >= 35 & Age <= 44")
age45 = full_table.query("Age >= 45 & Age <= 49")
age50 = full_table.query("Age >= 50 & Age <= 54")
age55 = full_table.query("Age >= 55")

print(f'Table: age1:\n{age1}')
print(f'Table: age18:\n{age18}')
print(f'Table: age25:\n{age25}')
print(f'Table: age35:\n{age35}')
print(f'Table: age45:\n{age45}')
print(f'Table: age50:\n{age50}')
print(f'Table: age55:\n{age55}')

m1 = age1['Gender'] == 'M'
m_age1 = age1.loc[m1]
m_age1_top10 = m_age1.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of men aged 1-17 years\n", m_age1_top10)

f1 = age1['Gender'] == 'F'
f_age1 = age1.loc[f1]
f_age1_top10 = f_age1.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of women aged 1-17 years\n", f_age1_top10)

m18 = age18['Gender'] == 'M'
m_age18 = age18.loc[m18]
m_age18_top10 = m_age18.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of men aged 18-24 years\n", m_age18_top10)

f18 = age18['Gender'] == 'F'
f_age18 = age18.loc[f18]
f_age18_top10 = f_age18.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of women aged 18-24 years\n",f_age18_top10)

m25 = age25['Gender'] == 'M'
m_age25 = age25.loc[m25]
m_age25_top10 = m_age25.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of men aged 25-34 years\n", m_age25_top10)

f25 = age25['Gender'] == 'F'
f_age25 = age25.loc[f25]
f_age25_top10 = f_age25.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of women aged 25-34 years\n", f_age25_top10)

m35 = age35['Gender'] == 'M'
m_age35 = age35.loc[m35]
m_age35_top10 = m_age35.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of men aged 35-44 years\n", m_age35_top10)

f35 = age35['Gender'] == 'F'
f_age35 = age35.loc[f35]
f_age35_top10 = f_age35.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of women aged 35-44 years\n", f_age35_top10)

m45 = age45['Gender'] == 'M'
m_age45 = age45.loc[m45]
m_age45_top10 = m_age45.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of men aged 45-49 years\n", m_age45_top10)

f45 = age45['Gender'] == 'F'
f_age45 = age45.loc[f45]
f_age45_top10 = f_age45.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of women aged 45-49 years\n", f_age45_top10)

m50 = age50['Gender'] == 'M'
m_age50 = age50.loc[m50]
m_age50_top10 = m_age50.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of men aged 50-55 years\n", m_age50_top10)

f50 = age50['Gender'] == 'F'
f_age50 = age50.loc[f50]
f_age50_top10 = f_age50.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of women aged 50-55 years\n", f_age50_top10)

m55 = age55['Gender'] == 'M'
m_age55 = age55.loc[m55]
m_age55_top10 = m_age55.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of men aged 55+ years\n", m_age55_top10)

f55 = age55['Gender'] == 'F'
f_age55 = age55.loc[f55]
f_age55_top10 = f_age55.sort_values(by='Rating', ascending=False).head(10)
print("Table: Top 10 in the category of women aged 55+ years\n", f_age55_top10)