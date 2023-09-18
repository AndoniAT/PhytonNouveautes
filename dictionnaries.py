# 2 Dictionnaries
dict1 = { 2016: 'Portland', 2018: 'Cleveland' }
dict2 = { 2017: 'Rimini', 2018: 'Edimbourg', 2019: 'Bale' }

# Fussion 1
# We can use the fussion with **
print('== Fussion 1 ==')
fussion1 = {**dict1, **dict2}
print(fussion1)

# Fussion 2
# We can use also a loop
print('\n== Fussion 2 ==')
fussion2 = dict1.copy()
for key, value in dict2.items() :
    fussion2[key] = value

print(fussion2)

# As we can see, no method is going to change the origin data in both dictionnaries
print('\nCheck no altered data ==>')
print(dict1)
print(dict2)

# Fussion 3 Update
print('\n== UPDATE ==')
dict1.update(dict2)
# however, this is going to change your original data in dict1
print(dict1)

# The update mathod doesnt return the merged dictionnarie, so avoid to do the following :
dict1 = { 2016: 'Portland', 2018: 'Cleveland' }
dict2 = { 2017: 'Rimini', 2018: 'Edimbourg', 2019: 'Bale' }
fussion3 = dict1.copy().update(dict2)
# Because it doesn't work
print(fussion3)

# Fussion 4 Operator :=
# We can use the := operator
(fussion4 := dict1.copy()).update(dict2)
print("\n== Fussion 4 => ( Operator := ) ==")
print(fussion4)

# Fussion 5 Union |
dict1 = { 2016: 'Portland', 2018: 'Cleveland' }
dict2 = { 2017: 'Rimini', 2018: 'Edimbourg', 2019: 'Bale' }
fussion5 = dict1 | dict2
print("\n== Fussion 5 => ( Union | ) ==")
print(fussion5)

# Union doesn't change the original data
print('\nCheck no altered data ==>')
print(dict1)
print(dict2)

# Fussion 6 In-place-union =|
dict1 |= dict2
print("\n== Fussion 6 => (In-place-union |= ) == ")
# In-place-union changes the original data
print(dict1)