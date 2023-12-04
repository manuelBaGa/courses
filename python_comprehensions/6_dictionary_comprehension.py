import random
#normal structure
dict = {}
for i in range(1,5):
    dict[i]=i*2

print(dict)

#comprehension sintaxys
dict_v2 = { i : i*2 for i in range(1,5)}
print(dict_v2)

#normal structure
countries = ['col','mex','bol','pe']
population = {}
for country in countries:
    population[country] = random.randint(1,100)

print(population)

#comprehension sintaxys
population_v2={ country: random.randint(1,100) for country in countries}
print(population_v2)

#dict comprehension with two lists
names = ['nico','zule','santi']
ages= [12,56,98]

print(list(zip(names,ages)))

new_dict = { name:age for (name, age) in zip(names,ages)}
print(new_dict)
