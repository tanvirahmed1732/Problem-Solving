//Mileage matters

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
		    double n = sc.nextInt();
		    double x = sc.nextInt();
		    double y = sc.nextInt();
		    double a = sc.nextInt();
		    double b = sc.nextInt();
		    double pm = (n/a)*x;
		    double dm = (n/b)*y;
		    if(pm < dm)
		    System.out.println("PETROL");
		    else if(pm == dm)
		    System.out.println("ANY");
		    else
		    System.out.println("DIESEL");
		}
	}
}
