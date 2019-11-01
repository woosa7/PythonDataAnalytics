# -------------------------------------------
# Which day of the week?

from datetime import date

# Create a date object
hurricane_andrew = date(1992, 8, 26)
print(hurricane_andrew.weekday())

# -------------------------------------------
# How many hurricanes come early?

print(len(florida_hurricane_dates))

# Counter for how many before June 1
early_hurricanes = 0
# We loop over the dates
for hurricane in florida_hurricane_dates:
    # Check if the month is before June (month number 6)
    if hurricane.month < 6:
        early_hurricanes = early_hurricanes + 1

print(early_hurricanes)

# -------------------------------------------
# Subtracting dates

from datetime import date

# Create a date object for May 9th, 2007
start = date(2007, 5, 9)
# Create a date object for December 13th, 2007
end = date(2007, 12, 13)
# Subtract the two dates and print the number of days
print((end - start).days)

# -------------------------------------------
# Counting events per calendar month

# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                         7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
    # Pull out the month
    month = hurricane.month
    # Increment the count in your dictionary by one
    hurricanes_each_month[month] += 1

print(hurricanes_each_month)

# -------------------------------------------
# Putting a list of dates in order

# Print the first and last scrambled dates
print(dates_scrambled[0])
print(dates_scrambled[-1])

# Put the dates in order
dates_ordered = sorted(dates_scrambled)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])

# -------------------------------------------
# Printing dates in a friendly format

# Assign the earliest date to first_date
first_date = florida_hurricane_dates[0]

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)

# -------------------------------------------
# Representing dates in different ways

from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))
print(andrew.strftime('%Y-%d'))

# -------------------------------------------
# Creating datetimes by hand

from datetime import datetime

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)
print(dt.isoformat())

# Replace the year with 1917
dt_old = dt.replace(year=1917)
print(dt_old)

# -------------------------------------------
# Counting events before and after noon

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
for trip in onebike_datetimes:
    # Check to see if the trip starts before noon
    if trip['start'].hour < 12:
        # Increment the counter for before noon
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon
        trip_counts['PM'] += 1

print(trip_counts)

# -------------------------------------------
# Turning strings into datetimes

# Import the datetime class
from datetime import datetime

# Starting string, in YYYY-MM-DD HH:MM:SS format
s = '2017-02-03 00:00:01'
fmt = '%Y-%m-%d %H:%M:%S'
d = datetime.strptime(s, fmt)
print(d)

# Starting string, in YYYY-MM-DD format
s = '2030-10-15'
fmt = '%Y-%m-%d'
d = datetime.strptime(s, fmt)
print(d)

# -------------------------------------------
# Parsing pairs of strings as datetimes

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# Loop over all trips
for (start, end) in onebike_datetime_strings:
    trip = {'start': datetime.strptime(start, fmt),
            'end': datetime.strptime(end, fmt)}

    # Append the trip
    onebike_datetimes.append(trip)

# -------------------------------------------
# Recreating ISO format with strftime()


# Import datetime
from datetime import datetime

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))

# -------------------------------------------
# Unix timestamps

from datetime import datetime

# Starting timestamps
timestamps = [1514665153, 1514664543]
# Datetime objects
dts = []

# Loop
for ts in timestamps:
    dts.append(datetime.fromtimestamp(ts))

print(dts)

# -------------------------------------------
# Turning pairs of datetimes into durations

print(onebike_datetimes[0])

# Initialize a list for all the trip durations
onebike_durations = []

for trip in onebike_datetimes:
    # Create a timedelta object corresponding to the length of the trip
    trip_duration = trip['end'] - trip['start']

    # Get the total elapsed seconds in trip_duration
    trip_length_seconds = trip_duration.total_seconds()

    # Append the results to our list
    onebike_durations.append(trip_length_seconds)

# -------------------------------------------
# Average trip time

# What was the total duration of all trips?
total_elapsed_time = sum(onebike_durations)

# What was the total number of trips?
number_of_trips = len(onebike_durations)

# Divide the total duration by the number of trips
print(total_elapsed_time / number_of_trips)

# -------------------------------------------
# The long and the short of why time is hard

# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)

# Print out the results
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")

# -------------------------------------------
# Creating timezone aware datetimes

from datetime import datetime, timezone, timedelta

UTC = timezone(timedelta(hours=0))
# October 1, 2017 at 15:26:26, UTC
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=UTC)
print(dt.isoformat())

# Create a timezone for Pacific Standard Time, or UTC-8
pst = timezone(timedelta(hours=-8))
# October 1, 2017 at 15:26:26, UTC-8
dt = datetime(2017, 10, 1, 15, 26, 26, tzinfo=pst)
print(dt.isoformat())

# -------------------------------------------
# Setting timezones

# Create a timezone object corresponding to UTC-4
edt = timezone(timedelta(hours=-4))

# Loop over trips, updating the start and end datetimes to be in UTC-4
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=edt)
    trip['end'] = trip['end'].replace(tzinfo=edt)

# -------------------------------------------
# What time did the bike leave in UTC?

# Loop over the trips
for trip in onebike_datetimes[:10]:
    # Pull out the start and set it to UTC
    dt = trip['start'].astimezone(timezone.utc)

    # Print the start time in UTC
    print('Original:', trip['start'], '| UTC:', dt.isoformat())

# -------------------------------------------
# Putting the bike trips into the right time zone

# Import tz
from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
for trip in onebike_datetimes[:10]:
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=et)
    trip['end'] = trip['end'].replace(tzinfo=et)

# -------------------------------------------
# What time did the bike leave? (Global edition)

# Create the timezone object
uk = tz.gettz('Europe/London')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in the UK?
notlocal = local.astimezone(uk)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# Create the timezone object
sm = tz.gettz('Pacific/Apia')

# Pull out the start of the first trip
local = onebike_datetimes[0]['start']

# What time was it in Samoa?
notlocal = local.astimezone(sm)

# Print them out and see the difference
print(local.isoformat())
print(notlocal.isoformat())

# -------------------------------------------
# Loading a csv file in Pandas

import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('capital-onebike.csv',
                    parse_dates=['Start date', 'End date'])

# Print the initial (0th) row
print(rides.iloc[0])

# -------------------------------------------
# Making timedelta columns

# Subtract the start date from the end date
ride_durations = rides['End date'] - rides['Start date']

# Convert the results to seconds
rides['Duration'] = ride_durations.dt.total_seconds()

print(rides['Duration'].head())

# -------------------------------------------
# How many joyrides?

# Create joyrides
joyrides = (rides['Start station'] == rides['End station'])

# Total number of joyrides
print("{} rides were joyrides".format(joyrides.sum()))

# Median of all rides
print("The median duration overall was {:.2f} seconds" \
      .format(rides['Duration'].median()))

# Median of joyrides
print("The median duration for joyrides was {:.2f} seconds" \
      .format(rides[joyrides]['Duration'].median()))

# -------------------------------------------
# It's getting cold outside, W20529

import matplotlib.pyplot as plt

# Resample rides to daily(D), take the size, plot the results
rides.resample('D', on='Start date') \
    .size() \
    .plot(ylim=[0, 15])
plt.show()

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='Start date') \
    .size() \
    .plot(ylim=[0, 150])
plt.show()

# -------------------------------------------
# Members vs casual riders over time

# Resample rides to be monthly on the basis of Start date
monthly_rides = rides.resample('M', on='Start date')['Member type']

print(monthly_rides.head())

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

# -------------------------------------------
# Combining groupby() and resample()

# Group rides by member type, and resample to the month
grouped = rides.groupby('Member type') \
    .resample('M', on='Start date')

# Print the median duration for each group
print(grouped['Duration'].median())

# -------------------------------------------
# Timezones in Pandas

# Localize the Start date column to America/New York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')
print(rides['Start date'].iloc[0])

# Localize the Start date column to America/New York
rides['Start date'] = rides['Start date'].dt.tz_localize('America/New_York', ambiguous='NaT')
print(rides['Start date'].iloc[0])

# Convert the Start date column to Europe/London
rides['Start date'] = rides['Start date'].dt.tz_convert('Europe/London')
print(rides['Start date'].iloc[0])

# -------------------------------------------
# How long per weekday?

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['Start date'].dt.weekday_name

# Print the median trip time per weekday
print(rides.groupby('Ride start weekday')['Duration'].median())

# -------------------------------------------
# How long between rides?

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['Start date'] - (rides['End date'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on='Start date')

# Print the average hours between rides each month
print(monthly['Time since'].mean() / (60 * 60))

# -------------------------------------------
