#!/usr/bin/env python3

########################
# a_list is the ORIGINAL LIST
#########################
a_list = [1, 2, 3, 4]

print("The original list...")
print(a_list)
print()        # This simply prints an empty line (more below)

#################################
# Using the FOR loop, with enumerate to navigate the entire list
###################################
# NOTE that i is the index used to access a given item in the list
# This demonstrates that we can change a value in the list
#####################################
for i, item in enumerate(a_list):
    a_list[i] = 100        # This changes the value in the list
# END of the FOR loop

###########################
# Print the modified list
# NOTE that each item should now be 100.
###############################
print(a_list)