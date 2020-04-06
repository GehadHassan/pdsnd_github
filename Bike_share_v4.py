# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 07:13:09 2020

@author: Gehad
"""

import time
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 20)
pd.set_option('display.max_colwidth', 200)
pd.set_option('display.max_rows', 10)


CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new_york_city', 'washington' ]
months = ['all', 'January', 'February', 'March', 'April','May', 'June']
days = ['all', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saterday']

def get_filters():
    
    
    while True:
    
        city = input('Enter city name from the list {0}  :  '.format(cities)).lower()
    
        if city in cities:
            print('you selectd {0} city'.format(city))
            break

        else:
            print('invalid input.. Try again')
        
    
    
    while True:
        month = input('Enter month name or all from the list: {0}:'.format(months))
        if month in months:
            print('you selectd {0} as the month value '.format(month))
            break
        else:
            print('invalid input.. Try again')   
            
    while True:
        day = input('Enter day name or all from the list: {0}:'.format(days))
        if day in days:
            print('you selectd {0} as the day name '.format(day))
            break
        else:
            print('invalid input.. Try again') 
    
    return city,month,day
            

def load_data(city, month, day):
    
       
#    root_path = r'F:\Storm_drainage_desgin&Python&phdprep_2019\Learning_python\AAL_Scholarship\UDACITY\A-Programming_for_Data_Science_with_Python\D-Introduction_to_Python\Python_project'
        
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time']= pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
#    if (month == 'all' and day == 'all'):
#        print('Select all months and days')
#        df = df
#    elif (month == 'all' and day != 'all'):
#        print('Select all months and {0}'.format(day))
#        df = df[df['day'] == day]
#    elif (month != 'all' and day == 'all'):
#        print('Select {0} and all days'.format(month))
#        df = df[df['month'] == month]
#    else :
#        print('Select {0} and {1}'.format(month,day))
#        df = df[(df['month'] == month) & (df['day'] == day)]
    
    if month!='all':
        months=['January','February','March','April','May','June']
        month = months.index(month)+1
        df = df[df['month']==month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    print('-'*50)   
    return df

def raw_data(df):
    """Displays some rows of raw data."""

    print('\nDisplay raw data...\n')
    

    # display raw data?
    while True:
        
            ask = input('Do you like to show raw data? y or n:').lower()
                   
            if ask == 'y': 
                
                ask2 = input('How many raws do you like to view?')
                view_data = df.head(int(ask2))
                print(view_data)
            
            elif ask == 'n':
                              
                break

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    common_month = df['month'].mode()[0]
    print('common month is: {}' .format( common_month))

    # display the most common day of week
    common_day_of_week = df['day'].mode()[0]
    print('common_day_of_week is: {}' .format(common_day_of_week))
    
    # display the most common start hour
    
    common_hour = df['hour'].mode()[0]
    print('common_hour is: {}' .format (common_hour))
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*50)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('common_start_station is: {}' .format(common_start_station))
    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('common_end_station is: {}' .format(common_end_station))

#     display most frequent combination of start station and end station trip
    df['common Combination'] = df['Start Station']+' | | ' +df['End Station']
    frequent_combination =  df['common Combination'].value_counts().idxmax()
    print('frequent_combination is: {}'.format(frequent_combination))
    
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*50)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total_travel_time: {} sec' .format(total_travel_time))
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean_travel_time: {} sec' .format( mean_travel_time))
    
    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_user_type = df['User Type'].value_counts()
    print('counts_user_type: {}' .format(counts_user_type))
    # Display counts of gender
    if city == 'washington':
        print('No data available')
    else:
         gender_counts = df['Gender'].value_counts()
         print('gender_counts: {}' .format( gender_counts)) 
    
     
    # Display earliest, most recent, and most common year of birth
    
    if city == 'washington':
        print('No data available')
    else:
    
        earliest_yr = df['Birth Year'].min()
        print('earliest_yr: {}' .format( earliest_yr)) 
        
        recent_yr = df['Birth Year'].max()
        print('recent_yr: {}' .format( recent_yr))
            
        
        common_yr = df['Birth Year'].value_counts().idxmax()
        print('common_yr: {}' .format( common_yr))

    print("\nThis took %s seconds." % round((time.time() - start_time),2))
    print('-'*50)



#city, month, day = get_filters()
#df = load_data(city, month, day)
#print(df.head())
#time_stats(df)
#station_stats(df)
#trip_duration_stats(df)   
#user_stats(df)   


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    
    
    