import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1. How many people of each race are represented in this dataset? 
    race_counts = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'].value_counts(normalize=True) * 100)['Bachelors']

    # 4. What percentage of people with advanced education make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_higher_education = (len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100

    # 5. What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    percentage_lower_education = (len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100

    # 6. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_percentage = (len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]) / num_min_workers) * 100

    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    highest_earning_country = (df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentage = ((df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()).max()) * 100

    # 9. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("1. People of each race represented in the dataset:\n", race_counts)
        print("\n2. Average age of men:", round(average_age_men, 1))
        print("\n3. Percentage of people with a Bachelor's degree:", round(percentage_bachelors, 1))
        print("\n4. Percentage of people with advanced education (>50K):", round(percentage_higher_education, 1))
        print("\n5. Percentage of people without advanced education (>50K):", round(percentage_lower_education, 1))
        print("\n6. Minimum number of hours a person works per week:", min_work_hours)
        print("\n7. Percentage of people who work the minimum number of hours per week and earn >50K:", round(rich_percentage, 1))
        print("\n8. Country with the highest percentage of people earning >50K:", highest_earning_country)
        print("   Percentage:", round(highest_earning_country_percentage, 1))
        print("\n9. Most popular occupation for those earning >50K in India:", top_IN_occupation)

    return {
        'race_counts': race_counts,
        'average_age_men': round(average_age_men, 1),
        'percentage_bachelors': round(percentage_bachelors, 1),
        'percentage_higher_education': round(percentage_higher_education, 1),
        'percentage_lower_education': round(percentage_lower_education, 1),
        'min_work_hours': min_work_hours,
        'rich_percentage': round(rich_percentage, 1),
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': round(highest_earning_country_percentage, 1),
        'top_IN_occupation': top_IN_occupation
    }

if __name__ == "__main__":
    calculate_demographic_data()
