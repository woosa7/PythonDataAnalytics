"""
Streamlined Data Ingestion with pandas
"""

# -----------------------------------------------------------------
# 1. Importing Data from Flat Files
# -----------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/chap02/vt_tax_data_2016.csv')
print(data.head())

# tax returns by income level
print(data.groupby("agi_stub").sum())

# the total number of tax returns by income level
counts = data.groupby("agi_stub").N1.sum()
print(counts)
counts.plot.bar()
plt.show()

# -----------------------------------------------------------------
# Specifying Data Types

# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub': 'category',
              'zipcode': str}

data = pd.read_csv("data/chap02/vt_tax_data_2016.csv", dtype=data_types)

print(data.dtypes.head())

# -----------------------------------------------------------------
# Missing data

# specifying that 0 in zipcode are NA values (0 --> NA)
null_values = {'zipcode': 0}

data = pd.read_csv("data/chap02/vt_tax_data_2016.csv", na_values=null_values)

print(data[data.zipcode.isna()])

# -----------------------------------------------------------------
# Lines with errors

try:
    # Set warn_bad_lines to issue warnings about bad records
    data = pd.read_csv("data/chap02/vt_tax_data_2016_corrupt.csv",
                       error_bad_lines=False,
                       warn_bad_lines=True)

    print(data.head())

except:
    print("Your data contained rows that could not be parsed.")

# -----------------------------------------------------------------
# 2. Importing Data from Excel Files
# -----------------------------------------------------------------
survey_responses = pd.read_excel("data/chap02/fcc_survey.xlsx")

print(survey_responses.head())

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("data/chap02/fcc_survey.xlsx",
                                 skiprows=2,
                                 usecols='AD,AW:BA')

print(survey_responses.columns)

# -----------------------------------------------------------------
# Select a single sheet

# index
responses_2017 = pd.read_excel("data/chap02/fcc_survey.xlsx",
                               sheet_name=1)

# name
responses_2017 = pd.read_excel("data/chap02/fcc_survey.xlsx",
                               sheet_name='2017',
                               skiprows=2)

job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# -----------------------------------------------------------------
# Select multiple sheets

# Load both the 2016 and 2017 sheets by name
all_survey_data = pd.read_excel("data/chap02/fcc_survey.xlsx",
                                sheet_name=['2016', '2017'])

# all sheets
all_survey_data = pd.read_excel("data/chap02/fcc_survey.xlsx",
                                sheet_name=None,
                                skiprows=2)

print(type(all_survey_data))
print(all_survey_data.keys())

# -----------------------------------------------------------------
# Combine

# Create an empty data frame
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in all_survey_data.values():
    # Print the number of rows being added
    print("Adding {} rows".format(df.shape[0]))
    # Append df to all_responses, assign result
    all_responses = all_responses.append(df)

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

# -----------------------------------------------------------------
# Set Boolean columns

survey_data = pd.read_excel("data/chap02/fcc_survey_subset.xlsx")

# Count NA values in each column
print(survey_data.isna().sum())

# Set dtype to load appropriate column(s) as Boolean data
survey_data = pd.read_excel("data/chap02/fcc_survey_subset.xlsx",
                            dtype={'HasDebt': bool})

# View financial burdens by Boolean group
print(survey_data.groupby('HasDebt').sum())

# -----------------------------------------------------------------
# Get datetimes from multiple columns

survey_data = pd.read_excel("data/chap02/fcc_survey.xlsx",
                            parse_dates=["Part1StartTime"],
                            skiprows=2)

print(survey_data.Part1StartTime.head())

"""
# 날짜와 시간이 분리되어 있는 경우

datetime_cols = {"Part2Start": ["Part2StartDate", "Part2StartTime"]}

survey_data = pd.read_excel("data/chap02/fcc_survey.xlsx",
                            parse_dates=datetime_cols,
                            skiprows=2)
"""

# -----------------------------------------------------------------
# Parse non-standard date formats

survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"], format="%Y%m%d %H:%M:%S")

# -----------------------------------------------------------------
# 3. Importing Data from Database
# -----------------------------------------------------------------
# Connect to database

from sqlalchemy import create_engine

# Create the database engine
engine = create_engine("sqlite:///data/chap02/nyc_weather.db")

print(engine.table_names())

# -----------------------------------------------------------------
# Load entire tables

# Load pd311calls without any SQL
hpd_calls = pd.read_sql("hpd311calls", engine)

print(hpd_calls.head())

# Create a SQL query to load the entire weather table
query = """
SELECT *
  FROM weather;
"""
# Load weather with the SQL query
weather = pd.read_sql(query, engine)

print(weather.head())

# -----------------------------------------------------------------
# Selecting columns with SQL

# Write query to get date, tmax, and tmin from weather
query = """
SELECT date,
       tmax,
       tmin
  FROM weather;
"""

# Make a data frame by passing query and engine to read_sql()
temperatures = pd.read_sql(query, engine)

print(temperatures)

# -----------------------------------------------------------------
# Create query to get hpd311calls records about safety
query = """SELECT *
		     FROM hpd311calls
            WHERE complaint_type = 'SAFETY';"""

safety_calls = pd.read_sql(query, engine)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()

# -----------------------------------------------------------------
# Getting distinct values

# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough,
       complaint_type
  FROM hpd311calls;
"""

# Load results of query to a data frame
issues_and_boros = pd.read_sql(query, engine)

print(issues_and_boros)

# -----------------------------------------------------------------
# Counting in groups

# Create query to get call counts by complaint_type
query = """
SELECT complaint_type,
       COUNT(*)
  FROM hpd311calls
 GROUP BY complaint_type;
"""

# Create data frame of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

calls_by_issue.plot.barh(x="complaint_type")
plt.show()

# -----------------------------------------------------------------
# aggregate functions

# Create a query to get month and max tmax by month
query = """
SELECT month,
       MAX(tmax),
       MIN(tmin),
       SUM(prcp)
  FROM weather
 GROUP BY month;"""

# Get data frame of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

print(weather_by_month)

# -----------------------------------------------------------------
# Joining tables

# Query to join weather to call records by date columns
query = """
SELECT *
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date;
"""

# Create data frame of joined tables
calls_with_weather = pd.read_sql(query, engine)

print(calls_with_weather.head())

# -----------------------------------------------------------------
# Joining and filtering

# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
 WHERE hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls data frame
leak_calls = pd.read_sql(query, engine)

print(leak_calls.head())

# -----------------------------------------------------------------
# 4. Importing JSON Data and Working with APIs
# -----------------------------------------------------------------
# Load JSON data

import json

# string
with open('data/chap02/dhs_daily_report.json') as json_data:
    jsonString = json.load(json_data)
    print(jsonString)

# DataFrame
# The New York City Department of Homeless Services Daily Report
pop_in_shelters = pd.read_json("data/chap02/dhs_daily_report.json")

print(pop_in_shelters.info())

# -----------------------------------------------------------------
# Work with JSON orientations
# split by columns, index, data

try:
    df = pd.read_json("data/chap02/dhs_report_splitted.json",
                      orient="split")

    # Plot total population in shelters over time
    df["date_of_census"] = pd.to_datetime(df["date_of_census"])
    df.plot(x="date_of_census",
            y="total_individuals_in_shelter")
    plt.show()

except ValueError:
    print("pandas could not parse the JSON.")

# -----------------------------------------------------------------
# Yelp Business Search API
import requests

# need the API Key
api_url = "https://api.yelp.com/v3/businesses/search"
headers = {
    'Authorization': 'Bearer mhmt6jn3SFPVC1u6pfwgHWQvsa1wmWvCpKRtFGRYlo4mzA14SisQiDjyygsGMV2Dm7tEsuwdC4TYSA0Ai_GQTjKf9d5s5XLSNfQqdg1oy7jcBBh1i7iQUZBujdA_XHYx'}
params = {'term': 'cafe', 'location': 'NYC'}

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url,
                        headers=headers,
                        params=params)

# Extract JSON data from the response
data = response.json()
cafes = pd.DataFrame(data)

print(cafes.dtypes)
print(cafes.head())

# -----------------------------------------------------------------
# Flatten nested JSONs
# flattened data nested down one level.

from pandas.io.json import json_normalize

data = response.json()

# Flatten business data into a data frame, replace separator
cafes = json_normalize(data["businesses"],
                       sep="_")

# View data
print(cafes.head())

# -----------------------------------------------------------------
# skip

# Handle deeply nested data

# Combining multiple datasets

# Append & Merge DataFrame

# -----------------------------------------------------------------
