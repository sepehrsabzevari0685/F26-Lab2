# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file


import sys

arguments = len(sys.argv) - 1

if arguments == 0:
    print("This script requires exactly two arguments. No arguments were provided!")
elif arguments == 2:
    print("Hello user, good job, your provided two arguments!")
else:
    print(f"This script requires exactly two arguments. You provided {arguments} arguments.")
