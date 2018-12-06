#!/usr/bin/env python3

# Import the operating system module
import os

# Open the output file for writing
out_file = open('test_014A.py', 'w')

# This writes out the following using only one line
# There are no embedded newlines in these two strings
out_file.write('To be or not to be')
out_file.write('That is the question')

# Use the \n to write out a newline
out_file.write('\n')

# This will add a blank line to the output file
out_file.write('\n')

# This writes out the following using two lines
out_file.write('To be or not to be\n')
out_file.write('That is the question\n')

##############################
# IMPORTANT!    Close the file
##############################
out_file.close()