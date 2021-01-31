#Name: David Cronk
#Assignment: HW1
#This program takes a user input for year and tells the user if it is a 
#leap year or not. 
#To run this program, type the comman python david_cronk_hw1.py

#import time for sleep functionality
import time
#Get user input
#try:
year = int(input("\nEnter a year to see if it is a leap year: "))
#check if input is an integer
#except:
#	print("\nNot a valid input, please run again!\n")
#	time.sleep(3)
#	exit()
#else, it is an integer. If integer is 0 or below, exit
#if year <= 0:
#	print("\nNot a valid year, please run again!\n")
#	time.sleep(3)
#	exit()
#if not, then if integer is divisible by 4...
if (year % 4) == 0:
	#if year is divisible by 100...
	if (year % 100) == 0:
		#if year divisible by 4,100, and 400, year is a leap year
		if (year % 400) == 0:
			print(str(year) + " is a leap year!\n")
			time.sleep(3)
			exit()
		#else year is only divisible by 4 and 100, not a leap year
		else:
			print(str(year) + " is not a leap year!\n")
			time.sleep(3)
			exit()
	#if only divisible by 4, year is a leap year	
	print(str(year) + " is a leap year!\n")
	time.sleep(3)
	exit()
#else the year is not divisible by 4, not a leap year
else:
	print(str(year) + " is not a leap year!\n")
	time.sleep(3)
	exit()
exit()
			
	
