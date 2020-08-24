import datetime
import csv
from pprint import pprint
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

def print_first_point(filename):
    city = filename.split('-')[0].split('/')[-1]
    print('\nCity:{}'.format(city))
    with open(filename, 'r') as f_in:
        trip_reader = csv.DictReader(f_in)
        first_trip = next(trip_reader)
        pprint(first_trip)
    return (city, first_trip)

data_files = ['chicago.csv', 'new_york_city.csv', 'washington.csv']

example_trips = {}
for data_file in data_files:
    city, first_trip = print_first_point(data_file)
    example_trips[city] = first_trip

def duration_in_mins(datum, city):
    if city == 'new_york_city':
        duration = int(datum['Trip Duration'])
    elif city == 'chicago':
        duration = int(datum['Trip Duration'])
    else:
        duration = int(datum['Trip Duration'])
    return duration/60

def date_string_to_weekday(date):
    weekday_dictionary = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
                          3: "Thursday", 4: "Friday", 5: "Saturday",
                          6: "Sunday"}
    month, day, year = date.split('/')
    week_day = datetime.datetime.weekday(datetime.date(int(year), int(month),
                                                       int(day)))
    return weekday_dictionary[week_day]

def time_of_trip(datum, city):
    if city == 'new_york_city':
        month = datum['Start Time'].split('/')[0]
        hour = datum['Start Time'].split()[1].split(':')[0]
        day_of_week = date_string_to_weekday(datum['Start Time'].split()[0])
    elif city == 'chicago':
        month = datum['Start Time'].split('/')[0]
        hour = datum['Start Time'].split()[1].split(':')[0]
        day_of_week = date_string_to_weekday(datum['starttime'].split()[0])
    else:
        month = datum['Start Time'].split('/')[0]
        hour = datum['Start Time'].split()[1].split(':')[0]
        day_of_week = date_string_to_weekday(datum['Start Time'].split()[0])
    return (int(month), int(hour), day_of_week)

def type_of_user(datum, city):
    if city == 'new_york_city': user_type = datum['User Type']
    elif city == 'chicago': user_type = datum['User Type']
    else: user_type = datum['User Type']
    return user_type

def condense_data(in_file, out_file, city):
    with open(out_file, 'w') as f_out, open(in_file, 'r') as f_in:
        out_colnames = ['duration', 'month', 'hour', 'day_of_week', 'user_type']
        trip_writer =csv.DictWriter(f_out, fieldnames = out_colnames)
        trip_writer.writeheader()
        trip_reader = csv.DictReader(f_in)
        first_trip = next(trip_reader)

        for row in trip_reader:
            new_point = {}
            month, hour, day_of_week = time_of_trip(row, city)
            new_point[out_colnames[0]] = duration_in_mins(row, city)
            new_point[out_colnames[1]] = month
            new_point[out_colnames[2]] = hour
            new_point[out_colnames[3]] = day_of_week
            new_point[out_colnames[4]] = type_of_user(row, city)

            trip_writer.writerow(new_point)

    city_info = {'washington': {'in_file': './data/washington.csv',
                                'out_file': './data/washington-summary.csv'},
                 'chicago': {'in_file': './data/chicago.csv',
                             'out_file': './data/chicago-summary.csv'},
                 'new_york_city': {'in_file': './data/new_york_city.csv',
                                   'out_file': './data/new_york_city-summary.csv'}}
    for city, filenames in city_info.items():
        condense_data(filenames['in_file'], filenames['out_file'], city)
        print_first_point(filenames['out_file'])

data = ['trip_reader']
df = pd.DataFrame(data)

df.apply(pd.value_counts)

data = ['trip_reader']
df = pd.DataFrame(data)

df.month.value_counts().argmax()
df.day_of_week.value_counts().argmax()
df.hour.value_counts().argmax()

data_two = [city, "Start Station", "End Station"]
df = pd.DataFrame(data_two)

DataFrame(data_two).value_counts('Start Station').argmax('Start Station')
DataFrame(data_two).value_counts('End Station').argmax('End Station')

data = pd.read_csv("chicago.csv", "new_york_city.csv", "washington.csv", sep=',')
gps = data['Start Station','Trip Duration','End Station']
gps1 = gps.groupby('Start Station','End Station')

gps1 = gps1.count()
gps1.columns = ['count']
gps1.sort_values(['count'], ascending=True)
print(gps1)

def travel_time_stats(filename):
    df = pd.read_csv(filename)
    average = np.average(df['Trip Duration'])
    total_travel_time = 'Trip Duration'
    return average, total_travel_time

data = pd.read_csv("chicago.csv", "new_york_city.csv", sep = ',')
gender_and_birth = data('Gender', 'Birth Year')
df = pd.DataFrame(gender_and_birth)
DataFrame(gender_and_birth).apply(pd.value_counts)

print DataFrame(gender_and_birth).min('Birth Year')
print DataFrame(gender_and_birth).max('Birth Year')
print DataFrame(gender_and_birth).value_counts('Birth Year').argmax('Birth Year')
