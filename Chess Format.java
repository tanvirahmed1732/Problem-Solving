/* package codechef; // don't place package name! */

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
		    int a = sc.nextInt();
		    int b = sc.nextInt();
		    int sum = a + b;
		    if(sum<3)
		    System.out.println("1");
		    else if(3<= sum && sum <= 10)
		    System.out.println("2");
		    else if(11<= sum && sum <= 60)
		    System.out.println("3");
		    else if(60<sum)
		    System.out.println("4");
		}
	}
}
