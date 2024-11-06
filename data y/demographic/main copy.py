from demographic_data_analyzer import load_data, analyze_data

def main():
    data = load_data()
    
    results = analyze_data(data)

    print("\nAnalisis Data Demografis:")
    print("1. Number of people of each race:\n", results['race_counts'])
    print("2. Average age of men:", results['average_age_men'])
    print("3. Percentage of people with a Bachelor's degree:", results['percentage_bachelors'])
    print("4. Percentage of people with advanced education who earn >50K:", results['percentage_advanced_salary'])
    print("5. Percentage of people without advanced education who earn >50K:", results['percentage_no_advanced_salary'])
    print("6. Minimum hours worked per week:", results['min_hours_per_week'])
    print("7. Percentage of people who work minimum hours and earn >50K:", results['percentage_min_hours_salary'])
    print("8. Country with the highest percentage of people earning >50K highest:", results['highest_earning_country'], 
          "with percentage", results['highest_earning_percentage'])
    print("9. Most popular jobs for earners >50K di India:", results['popular_occupation_india'])

if __name__ == "__main__":
    main()
