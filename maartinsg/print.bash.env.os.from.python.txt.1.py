#!/usr/bin/env python

# I have chosen to print some environment variables pre-defined for login BASH 
# shell in Linux, to use Python routines of approaches, 
# so I wrote some code below:

import os

# I wrote a text to display HOME variable from Bash likes
sHOME = os.environ["HOME"]
print(sHOME)
