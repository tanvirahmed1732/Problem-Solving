//Hardest Problem Bet

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
		    int sa = sc.nextInt();
		    int sb = sc.nextInt();
		    int c = sc.nextInt();
		    if(sa<sb && sa<c)
		    System.out.println("Draw");
		    else if(sb< sa && sb< c)
		    System.out.println("Bob");
		    else
		    System.out.println("Alice");
		}
	}
}
