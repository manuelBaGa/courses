set_a = {'col','mex','bol'}
set_b = {'pe','bol'}
print(set_a,set_b)

#union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

#intersection
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

#difference
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

#symetric difference: join between elements that are not shared across sets.
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)