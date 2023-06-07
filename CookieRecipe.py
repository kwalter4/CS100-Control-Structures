
def main():

  # This program will make a customized cookie recipe for the customer
  # Give the original recipe that makes 48 cookies
  print("Cookie Recipe:")
  print("1.5 cups of sugar")
  print("1 cup of butter")
  print("2.75 cups of flour")
  print("Makes 48 cookies")

  # Make sure there are no magic numbers.
  recipe1_sugar = 1.5
  recipe1_butter = 1
  recipe1_flour = 2.75
  recipe1_cookieCount = 48

  # Obtain some answers from the customer
  recipe2_cookieCount = input(int("How many cookies do you want to make? "))
  recipe2_lowSugar = input("Do you want low sugar? (N/Y): ")
  recipe2_lowFat =input("Do you want low fat? (N/Y): ")

  # Calculate the Customized recipe
  conversion_ratio = recipe1_cookieCount / recipe2_cookieCount
  customized_sugar = recipe1_sugar * conversion_ratio
  customized_butter = recipe1_butter * conversion_ratio
  customized_flour = recipe1_flour * conversion_ratio

 # Adjusting menu for low sugar and low fat by using half the original amount
  if recipe2_lowSugar == 'Y' or recipe2_lowSugar == 'y':
      total_sugar = customized_sugar * 0.5
  else:
      total_sugar = customized_sugar

  if recipe2_lowFat == 'Y' or recipe2_lowFat == 'y':
      total_butter = customized_butter * 0.5
  else:
      total_butter = customized_butter

 # We can now output the new customized recipe
 print("Cookie Recipe:")
 print({total_sugar},"cups of sugar")
 print({total_butter},"cups of butter")
 print({customized_flour},"cups of flour")
 print("Makes",{recipe2_cookieCount},"Cookies")


if __name__ == '__main__':
  main()