'''
INSTRUCTIONS
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them

TEST EXAMPLES:
test.assert_equals(parse_int('one'), 1)
test.assert_equals(parse_int('twenty'), 20)
test.assert_equals(parse_int('two hundred forty-six'), 246)
'''

string='seven hundred eighty-three thousand nine hundred and nineteen'

numbers_dict={
    'on':1,'tw':2,'th':3,'fo':4,'fi':5,'si':6,'se':7,'ei':8,'ni':9,'ze':0
}
multipliers={'hundred':100,'thousand':1000,'million':1000000}
exceptions={'ten':10,'eleven':11,'twelve':12}
simple_string=string.replace('-',' ').replace(' and',' ')
num=0
thousands=0
for word in simple_string.split():
    if word in multipliers:
        if word=='thousand':
            thousands=num*multipliers[word]
            num=0
        else:
            num*=multipliers[word]
    elif word in exceptions:
        num+=exceptions[word]
    elif word[-2:] == 'ty':
        num+=numbers_dict[word[:2]]*10
    elif word[-4:] == 'teen':
        num+=numbers_dict[word[:2]] + 10
    else:
        num+=numbers_dict[word[:2]]

print(thousands+num)