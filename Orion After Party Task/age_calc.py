""" Start
Prompt user to input father's age
propt user to input son's age
Using an if statement, ensure that the numbers inputed are neither less than 1 nor ore than 80
Calculate the number of years it would take or the number of yeaars ago the father's age would be or was twice his son's:
	father's age = F
	son's age = S
	number of years = x
Using a conditional statement to separate the calculations, ensure the number of years value is always greater than 0 (i.e. is not a negative value).
	
	To get how many years time it would take the father's age to be twice his son's:
	 F + x = 2(S + x)
	 F + x = 2S + 2x
	 F - 2S = 2x - x
	 F - 2S = x


	To get how many years ago the father's age was twice his son's:
	 F - x = 2(S - x)
	 F - x = 2S - 2x
	 -x + 2x = 2S - F
	 x = 2S - F

Print the results
End  """

fathers_age = int(input("Enter a number between 1 and 80 as the Father's age: "))
	
sons_age = int(input("Enter a number between 1 and 80 as the son's age: "))

twice_sons_age = 2 * sons_age

if((fathers_age < 1 or fathers_age >80) or (sons_age < 1 or sons_age > 80)):
		print("Invalid Input")

else:
	if twice_sons_age < fathers_age:
		number_of_years = fathers_age - twice_sons_age;
		print(f"In {numberOfYears} years time, the father would be twice as old as his son.")

	elif twice_sons_age > fathers_age:
		number_of_years = twice_sons_age - fathers_age
		print(f"{numberOfYears} years ago, the father was twice as old as his son.")

	else:
		print(f"The father is the same age as his son")
		
			