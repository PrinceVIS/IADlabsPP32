import pandas

def main():
    pandas.set_option('display.max_columns', None)

    movies_content = pandas.read_table('DataSet/movies.dat', sep = '::', encoding = 'ISO-8859-1', engine = 'python')
    ratings_content = pandas.read_table('DataSet/ratings.dat', sep = '::', encoding = 'ISO-8859-1', engine = 'python')
    users_content = pandas.read_table('DataSet/users.dat', sep = '::', encoding = 'ISO-8859-1', engine = 'python')

    merged_table = ratings_content.merge(movies_content, right_on = 'MovieID', left_on = 'MovieID')
    merged_table = merged_table.merge(users_content, right_on = 'UserID', left_on = 'UserID')


    kid_raitings = merged_table.query("Age >= 1 & Age <= 11")              #range 1-11
    teen_raitings = merged_table.query("Age >= 12 & Age <= 17")            #range 12-17    
    youth_raitings = merged_table.query("Age >= 18 & Age <= 29")           #range 18-29
    adults_raitings = merged_table.query("Age >= 30 & Age <= 54")          #range 30-54
    old_raitings = merged_table.query("Age >= 55")                         #range 55-...

    male_raitings = merged_table.query("Sex == 'M'")
    female_raitings = merged_table.query("Sex == 'F'")

    print(f"All male:\n{male_raitings.sort_values(by = ['Rating'], ascending = False).head(10)}\n")
    print(f"All female:\n{female_raitings.sort_values(by = ['Rating'], ascending = False).head(10)}\n")

    all_ages_table = {
        11 : kid_raitings,
        17 : teen_raitings,
        29 : youth_raitings,
        54 : adults_raitings,
        55 : old_raitings
    }

    index = 0;
    for table in all_ages_table.values() :

        age = list(all_ages_table.keys())[index]
        index += 1

        msg = 'under' if age < 55 else 'older then'

        male_age_raitings = table.query("Sex == 'M'")
        female_age_raitings = table.query("Sex == 'F'")

        print(f"All male {msg} {age} years:\n{male_age_raitings.sort_values(by = ['Rating'], ascending = False).head(10)}\n")
        print(f"All female {msg} {age} years:\n{female_age_raitings.sort_values(by = ['Rating'], ascending = False).head(10)}\n")





if __name__ == '__main__' :
    main()
