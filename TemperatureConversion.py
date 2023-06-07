
def main():
#
    # The purpose of this program is to convert temperature into either fahrenheit or celsius
    # We will use these formulas
    # F = 9/5 * C + 32
    # C = F - 32 * 5/9
# Explain the program to the user
 print("Would you like to:")
 print("1) Convert Celsius to Fahrenheit")
 print("2) Convert Fahrenheit to Celsius")

# Get user information
 user_choice = int(input("Enter 1 or 2: "))

# Define variables
 cels_to_fahr = 1
 fahr_to_cels = 2


# Use Boolian Logic.
 if user_choice == 1:
    degcels1 = float(input("Enter the degrees in celsius: "))
    F = (9/5 * degcels1 + 32)
    print(degcels1, "Celsius is", F, "Fahrenheit")
 else:
    degfahr1 = float(input("Enter the degrees in fahrenheit: "))
    C = (degfahr1 - 32 * 5/9)
    print(degfahr1, "Fahrenheit is", C)

if __name__ == '__main__':
    main()