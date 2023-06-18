//The Preparations

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
		    int n = sc.nextInt();
		    int k = sc.nextInt();
		    int mul = n * k;
		    if(mul<m)
		    System.out.println("YES");
		    else
		    System.out.println("NO");
		}
	}
}
