'''
The task:

The engineering team developed an application. This application is supposed to create an output file “output.txt” and somewhere in this file there should be a line:

Hello!

Please write an automated test. If the file “output.txt” is found and contains a line “Hello!” anywhere in the file the test succeeds, otherwise it fails.

Bonus task.

Write a GitHub to start the test
'''
import pytest

def test_my_automated_test():
    my_file = open("output.txt", "r")#github_workflows
    line=my_file.readline()

    while line != '':
        if 'Hello!' in line:
            print('Hello! was found in the text')
            break

        line = my_file.readline()
    else:
        raise Exception('Hello! was not found in the text')



