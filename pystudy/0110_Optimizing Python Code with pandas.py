"""
Optimizing Python Code with pandas
"""
# -----------------------------------------------------------------
# 1. Selecting columns and rows efficiently
# -----------------------------------------------------------------
# Row selection: loc[] vs iloc[]

# Define the range of rows to select: row_nums
row_nums = range(0, 1000)

# Select the rows using .loc[] and row_nums and record the time before and after
loc_start_time = time.time()
rows = poker_hands.loc[row_nums]
loc_end_time = time.time()

# Print the time it took to select the rows using .loc
print("Time using .loc[]: {} sec".format(loc_end_time - loc_start_time))

# Select the rows using .iloc[] and row_nums and record the time before and after
iloc_start_time = time.time()
rows = poker_hands.iloc[row_nums]
iloc_end_time = time.time()

# Print the time it took to select the rows using .iloc
print("Time using .iloc[]: {} sec".format(iloc_end_time - iloc_start_time))

# iloc[] is more efficient

# -----------------------------------------------------------------
# Column selection: .iloc[] vs by name

# Use .iloc to select the first 6 columns and record the times before and after
iloc_start_time = time.time()
cols = poker_hands.iloc[:, 0:6]
iloc_end_time = time.time()

# Print the time it took
print("Time using .iloc[] : {} sec".format(iloc_end_time - iloc_start_time))

# Use simple column selection to select the first 6 columns
names_start_time = time.time()
cols = poker_hands[['S1', 'R1', 'S2', 'R2', 'S3', 'R3']]
names_end_time = time.time()

# Print the time it took
print("Time using selection by name : {} sec".format(names_end_time - names_start_time))

# Simple columns selection is more efficient

# -----------------------------------------------------------------
# Random row selection

# Extract number of rows in dataset
N = poker_hands.shape[0]

# Select and time the selection of the 75% of the dataset's rows
rand_start_time = time.time()
poker_hands.iloc[np.random.randint(low=0, high=N, size=int(0.75 * N))]
print("Time using Numpy: {} sec".format(time.time() - rand_start_time))

# Select and time the selection of the 75% of the dataset's rows using sample()
samp_start_time = time.time()
poker_hands.sample(int(0.75 * N), axis=0, replace=True)
print("Time using .sample: {} sec".format(time.time() - samp_start_time))

# sample() is more efficient


# -----------------------------------------------------------------
# 2. Replacing values in a DataFrame
# -----------------------------------------------------------------
# Replacing scalar values

# Replace all the entries that has 'FEMALE' as a gender with 'GIRL'
names['Gender'].loc[names['Gender'] == 'FEMALE'] = 'GIRL'

# efficient way
# Replace all the entries that has 'FEMALE' as a gender with 'GIRL'
names['Gender'].replace('FEMALE', 'GIRL', inplace=True)

# -----------------------------------------------------------------
# Replace values using lists

# Replace all non-Hispanic ethnicities with 'NON HISPANIC'
names['Ethnicity'].loc[(names["Ethnicity"] == 'BLACK NON HISP') |
                       (names["Ethnicity"] == 'BLACK NON HISPANIC') |
                       (names["Ethnicity"] == 'WHITE NON HISP') |
                       (names["Ethnicity"] == 'WHITE NON HISPANIC')] = 'NON HISPANIC'

# efficient way
# Replace all non-Hispanic ethnicities with 'NON HISPANIC'
names['Ethnicity'].replace(['BLACK NON HISP', 'BLACK NON HISPANIC', 'WHITE NON HISP', 'WHITE NON HISPANIC'],
                           'NON HISPANIC', inplace=True)

# -----------------------------------------------------------------
# Replace multiple values using list to list

names['Ethnicity'].replace(['ASIAN AND PACI', 'BLACK NON HISP', 'WHITE NON HISP'],
                           ['ASIAN AND PACIFIC ISLANDER', 'BLACK NON HISPANIC', 'WHITE NON HISPANIC'],
                           inplace=True)

# -----------------------------------------------------------------
# Replace values using dictionaries

# Replace string to string
poker_hands['Explanation'].replace({'Royal flush': 'Flush', 'Straight flush': 'Flush'}, inplace=True)
print(poker_hands['Explanation'].head())

# Replace the number by a string
names['Rank'].replace({1: 'FIRST', 2: 'SECOND', 3: 'THIRD'}, inplace=True)
print(names.head())

# -----------------------------------------------------------------
# Replace multiple values with just one value

# Replace the rank of the first three ranked names to 'MEDAL'
names.replace({'Rank': {1: 'MEDAL', 2: 'MEDAL', 3: 'MEDAL'}}, inplace=True)

# Replace the rank of the 4th and 5th ranked names to 'ALMOST MEDAL'
names.replace({'Rank': {4: 'ALMOST MEDAL', 5: 'ALMOST MEDAL'}}, inplace=True)
print(names.head())

# -----------------------------------------------------------------
# 3. Efficient iterating
# -----------------------------------------------------------------
# iterrows()

for index, values in poker_hands.iterrows():
    # Check if index is odd
    if index % 2 == 1:
        # Sum the ranks of all the cards
        hand_sum = sum([values[1], values[3], values[5], values[7], values[9]])

# -----------------------------------------------------------------
# apply() in every cell

# Define the lambda transformation
get_square = lambda x: x ** 2

# Apply the transformation
data_sum = poker_hands.apply(get_square)
print(data_sum.head())

# -----------------------------------------------------------------
# apply() for rows iteration

# Define the lambda transformation
get_variance = lambda x: np.var(x)

# Apply the transformation
data_tr = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].apply(get_variance, axis=1)
print(data_tr.head())

data_tr = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].apply(get_variance, axis=0)
print(data_tr.head())

# -----------------------------------------------------------------
# pandas vectorization

# Calculate the mean rank in each hand
row_start_time = time.time()
mean_r = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].mean(axis=1)
print("Time using pandas vectorization for rows: {} sec".format(time.time() - row_start_time))
print(mean_r.head())

# Calculate the mean rank of each of the 5 card in all hands
col_start_time = time.time()
mean_c = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].mean(axis=0)
print("Time using pandas vectorization for columns: {} sec".format(time.time() - col_start_time))
print(mean_c.head())

# -----------------------------------------------------------------
# Vectorization methods for looping a DataFrame

# Calculate the variance in each hand
start_time = time.time()
poker_var = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].var(axis=1)
print("Time using pandas vectorization: {} sec".format(time.time() - start_time))
print(poker_var.head())

# Calculate the variance in each hand
start_time = time.time()
poker_var = poker_hands[['R1', 'R2', 'R3', 'R4', 'R5']].values.var(axis=1, ddof=1)
print("Time using NumPy vectorization: {} sec".format(time.time() - start_time))
print(poker_var[0:5])

# -----------------------------------------------------------------
# 4. Data manipulation using groupby()
# -----------------------------------------------------------------
# min-max normalization using .transform()

# Define the min-max transformation
min_max_tr = lambda x: (x - x.min()) / (x.max() - x.min())

# Group the data according to the time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_min_max_group = restaurant_grouped.transform(min_max_tr)
print(restaurant_min_max_group.head())

# -----------------------------------------------------------------
# exponential transformation
# exponential distribution : e**(−λ∗x)∗λ
# λ (lambda) is the mean of the group that the observation x belongs to.

# Define the exponential transformation
exp_tr = lambda x: np.exp(-x.mean() * x) * x.mean()

# Group the data according to the time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_exp_group = restaurant_grouped['tip'].transform(exp_tr)
print(restaurant_exp_group.head())

# -----------------------------------------------------------------
# Validation of z-score normalization

zscore = lambda x: (x - x.mean()) / x.std()

# Apply the transformation
poker_trans = poker_grouped.transform(zscore)

# Re-group the grouped object and print each group's means and standard deviation
poker_regrouped = poker_trans.groupby(poker_hands['Class'])

print(np.round(poker_regrouped.mean(), 3))
print(poker_regrouped.std())

# -----------------------------------------------------------------
# Missing value imputation using transform()

# Identifying missing values
# erased by mistake the 'tips' in 65 tables

# Group both objects according to smoke condition
restaurant_nan_grouped = restaurant_nan.groupby('smoker')

# Store the number of present values
restaurant_nan_nval = restaurant_nan_grouped['tip'].count()

# Print the group-wise missing entries
print(restaurant_nan_grouped['total_bill'].count() - restaurant_nan_nval)

# -----------------------------------------------------------------
# Missing value imputation

# Define the lambda function
missing_trans = lambda x: x.fillna(x.median())

# Group the data according to time
restaurant_grouped = restaurant_data.groupby('time')

# Apply the transformation
restaurant_impute = restaurant_grouped.transform(missing_trans)
print(restaurant_impute.head())

# -----------------------------------------------------------------
# filter() function

# Filter the days where the count of total_bill is greater than $40
total_bill_40 = restaurant_data.groupby('day').filter(lambda x: x['total_bill'].count() > 40)

# Print the number of tables where total_bill is greater than $40
print('Number of tables where total_bill is greater than $40:', total_bill_40.shape[0])

# the mean amount of money the customers paid
# Select only the entries that have a mean total_bill greater than $20
total_bill_20 = total_bill_40.groupby('day').filter(lambda x: x['total_bill'].mean() > 20)

# Print days of the week that have a mean total_bill greater than $20
print('Days of the week that have a mean total_bill greater than $20:', total_bill_20.day.unique())

# -----------------------------------------------------------------
