numbers=[]
for element in range(1,11):
    numbers.append(element*2)

print(numbers)

numbers_v2 = [element*2 for element in range(1,11)]
print(numbers_v2)

numbers_v3=[]
for i in range(1,11):
    if i%2 == 0:
        numbers_v3.append(i*2)

print(numbers_v3)

numbers_v4=[i*2 for i in range (1,11) if i%2 == 0]
print(numbers_v4)        