# Control Structures Assignment

This assignment will introduce you to Control Structures.  Besure to read all the instructions carefully, there are many ways to solve these problems but some problems have specific requirements in the way they must be coded.

The test folder includes tests for each problem that you can use to ensure that you've solved the problem correctly. 

For all output of floating-point numbers format the number to two points of precision using python's formatted strings for example:
```
f"{sugar:.2f} cups of sugar"
```
Examples are just examples and you don't need to use the same wording, however read the descriptions carefully as some problems have specific word requirements or line order requirements for the tests to pass. The examples do pass the tests

## 1) TemperatureConversion.py

Write a program that converts Celsius temperatures to Fahrenheit temperatures and vice versa. The formula is as follows:

F = ((9/5) * C) +32

C = (F – 32) * 5/9

Your program should ask the user to choose from a menu that gives them a choice of what conversion they would like. The choices should be numbered, 1 for Celsius to Fahrenheit and 2 for Fahrenheit to Celsius. Depending on the choice, your program should prompt the user to enter a temperature in Celsius or in Fahrenheit, perform the calculation and then display the temperature converted on the last line. Make sure your output is clearly labeled by adding explanation text next to the values printed. 

**Example:**

![Temperature](images/Temperature.png)


## 2) CookieRecipe.py

A cookie recipe calls for the following ingredients:
```
    1.5 cups of sugar
    1 cup of butter
    2.75 cups of flour
    Makes 48 Cookies 
```
The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks the user how many cookies he or she wants to make, then displays the number of cups of each ingredient needed for the specified number of cookies. 

Additionally, give the user the option of low fat and low sugar. If the user chooses either option, cut down the amount of butter or sugar in half depending on what the user chose. Make sure the choices are clearly stated. Use Y/N for the low fat and low sugar questions.  The Y & N answers should be case-insensitive, meaning Y & y are the same thing.  It's okay to default to no if the answer isn't Y or y.  

The final output should print the amount of sugar, amount of butter, amount of flour and number of cookies each on their own line in that order.  

**Example:** 

![Cookies](images/CookieRecipe.png)
## DayOfTheWeek.py

Write a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should display an error message, that includes the word "error", if the user enters a number that is outside the range of 1 through 7, or a non-number word like "tree."  You must use a cascading/multiple selection for this problem.

**Example:** 

![Day of the Week](images/DayOfTheWeek.png)

## 4) MagicDate.py

The date June 10, 1960, is special because when it is written in the following format, the month times the day equals the year:
6/10/60

Design a program that asks the user to enter a month (in two-digit numeric form), a two-digit day, and a two-digit year. The program should then determine whether the month times the day equals the year. If so, it should display a message saying the date "is a magic date" on the last line of the output. Otherwise, it should display a message saying the date "is not a magic date" on the last line of the output.  

**Example:**

![Magic Date](images/MagicDate.png)

## 5) Colors.py

The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors. When you mix two primary colors, you get a secondary color, as shown here:
```
    When you mix red and blue, you get purple.
    When you mix red and yellow, you get orange.
    When you mix blue and yellow, you get green.
    
Also mixing the same color with itself, you get that same color 
```
You should be able to add the colors in any order, and any combination including red & red which would just produce red.  If anything other than red, blue or yellow is entered for ether of the color options the program should produce an error message that includes the word "error". 

## Remember
**Style Matters**: Comment your code, use good variable descriptive variable names.  Pay attention to spacing and formatting.  Your code should tell the story of what it does. 

**Commit As You Go**: Commit and push your code to Github as you finish each section or even more often.  This will act as a back up and history of your changes.  Only the last commit before the deadline will be graded.  

**Turn It In**: Once you're done make sure your code is committed to Github.  Then copy the repository URL and pasting it into your submission on Blackboard. 