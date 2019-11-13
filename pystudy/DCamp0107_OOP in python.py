"""
Object-Oriented Programming in Python
"""
import sys

# -------------------------------------------
# Object: Instance of a Class

# Create class & Init Method
class DataShell:

    # Initialize class with self argument
    def __init__(self):
        pass


# Instantiate DataShell
my_data_shell = DataShell()
print(my_data_shell)

# -------------------------------------------
# Instance Variables

class DataShell:

    # Initialize class with self, identifier and data arguments
    def __init__(self, identifier, data):
        # Set identifier and data as instance variables, assigning value of input arguments
        self.identifier = identifier
        self.data = data


x = 100
y = [1, 2, 3, 4, 5]

# Instantiate DataShell passing x and y as arguments
my_data_shell = DataShell(x, y)

print(my_data_shell.identifier)
print(my_data_shell.data)

# -------------------------------------------
# Class Variables

class DataShell:
    # Declare a class variable family, and assign value of "DataShell"
    family = 'DataShell'

    def __init__(self, identifier):
        self.identifier = identifier


x = 100
my_data_shell = DataShell(x)

# Print my_data_shell class variable family
print(my_data_shell.family)

# -------------------------------------------
# Overriding Class Variables

class DataShell:
    # Declare a class variable family
    family = 'DataShell'

    def __init__(self, identifier):
        self.identifier = identifier


x = 100
my_data_shell = DataShell(x)

# Print my_data_shell class variable family
print(my_data_shell.family)

# Override the my_data_shell.family value with "NotDataShell"
my_data_shell.family = 'NotDataShell'
print(my_data_shell.family)

# -------------------------------------------
# Methods I

class DataShell:

    def __init__(self):
        pass

    # Define class method which takes self argument
    def print_static(self):
        print("You just executed a class method!")


my_data_shell = DataShell()
my_data_shell.print_static()

# -------------------------------------------
# Methods II

class DataShell:

    def __init__(self, dataList):
        self.data = dataList

    # Define method that prints data
    def show(self):
        print(self.data)

    # Define method that prints average of data
    def avg(self):
        avg = sum(self.data) / float(len(self.data))
        print(avg)


integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_data_shell = DataShell(integer_list)

my_data_shell.show()
my_data_shell.avg()

# -------------------------------------------
# Return Statement

class DataShell:

    def __init__(self, dataList):
        self.data = dataList

    def show(self):
        return self.data

    def avg(self):
        avg = sum(self.data) / float(len(self.data))
        return avg


my_data_shell = DataShell(integer_list)

print(my_data_shell.show())
print(my_data_shell.avg())

# -------------------------------------------
# Return Statement: A More Powerful DataShell

import numpy as np
import pandas as pd

class DataShell:

    def __init__(self, inputFile):
        self.file = inputFile

    def generate_csv(self):
        self.data_as_csv = pd.read_csv(self.file)
        return self.data_as_csv


us_life_exp = 'data/chap01/us_life_expectancy.csv'

data_shell = DataShell(us_life_exp)

df = data_shell.generate_csv()
print(df)

# -------------------------------------------
# Data as Attributes

class DataShell:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)


us_data_shell = DataShell(us_life_exp)
print(us_data_shell.data_as_csv)

# -------------------------------------------
# Renaming Columns

class DataShell:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)

    # Define method rename_column, with arguments self, column_name, and new_column_name
    def rename_column(self, column_name, new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name, new_column_name)


us_data_shell = DataShell(us_life_exp)
print(us_data_shell.data_as_csv.dtypes)

# Rename your objects column 'code' to 'country_code'
us_data_shell.rename_column('code', 'country_code')
print(us_data_shell.data_as_csv.dtypes)

# -------------------------------------------
# Self-Describing DataShells

class DataShell:

    def __init__(self, filepath):
        self.filepath = filepath
        self.data_as_csv = pd.read_csv(filepath)

    def rename_column(self, column_name, new_column_name):
        self.data_as_csv.columns = self.data_as_csv.columns.str.replace(column_name, new_column_name)

    def get_stats(self):
        # Return a description data_as_csv
        return self.data_as_csv.describe()


us_data_shell = DataShell(us_life_exp)
print(us_data_shell.get_stats())

# -------------------------------------------
# Animal Inheritance

# Create a class Animal
class Vertebrate:
    spinal_cord = True
    def __init__(self, name):
        self.name = name


# Create a class Mammal, which inherits from Vertebrate
class Mammal(Vertebrate):
    def __init__(self, name, animal_type):
        self.animal_type = animal_type
        self.temperature_regulation = True


# Create a class Reptile, which also inherits from Vertebrate
class Reptile(Vertebrate):
    def __init__(self, name, animal_type):
        self.animal_type = animal_type
        self.temperature_regulation = False


daisy = Mammal('Daisy', 'dog')
stella = Reptile('Stella', 'alligator')

print("Stella Spinal cord: " + str(stella.spinal_cord))
print("Stella temperature regulation: " + str(stella.temperature_regulation))

print("Daisy Spinal cord: " + str(daisy.spinal_cord))
print("Daisy temperature regulation: " + str(daisy.temperature_regulation))

# -------------------------------------------
# Abstract Class

class DataShell:
    def __init__(self, inputFile):
        self.file = inputFile


# Create class CsvDataShell, which inherits from DataShell
class CsvDataShell(DataShell):
    def __init__(self, inputFile):
        # Instance variable data
        self.data = pd.read_csv(inputFile)


my_data_shell = DataShell(us_life_exp)
print(my_data_shell)

us_data_shell = CsvDataShell(us_life_exp)
print(us_data_shell.data)

# -------------------------------------------
# Composition and Inheritance

class DataShell:
    # class variable
    family = 'DataShell'

    def __init__(self, name, filepath):
        self.name = name
        self.filepath = filepath


# Define class CsvDataShell
class CsvDataShell(DataShell):
    def __init__(self, name, filepath):
        self.data = pd.read_csv(filepath)
        self.stats = self.data.describe()


# Define class TsvDataShell
class TsvDataShell(DataShell):
    def __init__(self, name, filepath):
        self.data = pd.read_table(filepath)
        self.stats = self.data.describe()


us_data_shell = CsvDataShell("US", us_life_exp)
print(us_data_shell.stats)

france_life_exp = 'data/chap01/france_life_expectancy.csv'

france_data_shell = TsvDataShell('France', france_life_exp)
print(france_data_shell.stats)

# -------------------------------------------
