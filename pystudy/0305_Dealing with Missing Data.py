"""
Dealing with Missing Data
"""

# -----------------------------------------------------------------
# 1. The Problem With Missing Data
# -----------------------------------------------------------------
# Detecting missing values

college = pd.read_csv('college.csv')
print(college.head())
print(college.info())

# Store unique values of 'csat' column to 'csat_unique'
csat_unique = college.csat.unique()
print(np.sort(csat_unique))

college = pd.read_csv('college.csv', na_values='.')
print(college.head())
print(college.info())

# -----------------------------------------------------------------
# Replacing hidden missing values

print(diabetes.describe())

# Store all rows of column 'BMI' which are equal to 0
zero_bmi = diabetes.BMI[diabetes.BMI == 0]
print(zero_bmi)

# Set the 0 values of column 'BMI' to np.nan
diabetes.BMI[diabetes.BMI == 0] = np.nan

print(diabetes.BMI[np.isnan(diabetes.BMI)])

# -----------------------------------------------------------------
# Analyzing missingness percentage

# Load the airquality dataset
airquality = pd.read_csv('air-quality.csv', parse_dates=['Date'], index_col='Date')

# Create a nullity DataFrame airquality_nullity
airquality_nullity = airquality.isnull()
print(airquality_nullity.head())

# Calculate total of missing values
missing_values_sum = airquality_nullity.sum()
print('Total Missing Values:\n', missing_values_sum)

# Calculate percentage of missing values
missing_values_percent = airquality_nullity.mean() * 100
print('Percentage of Missing Values:\n', missing_values_percent)

# -----------------------------------------------------------------
# Visualize missingness

import missingno as msno

# Plot amount of missingness
msno.bar(airquality)
plt.show()
# display("/usr/local/share/datasets/bar_chart.png")

# Plot nullity matrix of airquality
msno.matrix(airquality)
plt.show()

# Plot nullity matrix of airquality with frequency 'M'
msno.matrix(airquality, freq='M')
plt.show()

# Plot the sliced nullity matrix of airquality with frequency 'M'
msno.matrix(airquality.loc['May-1976': 'Jul-1976'], freq='M')
plt.show()

# -----------------------------------------------------------------
# 2. Does Missingness Have A Pattern?

# Types of missingness
# 1. Missing Completely at Random (MCAR)
# 2. Missing at Random (MAR)
# 3. Missing Not at Random (MNAR)

# -----------------------------------------------------------------
# Guess the missingness type

msno.matrix(diabetes)  # Serum_Insulin is missing at random.
plt.show()

# Sort diabetes dataframe on 'Serum_Insulin'
sorted_values = diabetes.sort_values('Serum_Insulin')
msno.matrix(sorted_values)
plt.show()

# -----------------------------------------------------------------
# Finding correlations in your data

# Plot missingness heatmap of diabetes
msno.heatmap(diabetes)
# Plot missingness dendrogram of diabetes
msno.dendrogram(diabetes)
plt.show()


# ---> Skin_Fold is MNAR

# -----------------------------------------------------------------
# Fill dummy values

def fill_dummy_values(df):
    df_dummy = df.copy(deep=True)
    for col in df_dummy:
        col = df_dummy[col]
        col_null = col.isnull()
        # Calculate number of missing values in column
        num_nulls = col_null.sum()
        # Calculate column range
        col_range = col.max() - col.min()
        # Scale the random values to scaling_factor times col_range
        dummy_values = (rand(num_nulls) - 2) * scaling_factor * col_range + col.min()
        col[col_null] = dummy_values

    return df_dummy


# -----------------------------------------------------------------
# Generate scatter plot with missingness

# Fill dummy values in diabetes_dummy
diabetes_dummy = fill_dummy_values(diabetes)

# Sum the nullity of Skin_Fold and BMI
nullity = diabetes['Skin_Fold'].isnull() + diabetes['BMI'].isnull()

# Create a scatter plot of Skin Fold and BMI
diabetes_dummy.plot(x='Skin_Fold', y='BMI', kind='scatter', alpha=0.5,
                    # Set color to nullity of BMI and Skin_Fold
                    c=nullity,
                    cmap='rainbow')
plt.show()

# -----------------------------------------------------------------
# Delete MCAR

# Visualize the missingness of diabetes pre-dropping missing values
msno.matrix(diabetes)

# Print the number of missing values in Glucose
print(diabetes['Glucose'].isnull().sum())

# Drop all rows where 'Glucose' has a missing value
diabetes.dropna(subset=['Glucose'], how='all', inplace=True)

# Visualize the missingness of diabetes after-dropping missing values
msno.matrix(diabetes)

# -----------------------------------------------------------------
# Will you delete?

# Visualize the missingness in the data
msno.matrix(diabetes)
# Visualize the correlation of missingness between variables
msno.heatmap(diabetes)
plt.show()

# --> BMI values are Missing Completely at Random(MCAR).
#     Therefore, we should delete it.

# Drop rows where 'BMI' has a missing value
diabetes.dropna(subset=['BMI'], how='all', inplace=True)

# -----------------------------------------------------------------
# 3. Imputation Techniques
# -----------------------------------------------------------------
# Mean & median imputation

# Create mean imputer object
diabetes_mean = diabetes.copy(deep=True)
mean_imputer = SimpleImputer(strategy='mean')
diabetes_mean.iloc[:, :] = mean_imputer.fit_transform(diabetes_mean)

# others
median_imputer = SimpleImputer(strategy='median')
mode_imputer = SimpleImputer(strategy="most_frequent")
constant_imputer = SimpleImputer(strategy="constant", fill_value=0)

# -----------------------------------------------------------------
# Visualize imputations

# Set nrows and ncols to 2
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
nullity = diabetes.Serum_Insulin.isnull() + diabetes.Glucose.isnull()

# Create a dictionary of imputations
imputations = {'Mean Imputation': diabetes_mean, 'Median Imputation': diabetes_median,
               'Most Frequent Imputation': diabetes_mode, 'Constant Imputation': diabetes_constant}

# Loop over flattened axes and imputations
for ax, df_key in zip(axes.flatten(), imputations):
    # Select and also set the title for a DataFrame
    imputations[df_key].plot(x='Serum_Insulin', y='Glucose', kind='scatter',
                             alpha=0.5, c=nullity, cmap='rainbow', ax=ax,
                             colorbar=False, title=df_key)
plt.show()

# -----------------------------------------------------------------
# Filling missing time-series data

# Print prior to imputing missing values
print(airquality[30:40])

# Fill NaNs using forward fill
airquality.fillna(method='ffill', inplace=True)
print(airquality[30:40])

# Fill NaNs using backward fill
airquality.fillna(method='bfill', inplace=True)
print(airquality[30:40])

# -----------------------------------------------------------------
# Impute with interpolate method

# Interpolate the NaNs linearly
airquality.interpolate(method='linear', inplace=True)
# Interpolate the NaNs quadratically
airquality.interpolate(method='quadratic', inplace=True)
# Interpolate the NaNs with nearest value
airquality.interpolate(method='nearest', inplace=True)

# -----------------------------------------------------------------
# Visualize forward fill imputation

# Impute airquality DataFrame with ffill method
ffill_imputed = airquality.fillna(method='ffill')

# Plot the imputed DataFrame ffill_imp in red dotted style
ffill_imputed['Ozone'].plot(color='red', marker='o', linestyle='dotted', figsize=(30, 5))

# Plot the airquality DataFrame with title
airquality['Ozone'].plot(title='Ozone', marker='o', figsize=(30, 5))
plt.show()

# -----------------------------------------------------------------
# Visualize backward fill imputation

# Impute airquality DataFrame with bfill method
bfill_imputed = airquality.fillna(method='bfill')

# Plot the imputed DataFrame bfill_imp in red dotted style
bfill_imputed['Ozone'].plot(color='red', marker='o', linestyle='dotted', figsize=(30, 5))

# Plot the airquality DataFrame with title
airquality['Ozone'].plot(title='Ozone', marker='o', figsize=(30, 5))
plt.show()

# -----------------------------------------------------------------
# Plot interpolations

# Set nrows to 3 and ncols to 1
fig, axes = plt.subplots(3, 1, figsize=(30, 20))

# Create a dictionary of interpolations
interpolations = {'Linear Interpolation': linear, 'Quadratic Interpolation': quadratic,
                  'Nearest Interpolation': nearest}

# Loop over axes and interpolations
for ax, df_key in zip(axes, interpolations):
    # Select and also set the title for a DataFrame
    interpolations[df_key].Ozone.plot(color='red', marker='o', linestyle='dotted', ax=ax)
    airquality.Ozone.plot(title=df_key + ' - Ozone', marker='o', ax=ax)

plt.show()

# -----------------------------------------------------------------
# 4. Advanced Imputation Techniques
# -----------------------------------------------------------------
# KNN imputation

# https://github.com/iskandr/fancyimpute
from fancyimpute import KNN

# Copy diabetes to diabetes_knn_imputed
diabetes_knn_imputed = diabetes.copy(deep=True)

# Initialize KNN
knn_imputer = KNN()

# Impute using fit_tranform on diabetes
diabetes_knn_imputed.iloc[:, :] = knn_imputer.fit_transform(diabetes)

# -----------------------------------------------------------------
# MICE imputation

from fancyimpute import IterativeImputer

# Copy diabetes to diabetes_mice_imputed
diabetes_mice_imputed = diabetes.copy(deep=True)

# Initialize IterativeImputer
mice_imputer = IterativeImputer()

# Impute using fit_tranform on diabetes
diabetes_mice_imputed.iloc[:, :] = mice_imputer.fit_transform(diabetes)

# -----------------------------------------------------------------
# Imputing categorical values

# Ordinal encoding of a categorical column
ambience_ord_enc = OrdinalEncoder()

# Select non-null values of ambience column in users
ambience = users['ambience']
ambience_not_null = ambience[ambience.notnull()]

# Reshape ambience_not_null to shape (-1, 1)
reshaped_vals = ambience_not_null.values.reshape(-1, 1)

# Ordinally encode reshaped_vals
encoded_vals = ambience_ord_enc.fit_transform(reshaped_vals)

# Assign back encoded values to non-null values of ambience in users
users.loc[ambience.notnull(), 'ambience'] = np.squeeze(encoded_vals)

# -----------------------------------------------------------------
# Ordinal encoding of a DataFrame

# Create an empty dictionary ordinal_enc_dict
ordinal_enc_dict = {}

for col_name in users:
    # Create Ordinal encoder for col
    ordinal_enc_dict[col_name] = OrdinalEncoder()
    col = users[col_name]

    # Select non-null values of col in users
    col_not_null = col[col.notnull()]
    reshaped_vals = col_not_null.values.reshape(-1, 1)
    encoded_vals = ordinal_enc_dict[col_name].fit_transform(reshaped_vals)

    # Store the values to column in users
    users.loc[col.notnull(), col_name] = np.squeeze(encoded_vals)

# -----------------------------------------------------------------
# KNN imputation of categorical values

# Create KNN imputer
KNN_imputer = KNN()

# Impute and round the users DataFrame
users.iloc[:, :] = np.round(KNN_imputer.fit_transform(users))

# Loop over the column names in users
for col_name in users:
    # Reshape the data
    reshaped = users[col_name].values.reshape(-1, 1)

    # Perform inverse transform of the ordinally encoded columns
    users[col_name] = ordinal_enc_dict[col_name].inverse_transform(reshaped)

# -----------------------------------------------------------------
# Evaluation of different imputation techniques

import statsmodels.api as sm

# linear model
X = sm.add_constant(diabetes_cc.iloc[:, :-1])
y = diabetes_cc['Class']
lm = sm.OLS(y, X).fit()

# Print summary of lm
print('\nSummary: ', lm.summary())

# Print R squared score of lm
print('\nAdjusted R-squared score: ', lm.rsquared_adj)

# Print the params of lm
print('\nCoefficcients:\n', lm.params)

# -----------------------------------------------------------------
# Comparing R-squared and coefficients

r_squared = pd.DataFrame({'Complete Case': lm.rsquared_adj,
                          'Mean Imputation': lm_mean.rsquared_adj,
                          'KNN Imputation': lm_KNN.rsquared_adj,
                          'MICE Imputation': lm_MICE.rsquared_adj},
                         index=['Adj. R-squared'])

print(r_squared)

coeff = pd.DataFrame({'Complete Case': lm.params,
                      'Mean Imputation': lm_mean.params,
                      'KNN Imputation': lm_KNN.params,
                      'MICE Imputation': lm_MICE.params})

print(coeff)

# -----------------------------------------------------------------
# Comparing density plots

# Plot graphs of imputed DataFrames and the complete case
diabetes_cc['Skin_Fold'].plot(kind='kde', c='red', linewidth=3)
diabetes_mean_imputed['Skin_Fold'].plot(kind='kde')
diabetes_knn_imputed['Skin_Fold'].plot(kind='kde')
diabetes_mice_imputed['Skin_Fold'].plot(kind='kde')

# Create labels for the four DataFrames
labels = ['Baseline (Complete Case)', 'Mean Imputation', 'KNN Imputation', 'MICE Imputation']
plt.legend(labels)
plt.xlabel('Skin Fold')
plt.show()

# -----------------------------------------------------------------
