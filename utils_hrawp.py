''' ITERATION 2

Data Analysis for Mars Landing

This module provides a simple, reusable foundation for my analytics projects. 


Process:

In this second interation, add a function that returns the byline as a string.
I'll create a function named get_byline().
It'll return my byline to whatever calls the get_byline() function.
I'll update the main() function to use the new get_byline() function.

'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Using Data to Land on Mars'

#####################################
# Define the get_bylein() Function
#####################################

def get_byline() -> str:
   '''Return a byline for my anlystics projects.'''
   return byline
   
#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
     '''Print the byline to the console when this function is called.'''
     print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
