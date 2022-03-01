# Import os module
import os
# Import sys module
import sys

while True:
    # Take the name of the environment variable
    key_value = "MM"

    # Check the taken variable is set or not
    try:
        if os.environ[key_value]:
            print("The value of", key_value, " is ", os.environ[key_value])
    # Raise error if the variable is not set
        else:
            print(key_value, 'environment variable is not set.')
            os.environ[key_value] = 'BGM'
    except KeyError:
        print(key_value, 'environment variable is not set.')
        # Terminate from the script
        sys.exit(1)
