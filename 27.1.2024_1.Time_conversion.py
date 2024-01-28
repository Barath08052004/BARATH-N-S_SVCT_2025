# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

# Example


# Return '12:01:00'.


# Return '00:01:00'.

# Function Description

# Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

# timeConversion has the following parameter(s):

# string s: a time in  hour format
# Returns

# string: the time in  hour format
# Input Format

# A single string  that represents a time in -hour clock format (i.e.:  or ).

# Constraints

# All input times are valid
# Sample Input 0

# 07:05:45PM
# Sample Output 0

# 19:05:45
 
def timeConversion(s):

    # Convert the input string to uppercase to handle case insensitivity
    s = s.upper()    

    # Extract the hours, minutes, and seconds from the input string
    hours, minutes, seconds_ampm = map(int, s[:-2].split(':'))
    # Check if it is PM and not 12 PM, then add 12 hours to convert to 24-hour format
    if "PM" in s and hours != 12:
        hours += 12
    # Check if it is AM and 12 AM, then set hours to 0
    elif "AM" in s and hours == 12:
        hours = 0
    # Format the result as a string in 24-hour format

    result = f"{hours:02d}:{minutes:02d}:{seconds_ampm:02d}"
    
    return result
if __name__ == '__main__':
    s = input().strip()
    result = timeConversion(s)
    print(result)