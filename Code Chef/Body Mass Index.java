// Body Mass Index
import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){
		    int m = sc.nextInt();
		    int h = sc.nextInt();
		    int bmi = m/(h*h);
		    if(bmi<=18)
		    System.out.println("1");
		    else if(bmi> 18 && bmi < 25)
		    System.out.println("2");
		    else if (bmi > 24 && bmi < 30)
		    System.out.println("3");
		    else if(bmi >= 30)
		    System.out.println("4");
		}
	}
}
