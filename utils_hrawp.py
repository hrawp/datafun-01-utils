''' Finalize utils module

Data Analysis for Mars Landing
This is the fourth interation.
'''
#####################################
# Import Modules at Top
#####################################
import statistics

#####################################
# Declare a global variables
#####################################

# Boolean variable to indicate is the a Mars mission
is_mars_landing: bool = True

# Integer for how many days away from Mars.
days_away: int = 16

# List of strings representing robots ready for deployment
is_robots: list = ["Rover", "StarLite", "Wallie", "Eclipse"]

# List of floats robot sizes:  
robot_size: list = [40.5, 37.5, 70.5, 60.5, 35]

#####################################
# Calculate Basic Statistics 
#####################################

# Calculate some robot stats. 
min_robot_size: float = min(robot_size)
max_robot_size: float = max(robot_size)
mean_robot_size: float = statistics.mean(robot_size)
stdev_robot_size: float = round(statistics.stdev(robot_size),2)

#####################################
# Define a global variable named byline.
# Make it a multilin f-string to show our information.
#####################################

byline: str = f"""
----------------------------------------------
Options for Mars landing robots.
----------------------------------------------
Is this a Mars Mission: {is_mars_landing}
How many days away is the closest robot: {days_away}
What is the names of the robots: {is_robots}
The size of the robots: {robot_size}

Min robot size: {min_robot_size}
Max robot size: {max_robot_size}
Average robot size: {mean_robot_size}
Standard Deviation of robot size: {stdev_robot_size}

"""

#####################################
# Define the get_byline() Function
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
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()

