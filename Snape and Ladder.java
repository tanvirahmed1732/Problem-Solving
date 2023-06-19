//Snape and Ladder

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
		    int b = sc.nextInt();
		    int ls = sc.nextInt();
		    double max = 0;
		    max = Math.sqrt(b*b + ls*ls);
		    double min = 0;
		    min = Math.sqrt(ls*ls - b*b);
		    System.out.println(min+" "+max);
		}
	}
}
