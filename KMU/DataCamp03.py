# --------------------------------------------
# Dictionary
# --------------------------------------------

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'australia':'vienna'}

print(europe.keys())
print(europe['norway'])

europe['italy'] = 'rome'    # add or update
europe['poland'] = 'warsaw'

del(europe['australia'])    # Remove

print('italy' in europe)
print(europe)               # 순서는 고정 안됨


# Dictionary of dictionaries

europe = {'spain': {'capital':'madrid', 'population':46.77},
          'france': {'capital':'paris', 'population':66.03},
          'germany': {'capital':'berlin', 'population':80.62},
          'norway': {'capital':'oslo', 'population':5.084}}

print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}
europe['italy'] = data

print(europe)


# --------------------------------------------
# Pandas
# --------------------------------------------

















