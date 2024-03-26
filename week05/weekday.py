#A python program that outputs if the day is a weekday or not
#Author: Ebelechukwu igwagu


#import python datetime module library
from datetime import datetime

#get today's date using the datetime module and now() function
now = datetime.now()
print(type(now))
print (f"Today's date and time is {now}")

#define the weekday function
def is_weekday (weekday_no):
#dictionary mapping of weekdays to its corresponding number
    weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6:"Sunday"
    }
#get function is used to display the day associated with the inputted weekday number
    return weekdays.get(weekday_no, "not a weekday, check number again")
  
#assigning each numerical representation of weekday to their corresponding name using dictionary
#python weekday function numbers weekdays from 0 to 6

weekday_no = int(input("Enter weekday number from 0 to 6: "))
#ensures only a number within 1 to 6 is entered
# Ensure the entered weekday number is valid and an integer
while weekday_no < 0 or weekday_no > 6:
    weekday_no = int(input("Please enter a number from 0 to 6: "))

if weekday_no <= 4:
    print (f"Today is {is_weekday(weekday_no)} and it is a weekday.")
    if weekday_no == 4:
        print("TGIF!")
else:
    print (f"{is_weekday(weekday_no)} is the weekend, yay!")



#References
#https://pynative.com/python-get-the-day-of-week/
#pynative.com
#tutorialpoints.com
