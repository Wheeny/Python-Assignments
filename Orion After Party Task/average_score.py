""" Start
Prompt user to input 3 scores
Calculate the average of those scores
Using a conditional statement, assign a Grade to the average score
Print the results
End """

first_score = float(input("Enter an integer as 1st score: "))
	
second_score = float(input("Enter an integer as 2nd score: "))

third_score = float(input("Enter an integer as 3rd score: "))

average_score = (first_score + second_score + third_score)/3

print(f"Average Score: {average_score}" )

if((first_score < 0 or first_score > 100) or (third_score < 0 or third_score >  100) or (third_score < 0 or third_score > 100)):
	print("Invalid Input")

else: 
	if(average_score >= 90):
		print("Grade: A")

	elif(average_score >= 80):
		print("Grade: B")

	elif(average_score >= 70):
		print("Grade: C")

	elif(average_score >= 60):
		print("Grade: D")

	else:
		print("Grade: F")

				

	