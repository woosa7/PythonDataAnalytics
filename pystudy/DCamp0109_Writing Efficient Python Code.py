"""
Writing Efficient Python Code
"""

import warnings

warnings.filterwarnings(action='ignore')


"""
1. Foundations for efficiencies
"""
# -------------------------------------------
# Looping over a list

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']

# Non-Pythonic approach
i = 0
new_list= []
while i < len(names):
    if len(names[i]) >= 6:
        new_list.append(names[i])
    i += 1


# better way
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)


# list comprehension
best_list = [name for name in names if len(name) >= 6]
print(best_list)


# -------------------------------------------
# range()

# Create a range object that goes from 0 to 5
nums = range(6)
print(type(nums))   # range object

# Convert nums to a list
nums_list = list(nums)
print(nums_list)

# Create a new list of odd numbers from 1 to 11 by unpacking a range object
nums_list2 = [*range(1,12,2)]
print(nums_list2)


# -------------------------------------------
# enumerate()

# Rewrite the for loop to use enumerate
indexed_names = []
for i,name in enumerate(names):
    index_name = (i,name)
    indexed_names.append(index_name)
print(indexed_names)

# Rewrite the above for loop using list comprehension
indexed_names_comp = [(i,name) for i,name in enumerate(names)]
print(indexed_names_comp)

# Unpack an enumerate object with a starting index of one
indexed_names_unpack = [*enumerate(names, 1)]
print(indexed_names_unpack)


# -------------------------------------------
# map()

# Use map to apply str.upper to each element in names
names_map  = map(str.upper, names)

print(type(names_map))

# Unpack names_map into a list
names_uppercase = [*names_map]

print(names_uppercase)


# -------------------------------------------
# Bringing it all together

import numpy as np

arrival_times = [*range(10,60,10)]

# Convert arrival_times to an array and update the times
arrival_times_np = np.array(arrival_times)
new_times = arrival_times_np - 3

print(new_times)

# Use list comprehension and enumerate to pair guests to new times
guest_arrivals = [(names[i],time) for i,time in enumerate(new_times)]

print(guest_arrivals)

# Map the welcome_guest function to each (guest,time) pair
def welcome_guest(*args):
    message_list = ['Welcome to Festivus {}... You are {} min late.'.format(guest, time) for guest, time in args]
    return message_list

welcome_map = map(welcome_guest, guest_arrivals)

guest_welcomes = [*welcome_map]

print(*guest_welcomes, sep='\n')


# -------------------------------------------

"""
2. Timing and profiling code

%timeit
%%timeit
%lprun : find the bottleneck
%mprun : memory usage
"""


# -------------------------------------------

"""
3. Gaining efficiencies
"""
# -------------------------------------------
# Combine lists

with open('data/chap01/pokemon_name.txt', 'r') as f:
    names = f.readlines()
    names = [n.replace('\n','') for n in names]

with open('data/chap01/pokemon_type1.txt', 'r') as f:
    primary_types = f.readlines()
    primary_types = [n.replace('\n','') for n in primary_types]

with open('data/chap01/pokemon_type2.txt', 'r') as f:
    secondary_types = f.readlines()
    secondary_types = [n.replace('\n','') for n in secondary_types]

with open('data/chap01/pokemon_gen.txt', 'r') as f:
    generations = f.readlines()
    generations = [n.replace('\n','') for n in generations]


names_types = [*zip(names, primary_types, secondary_types)]
print(*names_types[:5], sep='\n')
print()

# Combine five items from names and three items from primary_types
differing_lengths = [*zip(names[:5], primary_types[:3])]
print(*differing_lengths, sep='\n')
print()


# -------------------------------------------
# Counting from a sample

from collections import Counter

# Collect the count of primary types
type_count = Counter(primary_types)
print(type_count, '\n')

# Collect the count of generations
gen_count = Counter(generations)
print(gen_count, '\n')

# Collect the count of Pokémon for each starting_letter
starting_letters = [name[0] for name in names]
starting_letters_count = Counter(starting_letters)
print(starting_letters_count)


# -------------------------------------------
# Combinations

from itertools import combinations
import random

pokemon = random.sample(names, 5)   # select 5 samples

# Create a combination object with pairs of Pokémon
combos_obj = combinations(pokemon, 2)
print(type(combos_obj), '\n')

# Convert combos_obj to a list by unpacking
combos_2 = [*combos_obj]
print(combos_2, '\n')

# Collect all possible combinations of 4 Pokémon directly into a list
combos_4 = [*combinations(pokemon, 4)]
print(combos_4)


# -------------------------------------------
# Set

ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']
misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

ash_set = set(ash_pokedex)
misty_set = set(misty_pokedex)

# Find the Pokémon that exist in both sets
both = ash_set.intersection(misty_set)
print(both)

# Find the Pokémon that Ash has, and Misty does not have
ash_only = ash_set.difference(misty_set)
print(ash_only)

# Find the Pokémon that are in only one set (not both)
unique_to_set = ash_set.symmetric_difference(misty_set)
print(unique_to_set)


# -------------------------------------------
# Searching from set

print('Pikachu' in ash_pokedex)
print('Pikachu' in misty_set)


# -------------------------------------------
# Gathering unique item

def find_unique_items(data):
    uniques = []

    for item in data:
        if item not in uniques:
            uniques.append(item)

    return uniques

# Use find_unique_items() to collect unique Pokémon names
uniq_names_func = find_unique_items(names)
print(len(uniq_names_func))

# Convert the names list to a set to collect unique Pokémon names
uniq_names_set = set(names)
print(len(uniq_names_set))

# Check that both unique collections are equivalent
print(sorted(uniq_names_func) == sorted(uniq_names_set))

# --> set is faster !!!

# Use the best approach to collect unique primary types and generations
uniq_types = set(primary_types)
uniq_gens = set(generations)
print(uniq_types, uniq_gens, sep='\n')


# -------------------------------------------
# Eliminating loops

# original code
gen1_gen2_name_lengths_loop = []

for name, gen in zip(names, generations):
    if int(gen) < 3:
        name_length = len(name)
        poke_tuple = (name, name_length)
        gen1_gen2_name_lengths_loop.append(poke_tuple)


# Effective code
gen1_gen2_pokemon = [name for name, gen in zip(names, generations) if int(gen) < 3]
name_lengths_map = map(len, gen1_gen2_pokemon)
gen1_gen2_name_lengths = [*zip(gen1_gen2_pokemon, name_lengths_map)]

print(gen1_gen2_name_lengths_loop[:5])
print(gen1_gen2_name_lengths[:5])


# -------------------------------------------
# totals and averages without a loop

# hp, attack, defense, sp_attack, sp_defense
stats = np.loadtxt('data/chap01/pokemon_stat.txt')

# Loop
poke_list = []

for pokemon, row in zip(names, stats):
    total_stats = np.sum(row)
    avg_stats = np.mean(row)
    poke_list.append((pokemon, total_stats, avg_stats))


# Effective code
total_stats_np = stats.sum(axis=1)
avg_stats_np = stats.mean(axis=1)
poke_list_np = [*zip(names, total_stats_np, avg_stats_np)]

print(poke_list_np == poke_list, '\n')
print(poke_list_np[:3])
print(poke_list[:3], '\n')

top_3 = sorted(poke_list_np, key=lambda x: x[1], reverse=True)[:3]
print('3 strongest Pokémon:\n{}'.format(top_3))

# -------------------------------------------
# One-time calculation loop

from collections import Counter

# Collect the count of each generation
gen_counts = Counter(generations)

total_count = len(generations)

for gen, count in gen_counts.items():
    gen_percent = round(count / total_count * 100, 2)
    print('generation {}: count = {:3}, percentage = {}'
          .format(gen, count, gen_percent))


# -------------------------------------------
# Holistic conversion loop
# gather all the possible pairs of Pokémon types.

pokemon_types = sorted(list(set(primary_types)))
print(pokemon_types, '\n')

# Collect all possible pairs using combinations()
possible_pairs = [*combinations(pokemon_types, 2)]

enumerated_tuples = []

for i, pair in enumerate(possible_pairs, 1):
    enumerated_pair_tuple = (i,) + pair
    enumerated_tuples.append(enumerated_pair_tuple)

# Convert all tuples in enumerated_tuples to a list
enumerated_pairs = [*map(list, enumerated_tuples)]
print(enumerated_pairs)


# -------------------------------------------
# Bringing it all together: z-scores

hps = stats[:, 0]
hp_avg = hps.mean()
hp_std = hps.std()


# Loop version
poke_zscores = []

for name, hp in zip(names, hps):
    z_score = (hp - hp_avg)/hp_std
    poke_zscores.append((name, hp, z_score))

high_hp_pokemon = []

for name, hp, zscore in poke_zscores:
    if zscore > 3:
        high_hp_pokemon.append((name, hp, zscore))


# Effective code version
z_scores = (hps - hp_avg)/hp_std
poke_zscores2 = [*zip(names, hps, z_scores)]
print(*poke_zscores2[:3], sep='\n')
print()

highest_hp_pokemon = [(name, hp, zscore) for name, hp, zscore in poke_zscores2 if zscore > 3]
print(*highest_hp_pokemon, sep='\n')


# -------------------------------------------

"""
4. pandas DataFrame iteration
"""

import pandas as pd

baseball_df = pd.read_csv('data/chap01/baseball_stats.csv')
pit_df = baseball_df[baseball_df.Team == 'PIT']
print(pit_df.head())


# -------------------------------------------
# Iterating with .iterrows()

for i, row in pit_df.iterrows():
    print(row)
    if i == 21: break

print()

for row_tuple in pit_df.iterrows():
    print(row_tuple)
    if row_tuple[0] == 21: break

print()


# -------------------------------------------
# Run differentials with .iterrows()

# 각 시즌별 run differential 계산.
# runs_score (RS, 출루 횟수) - runs_allowed (RA, 총 출루 허용횟수)

giants_df = baseball_df[baseball_df.Team == 'SFG']

run_diffs = []

# Write a for loop and collect runs allowed and runs scored for each row
for i,row in giants_df.iterrows():
    run_diff = row['RS'] - row['RA']
    run_diffs.append(run_diff)

giants_df['RD'] = run_diffs
print(giants_df.head())


# -------------------------------------------
# Iterating with .itertuples()

run_diffs = []

# Loop over the DataFrame and print each row's Index, Year and Wins (W)
for row in giants_df.itertuples():
    run_diff = row.RS - row.RA
    run_diffs.append(run_diff)

    if row.Playoffs == 1:
        print(row.Index, row.Year, row.W)   # W : wins

giants_df['RD'] = run_diffs
print(giants_df.head())


# -------------------------------------------
# Analyzing baseball stats with .apply()

runs_df = giants_df[['RS','RA','W','Playoffs']]

# Gather sum of all columns
stat_totals = runs_df.apply(sum, axis=0)
print(stat_totals, '\n')

# Gather total runs scored in all games per year
total_runs_scored = runs_df[['RS', 'RA']].apply(sum, axis=1)
print(total_runs_scored[:5], '\n')

# Convert numeric playoffs to text
def text_playoffs(num_playoffs):
    if num_playoffs == 1:
        return 'Yes'
    else:
        return 'No'

textual_playoffs = runs_df.apply(lambda row: text_playoffs(row['Playoffs']), axis=1)
print(textual_playoffs)


# -------------------------------------------
# Settle a debate with .apply()

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)

# Create a win percentage Series
win_percs = giants_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

giants_df['WP'] = win_percs
print(giants_df.head(), '\n')

# Display dbacks_df where WP is greater than 0.60
print(giants_df[giants_df['WP'] >= 0.60])


# -------------------------------------------
# Replacing .iloc with underlying arrays

# old version
win_percs_list = []

for i in range(len(giants_df)):
    row = giants_df.iloc[i]

    wins = row['W']
    games_played = row['G']
    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

giants_df['WP'] = win_percs_list


# Effective version
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(giants_df['W'].values, giants_df['G'].values)

# Append a new column to baseball_df that stores all win percentages
giants_df['WP'] = win_percs_np

print(giants_df.head())


# -------------------------------------------
# Predict win percentage

def predict_win_perc(RS, RA):
    prediction = RS ** 2 / (RS ** 2 + RA ** 2)
    return np.round(prediction, 2)

# version 1 : Loop
win_perc_preds_loop = []

for row in baseball_df.itertuples():
    win_perc_pred = predict_win_perc(row.RS, row.RA)
    win_perc_preds_loop.append(win_perc_pred)


# version 2 : apply
win_perc_preds_apply = baseball_df.apply(lambda row: predict_win_perc(row['RS'], row['RA']), axis=1)

# version 3 : using NumPy arrays
win_perc_preds_np = predict_win_perc(baseball_df['RS'].values, baseball_df['RA'].values)
baseball_df['WP_preds'] = win_perc_preds_np

print(baseball_df.head())

# -------------------------------------------
