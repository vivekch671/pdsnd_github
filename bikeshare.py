import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input=input("Please enter name of city from chicago, new york city, washington:").lower()
    while (city_input in {'chicago', 'new york city', 'washington'})== False:
        city_input=input("\nPlease enter valid city name from chicago, new york city, washington:").lower()

    return city_input

def get_month():
    # get user input for month (all, january, february, ... , june)
    month_input=input("Please enter the month by which you wish to filter (all or name of month \nbetween January to June:").lower()
    while (month_input in {'all','january', 'february', 'march','april','may','june'})== False:
        month_input=input("\nPlease enter valid month or all:").lower()

    return month_input

def get_day():
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_input=input("Please enter day by which you wish to filter (all or day of week):").lower()
    while (day_input in {'all','monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday'})== False:
        day_input=input("\nPlease enter valid weekday or all:").lower()

    return day_input
    print('-'*50)



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name

    if month!='all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
    if day!='all':

        df=df[df['day_of_week']==day.title()]

    df['Start Hour']=df['Start Time'].dt.hour
    df['Start-End Station combination']= df['Start Station']+"-"\
                +df['End Station']

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month=df['month'].mode()[0]
    print('\n Most common month: {}'.format(popular_month))

    # display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print('\n Most common day: {}'.format(popular_day))

    # display the most common start hour
    popular_hour=df['Start Hour'].mode()[0]
    print('\n Most common start hour: {}'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('\n Most commonly used start station: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]
    print('\n Most commonly used end station: {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    popular_station_comb= df['End Station'].mode()[0]
    print('\n Most frequent combination of start station and end station trip \: {}'.format(popular_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=np.sum(df['Trip Duration'])
    print('\nTotal travel time: {}'.format(total_travel_time))

    # display mean travel time
    mean_travel_time=np.mean(df['Trip Duration'])
    print('\nMean travel time: {}'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts=df.groupby(['User Type'])['User Type'].count()
    print('\nCount of users: \n{}'.format(user_counts))

    # Display counts of gender
    gender_counts=df['Gender'].value_counts()
    print('\nCount of gender: \n{}'.format(gender_counts))

    # Display earliest, most recent, and most common year of birth
    earliest_year=np.min(df['Birth Year'])
    recent_year=np.max(df['Birth Year'])
    common_year=df['Birth Year'].mode()[0]
    print('\nEarliest Birth Year: {} \nMost Recent Birth Year: {} \
    \nMost Common Year of Birth: {}'.format(earliest_year,recent_year,common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def main():
    while True:
        city = get_city()
        month = get_month()
        day = get_day()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:
            print("Gender data doesn't exist for Washington city")
            print('-'*40)
        display_data=input("\n Would you to like to see first 5 rows of data (Yes or No):")
        i=0
        while display_data.lower() == 'yes':
            print(df.iloc[i:i+5])
            i=i+5
            display_data=input("\n Would you to like to see next 5 rows of data (Yes or No):")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
