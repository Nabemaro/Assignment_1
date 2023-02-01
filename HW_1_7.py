year_list = [1900, 2019, 2020, 2021, 2022, 2023, 2024, 2100, 2400]


def is_leapyear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


for year in year_list:
    answer = is_leapyear(year)
    print(f'{year} is a leap year: {answer}')