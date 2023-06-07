
def main():

# Let the user know what the program is intended to do
 print("This program will tell you if a year is a magic year.")

# Next we need some input from the user
 user_day = int(input("Please enter the day of the month as a two digit number: "))
 user_month = int(input("Please enter the month as a two digit number: "))
 user_year = int(input("Please enter the year as a two digit number: "))

# Run the test to see if the day times the month equals the year
 if user_day * user_month == user_year:
    print("Yay, this is a magic number.")
 else:
    print("this is not a magic number.")

if __name__ == '__main__':
    main()