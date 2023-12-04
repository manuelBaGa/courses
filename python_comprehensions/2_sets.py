set_countries = {'col','mex','bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,443,23}
print(set_numbers)

#sets from multyple object types
set_types= {1,'hola',False,12.12}
print(set_types)

#creating sets from other objects
set_from_string = set('hola')
print(set_from_string)

#Set from a tuple
set_from_tuples = set(('abc','cbv','as','abc'))
print(set_from_tuples)

numbers = [1,2,3,1,2,3,4]
set_numbers_2 = set(numbers)
print(set_numbers_2)

#From set to list
unique_numbers = list(set_numbers_2)
print(unique_numbers)
