/*Start
Prompt user to input 3 scores
Calculate the average of those scores
Using a conditional statement, assign a Grade to the average score
Print the results
End */

import java.util.Scanner;
public class AverageScore{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);
	
	System.out.print("Enter an integer as 1st score: ");
	double firstScore = input.nextDouble();

	System.out.print("Enter an integer as 2nd score: ");
	double secondScore = input.nextDouble();

	System.out.print("Enter an integer as 3rd score: ");
	double thirdScore = input.nextDouble();

	double averageScore = (firstScore + secondScore + thirdScore)/3;

	System.out.printf("Average Score: %.2f%n ", averageScore);

	if((firstScore < 0 || firstScore > 100) || (thirdScore < 0 || thirdScore >  100) || (thirdScore < 0 || thirdScore > 100)){
	System.out.print("Invalid Input");}

	else { 
		if(averageScore >= 90){
		System.out.println("Grade: A");}

		else if(averageScore >= 80){
		System.out.println("Grade: B");}

		else if(averageScore >= 70){
		System.out.println("Grade: C");}

		else if(averageScore >= 60){
		System.out.println("Grade: D");}

		else System.out.println("Grade: F");

				}


			}


		}

	