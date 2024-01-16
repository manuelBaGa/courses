'''
The task:

The engineering team developed an application. This application is supposed to create an output file “output.txt” and somewhere in this file there should be a line:

Hello!

Please write an automated test. If the file “output.txt” is found and contains a line “Hello!” anywhere in the file the test succeeds, otherwise it fails.

Bonus task.

Write a GitHub to start the test
'''
try:
    my_file = open("github_workflows/output.txt", "r")#github_workflows
    line=my_file.readline()
    while line != '':
        if 'Hello!' in line:
            print('Test passed: Hello! was found in the text')
            break
        line = my_file.readline()
    else:
        print('Test failed: Hello! is not in the text')
except Exception as e:
    print("Test failed due to this exception: ", e)
