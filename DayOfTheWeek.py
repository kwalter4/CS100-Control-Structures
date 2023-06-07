
def main():

 # This program will give the weekday name based on it's corresponding number
 # Explain to the user what we will do
 print("This program will return the day of the week based on the number entered 1-7 => Monday-Sunday.")

 # Get input from the user
 number_of_day = int(input("Please enter a number 1-7: "))

 # Define Variables
 name_of_day = 'unknown'

 # Use Control Structures
 if number_of_day == '1':
    print("The weekday name is Monday.")
 elif "number_of_day" == '2':
    print("The weekday name is Tuesday.")
 elif "number_of_day" == '3':
    print("The weekday name is Wednesday.")
 elif "number_of_day" == '4':
    print("The weekday name is Thursday.")
 elif "number_of_day" == '5':
    print("The weekday name is Friday.")
 elif "number_of_day" == '6':
    print("The weekday name is Saturday.")
 elif "number_of_day" == '7':
    print("The weekday name is Sunday.")


if __name__ == '__main__':
    main()