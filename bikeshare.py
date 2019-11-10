import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = city = input("Which city would you like to analyse: \'Chicago\', \'New york\', or \'Washington\'? ").lower()
    while city not in ['chicago', 'washington', 'new york']:
        city = input('Invalid input. Please enter either Chicago, New York, or Washington.').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    user_filter = input("How would you like to filter the Data: By Month, Day or all ").lower()
    while user_filter not in ['month', 'day','all']:
        user_filter = input("Invalid Filter Type..Please try typing month or day or all ").lower()

    if user_filter == 'month':
        day = 'all'
        month = input("Select a month from January to June ").lower()
        while month not in ['january', 'february', 'march', 'april', 'may', 'june']:
            month = input("Invalid month, please try again ").lower()

            # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif user_filter == 'day':
        month = 'all'
        day = input("Please enter day of week: ").title()
        while day.title() not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            day = input("Invalid input, please try again").title()

    elif user_filter == 'all':
        month = 'all'
        day = 'all'
        print('-'*40)
        return city, month, day


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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = months[(df['month'].mode()[0])-1]
    print("Most Common Month is: ", common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of the week is: ", common_day)

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print("Most Popular Hour is: ", popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station is: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most Common End Station is: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    full_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    frequent_full_trip = full_trip.value_counts().idxmax()
    print("Most Frequent Full Trip is: " , frequent_full_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total Travel Time is: ", travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of User Types: ", user_types)


    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    if gender.empty == True:
        print("no gender data")
    else:
        print("Gender count: ", gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    print("Earliest Year Of Birth: ", df['Birth Year'].min())
    print("Most Recent Year Of Birth: ", df['Birth Year'].max())
    print("Most Common Year Of Birth: ", df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays 5 rows of raw data upon user request."""
    start_count = 0
    end_count = 5
    data = input("Would you like to see raw data? Type (yes/no): ").lower()
    if data == 'yes':
        while end_count <= df.shape[0] - 1:
            print(df.iloc[start_count:end_count,:])
            start_count += 5
            end_count += 5
            more_data = input("Would you like to see more data?: ").lower()
            if more_data == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
