#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program is some experimentation of local and global variables

# global variables
variable_x = 25


def local_variable():
    # This function demonstrates local variables

    variable_x = 10
    variable_y = 30
    variable_z = variable_x + variable_y
    print("Local variable_x, variable_y, variable_z: {0} + {1} = {2}".
          format(variable_x, variable_y, variable_z))


def global_variable():
    # This function demonstrates global variables

    global variable_x
    variable_x = variable_x + 1
    variable_y = 30
    variable_z = variable_x + variable_y
    print("Global variable_x, variable_y, variable_z: {0} + {1} = {2}".
          format(variable_x, variable_y, variable_z))


def main():
    # This function calls the local_variable and global_variable functions

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
