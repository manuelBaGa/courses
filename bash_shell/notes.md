### Make a script executable by bash
    -   !/bin/bash

### Give permitions to a file
chmod X1X2X3 --> X1 ~ 421 (4~read,2~write,1~execute) --> X1 ~ user, X2 ~ group, X3 ~ other users
                        7 <-- 4+2+1 (read+write+execute)

### User variables vs OS variables (environment variables)
vim /etc/profile <-- configuration for each environment variables
    -   Add you variable at the end of the profile
    -   VARIABLE = "This is my variable"
    -   export VARIABLE

### Export user variables to other processes
    -   export VARIABLE
    -   Call another script that will use the exported $VARIABLE.
        -   The second script will inherit the variable

### Arguments in scripts
    -   $0 -> Scripts Name
    -   $1 to ${10} ->  More than 1 digit requires curvy brakets
    -   $# -> Arguments counter
    -   $* -> All arguments

### Substitute the result from a command in a variable
    -   $(command)
    -   `command`

### Script debug
    -   -v --> Show the result fprm our script line by line
    -   -x --> Show the result from the commands

### Capturing information from the user
    -   Using functions echo and read

### Verify lenght and data type inputs
    -   For lenght: read -n<characters_number>
    -   For data types we use regular expressions

### Conditionals: if
    -   if [ condition1 ]; then
            statement1
        elif [ condition2 ]; then
            statement2
        else
            statement3
        fi