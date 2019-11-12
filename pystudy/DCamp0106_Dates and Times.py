"""
Working with Dates and Times
"""

# -------------------------------------------
# Which day of the week?

from datetime import date

# Create a date object
hurricane_andrew = date(1992, 8, 26)
print(hurricane_andrew.weekday())

# -------------------------------------------
# How many hurricanes come early?

import pickle

# list of the hurricanes that made landfall in Florida from 1950 to 2017
with open('data/chap01/florida_hurricane_dates.pkl', 'rb') as f:
    florida_hurricane_dates = pickle.load(f)

print(len(florida_hurricane_dates))

# Counter for how many before June 1
early_hurricanes = 0
for hurricane in florida_hurricane_dates:
    if hurricane.month < 6:
        early_hurricanes = early_hurricanes + 1

print(early_hurricanes)

# -------------------------------------------
# Subtracting dates

start = date(2007, 5, 9)
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
    month = hurricane.month
    hurricanes_each_month[month] += 1

print(hurricanes_each_month)

# -------------------------------------------
# Putting a list of dates in order

# Print the first and last scrambled dates
print(florida_hurricane_dates[0])
print(florida_hurricane_dates[-1])

# Put the dates in order
dates_ordered = sorted(florida_hurricane_dates)

print(dates_ordered[0])
print(dates_ordered[-1])

# -------------------------------------------
# Printing dates in a friendly format

first_date = florida_hurricane_dates[0]

# Convert to ISO and US formats
iso = "Our earliest hurricane date: " + first_date.isoformat()
us = "Our earliest hurricane date: " + first_date.strftime("%m/%d/%Y")

print("ISO: " + iso)
print("US: " + us)

# -------------------------------------------
# Representing dates in different ways

# Create a date object
andrew = date(1992, 8, 26)

print(andrew.strftime('%Y-%m-%d'))

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

import pandas as pd

df = pd.read_csv('data/chap01/capital-onebike.csv')
df = df[['start', 'end']]
df['start'] = pd.to_datetime(df['start'])
df['end'] = pd.to_datetime(df['end'])

onebike_datetimes = df[['start','end']]

# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

for i, trip in onebike_datetimes.iterrows():
    # Check to see if the trip starts before noon
    if trip.start.hour < 12:
        # Increment the counter for before noon
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon
        trip_counts['PM'] += 1

print(trip_counts)

# -------------------------------------------
# Turning strings into datetimes

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
# Recreating ISO format with strftime()

# Pull out the start of the first trip
first_start = onebike_datetimes['start'][0]

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))

# -------------------------------------------
# Unix timestamps

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

# Initialize a list for all the trip durations
onebike_durations = []

for i, trip in onebike_datetimes.iterrows():
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
print('Average trip time :', total_elapsed_time / number_of_trips)

# -------------------------------------------
# The long and the short of why time is hard

# Calculate shortest and longest trips
shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)
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
for i, trip in onebike_datetimes.iterrows():
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=edt)
    trip['end'] = trip['end'].replace(tzinfo=edt)

# -------------------------------------------
# Putting the bike trips into the right time zone

from dateutil import tz

# Create a timezone object for Eastern Time
et = tz.gettz('America/New_York')

# Loop over trips, updating the datetimes to be in Eastern Time
onebike_durations = []
for i, trip in onebike_datetimes.iterrows():
    # Update trip['start'] and trip['end']
    trip['start'] = trip['start'].replace(tzinfo=et)
    trip['end'] = trip['end'].replace(tzinfo=et)

    trip_duration = trip['end'] - trip['start']
    onebike_durations.append(trip_duration)

shortest_trip = min(onebike_durations)
longest_trip = max(onebike_durations)
print("The shortest trip was " + str(shortest_trip) + " seconds")
print("The longest trip was " + str(longest_trip) + " seconds")

# -------------------------------------------
# Loading a csv file in Pandas

import pandas as pd

# Load CSV into the rides variable
rides = pd.read_csv('data/chap01/capital-onebike.csv',
                    parse_dates=['start', 'end'])

print(rides.iloc[0])

# -------------------------------------------
# Making timedelta columns

# Subtract the start date from the end date
ride_durations = rides['end'] - rides['start']
rides['Duration'] = ride_durations.dt.total_seconds()
print(rides['Duration'].head())

# -------------------------------------------
# How many joyrides?

# Create joyrides
joyrides = (rides['start_station_no'] == rides['end_station_no'])
print("{} rides were joyrides".format(joyrides.sum()))

print("The median duration overall was {:.2f} seconds" \
      .format(rides['Duration'].median()))

print("The median duration for joyrides was {:.2f} seconds" \
      .format(rides[joyrides]['Duration'].median()))

# -------------------------------------------
# It's getting cold outside, W20529

import matplotlib.pyplot as plt

# Resample rides to daily(D), take the size, plot the results
rides.resample('D', on='start') \
    .size() \
    .plot(ylim=[0, 15])
plt.show()

# Resample rides to monthly, take the size, plot the results
rides.resample('M', on='start') \
    .size() \
    .plot(ylim=[0, 150])
plt.show()

# -------------------------------------------
# Members vs casual riders over time

# Resample rides to be monthly on the basis of start
monthly_rides = rides.resample('M', on='start')['type']

print(monthly_rides.head())

# Take the ratio of the .value_counts() over the total number of rides
print(monthly_rides.value_counts() / monthly_rides.size())

# -------------------------------------------
# Combining groupby() and resample()

# Group rides by member type, and resample to the month
grouped = rides.groupby('type').resample('M', on='start')

print(grouped['Duration'].median())

# -------------------------------------------
# Timezones in Pandas

# Localize the start column to America/New York
rides['start'] = rides['start'].dt.tz_localize('America/New_York', ambiguous='NaT')
rides['end'] = rides['end'].dt.tz_localize('America/New_York', ambiguous='NaT')
print(rides['start'].iloc[0])

# -------------------------------------------
# How long per weekday?

# Add a column for the weekday of the start of the ride
rides['Ride start weekday'] = rides['start'].dt.weekday_name

print(rides.groupby('Ride start weekday')['Duration'].median())

# -------------------------------------------
# How long between rides?

# Shift the index of the end date up one; now subract it from the start date
rides['Time since'] = rides['start'] - (rides['end'].shift(1))

# Move from a timedelta to a number of seconds, which is easier to work with
rides['Time since'] = rides['Time since'].dt.total_seconds()

# Resample to the month
monthly = rides.resample('M', on='start')

# Print the average hours between rides each month
print(monthly['Time since'].mean() / (60 * 60))

# -------------------------------------------
