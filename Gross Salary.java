//Gross Salary

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
		    double gs = 0.00;
		    double s = sc.nextDouble();
		    if(s < 1500){
		        gs = s + (s*0.1) + (s*0.9);
		    }
		    else
		    gs = s + 500 + (s*0.98);
		    System.out.println(gs);
		 }
	}
}
