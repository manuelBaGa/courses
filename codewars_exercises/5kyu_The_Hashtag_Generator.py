'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''

test_text = " Hello there thanks for trying my Kata"
def generate_hashtag(s):
    if s == '':
        return False
    else:
        hash_tag = '#'+''.join(map(str.capitalize,s.split()))
    return False if len(hash_tag) > 140 else hash_tag
    
print(generate_hashtag(test_text))

