"""
Robust Python Workflows
"""
import sys
from pprint import pprint

# -----------------------------------------------------------------
# 1. Python programming priciples
# -----------------------------------------------------------------
# DRY (Don't Repeat Yourself)

def read(filename):
    with open(filename, 'r') as file:
        return file.read()

# read 3 times
diabetes = read("data/diabetes.txt")
boston = read("data/boston.txt")
iris = read("data/iris.txt")


# --> list comprehension & unpack
filenames = ["data/diabetes.txt", "data/boston.txt", "data/iris.txt"]
diabetes, boston, iris = [read(f) for f in filenames]

# -----------------------------------------------------------------
# Using Standard library

from pathlib import Path

# list comprehension
diabetes, boston, iris = [Path(f).read_text() for f in filenames]

# generator expression
diabetes, boston, iris = (Path(f).read_text() for f in filenames)

# -----------------------------------------------------------------
# Find matches

def get_matches(filename, query):
    # Filter the list comprehension using an if clause
    return [line for line in Path(filename).open() if query in line]

# Iterate over files to find all matching lines
matches = [get_matches(name, "Number of") for name in filenames]
pprint(matches)

# -----------------------------------------------------------------
# Extract words

def obtain_words(string):
    # Replace non-alphabetic characters with spaces
    return "".join(char if char.isalpha() else " " for char in string).split()

def filter_words(words, minimum_length=5):
    # Remove words shorter than 5 characters
    return [word for word in words if len(word) >= minimum_length]

words = obtain_words(Path("data/diabetes.txt").read_text().lower())
filtered_words = filter_words(words, 3)
pprint(filtered_words)

# -----------------------------------------------------------------
# Most frequent words

import matplotlib.pyplot as plt
import pandas as pd

def count_words(word_list):
    # Count the words in the input list
    return {word: word_list.count(word) for word in word_list}

# Create the dictionary of words and word counts
word_count_dictionary = count_words(filtered_words)
print(word_count_dictionary)

(pd.DataFrame(word_count_dictionary.items())
 .sort_values(by=1, ascending=False)
 .head()
 .plot(x=0, kind="barh", xticks=range(5), legend=False)
 .set_ylabel("")
)
plt.show()


# -----------------------------------------------------------------
# 2. Documentation & test
# 3. Shell superpowers
# 4. Projects, pipelines and parallelism
# -----------------------------------------------------------------

# ---> Skip

# -----------------------------------------------------------------
