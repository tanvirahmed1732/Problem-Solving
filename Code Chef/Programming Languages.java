//Programming Languages

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
		    int a1 = sc.nextInt();
		    int b1 = sc.nextInt();
		    int a2 = sc.nextInt();
		    int b2 = sc.nextInt();
		    if(a == a1 && b == b1)
		    System.out.println("1");
		    else if(a == b1 && b == a1)
		    System.out.println("1");
		    else if(a == a2 && b == b2)
		    System.out.println("2");
		    else if(a == b2 && b == a2)
		    System.out.println("2");
		    else{
		    System.out.println("0");
		    }
		}
	}
}
