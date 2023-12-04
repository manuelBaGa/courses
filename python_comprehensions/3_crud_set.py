set_countries = {'col','mex','bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add elements
set_countries.add('pe')
print('pe' in set_countries)

#Update
set_countries.update({'ar','ecu','pe'})
print(set_countries)

#Remove
set_countries.remove('col')
print(set_countries)

set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

#Clear the wholes set
set_countries.clear()
print(set_countries)
print(len(set_countries))