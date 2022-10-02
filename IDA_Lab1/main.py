import pandas as pd
import seaborn as sn

# def group_by_age(df):
#     df['Age_Group'] = pd.cut(x=df['Age'], bins=[0, 1, 18, 25, 35, 45, 50, 56],
#                              labels=['Under 18', '18-24', '25-34', '35-44', '45-49', '50-55', '56+'])
#     return df


movies = ['MovieID', 'Title', 'Genres'];
data_movies = pd.read_table(".\\ml-1m\\movies.dat", sep="::", engine='python', names=movies);
moviesDataFrame = pd.DataFrame(data_movies, columns=movies);

ratings = ['UserID', 'MovieID', 'Rating', 'Timestamp'];
data_ratings = pd.read_table(".\\ml-1m\\ratings.dat", sep="::", engine='python', names=ratings);
ratingsDataFrame = pd.DataFrame(data_ratings, columns=ratings);

users = ['UserID', 'Gender', 'Age', 'Occupation', 'Zip-code']
data_users = pd.read_table(".\\ml-1m\\users.dat", sep="::", engine='python', names=users);
usersDataFrame = pd.DataFrame(data_users, columns=users);

mergedDataFrame = moviesDataFrame.merge(ratingsDataFrame.merge(usersDataFrame));

under_18_Group = mergedDataFrame[mergedDataFrame['Age'] == 1];
between_18_24_Group = mergedDataFrame[mergedDataFrame['Age'] == 18];
between_25_34_Group = mergedDataFrame[mergedDataFrame['Age'] == 25];
between_35_44_Group = mergedDataFrame[mergedDataFrame['Age'] == 35];
between_45_49_Group = mergedDataFrame[mergedDataFrame['Age'] == 45];
between_50_55_Group = mergedDataFrame[mergedDataFrame['Age'] == 50];
older_56_Group = mergedDataFrame[mergedDataFrame['Age'] == 56];
groupMale = mergedDataFrame[mergedDataFrame['Gender'] == 'M'];
groupFemale = mergedDataFrame[mergedDataFrame['Gender'] == 'F'];


# mergedDataFrame = group_by_age(mergedDataFrame)

print(under_18_Group.sort_values(by=['Rating'], ascending=False).head(10))
print(between_18_24_Group.sort_values(by=['Rating'], ascending=False).head(10))
print(between_25_34_Group.sort_values(by=['Rating'], ascending=False).head(10))
print(between_35_44_Group.sort_values(by=['Rating'], ascending=False).head(10))
print(between_45_49_Group.sort_values(by=['Rating'], ascending=False).head(10))
print(between_50_55_Group.sort_values(by=['Rating'], ascending=False).head(10))
print(older_56_Group.sort_values(by=['Rating'], ascending=False).head(10))

print(groupMale.sort_values(by=['Rating'], ascending=False).head(10))
print(groupMale.sort_values(by=['Rating'], ascending=False).head(10))
