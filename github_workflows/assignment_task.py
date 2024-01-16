'''
The task:

The engineering team developed an application. This application is supposed to create an output file “output.txt” and somewhere in this file there should be a line:

Hello!

Please write an automated test. If the file “output.txt” is found and contains a line “Hello!” anywhere in the file the test succeeds, otherwise it fails.

Bonus task.

Write a GitHub to start the test
'''
my_file = open("github_workflows/output.txt", "r")
my_text = my_file.readline()
try:
    assert my_text == 'Hello!'
    print("Assertion is correct")
except Exception as e:
    print("We have this exception: ", e.__str__)
