//Circular Track

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
		    int m = sc.nextInt();
		    int div = 0;
		    if(a>b)
		    div = a - b;
		    else
		    div = b - a;
		    int div2 = 0;
		    if(a>b)
		    div2 = m - a + b;
		    else
		    div2 = m - b + a;
		    if(div<div2)
		    System.out.println(div);
		    else
		    System.out.println(div2);
		}
	}
}
