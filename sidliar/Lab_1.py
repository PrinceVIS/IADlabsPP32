import pandas as pd

movies = pd.read_table('movies.dat', sep='::', encoding='ISO-8859-1', engine='python')
ratings = pd.read_table('ratings.dat', sep='::', encoding='ISO-8859-1', engine='python')
users = pd.read_table('users.dat', sep='::', encoding='ISO-8859-1', engine='python')

print("------------------------------------------------------------")
print("Movies\n", movies)
print("------------------------------------------------------------")
print("ratings\n", ratings)
print("------------------------------------------------------------")
print("User\n", users)
print("------------------------------------------------------------")

temp_table = ratings.merge(movies, right_on='movie_id', left_on='movie_id')
result_table = temp_table.merge(users, right_on='user_id', left_on='user_id')
print("Result\n", result_table)

young = result_table.query("age >= 1 & age <= 17")
adult = result_table.query("age >= 18 & age <= 59")
old = result_table.query("age >= 60")

print(f'Youth:\n{young}')
print(f'Adults:\n{adult}')
print(f'Olds:\n{old}')

m1 = young['gender'] == 'M'
m_youth = young.loc[m1]
m_youth_top10 = m_youth.sort_values(by='rating', ascending=False).head(10)
print("Top 10 in the category of young men with age 1-17 years\n", m_youth_top10)

f1 = young['gender'] == 'F'
f_youth = young.loc[f1]
f_youth_top10 = f_youth.sort_values(by='rating', ascending=False).head(10)
print("Top 10 in the category of young women with age 1-17 years\n", f_youth_top10)


m2 = adult['gender'] == 'M'
m_adult = adult.loc[m2]
m_adult_top10 = m_adult.sort_values(by='rating', ascending=False).head(10)
print("Top 10 in the category of adult men with age 18-59 years\n", m_adult_top10)

f2 = adult['gender'] == 'F'
f_adult = adult.loc[f2]
f_adult_top10 = f_adult.sort_values(by='rating', ascending=False).head(10)
print("Top 10 in the category of adult women with age 18-59 years\n", f_adult_top10)


m3 = old['gender'] == 'M'
m_old = old.loc[m3]
m_old_top10 = m_old.sort_values(by='rating', ascending=False).head(10)
print("Top 10 in the category of old men with age 60+\n", m_old_top10)

f3 = old['gender'] == 'F'
f_old = old.loc[f3]
f_old_top10 = f_old.sort_values(by='rating', ascending=False).head(10)
print("Top 10 in the category of old women with age 60+\n", f_old_top10)