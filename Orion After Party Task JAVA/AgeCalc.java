/* Start
Prompt user to input father's age
Prompt user to input son's age
Using an if statement, ensure that the numbers inputed are neither less than 1 nor ore than 80
Calculate the number of years it would take or the number of yeaars ago the father's age would be or was twice his son's:
	father's age = F
	son's age = S
	number of years = x
Use a conditional statement to separate the calculations to ensure the number of years value is always greater than 0 (i.e. is not a negative value).
	
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
End */




import java.util.Scanner;
public class AgeCalc{
	public static void main(String[] args){
	Scanner input = new Scanner(System.in);
	
	System.out.print("Enter a number between 1 and 80 as the Father's age: ");
	int fathersAge = input.nextInt();

	System.out.print("Enter a number between 1 and 80 as the son's age: ");
	int sonsAge = input.nextInt();

	int twiceSonsAge = 2 * sonsAge;

	if((fathersAge <1 || fathersAge >80) || (sonsAge <1 || sonsAge > 80)){
	System.out.print("Invalid Input");}

	else { if(twiceSonsAge < fathersAge){
		int numberOfYears = fathersAge - twiceSonsAge;
		System.out.printf("In %d years time, the father would be twice as old as his son.", numberOfYears);}

	else if(twiceSonsAge > fathersAge){
		int numberOfYears = twiceSonsAge - fathersAge;
		System.out.printf("%d years ago, the father was twice as old as his son.", numberOfYears);}

	else { System.out.print(" The father is the same age as his son");}
		
				}

			}

		}