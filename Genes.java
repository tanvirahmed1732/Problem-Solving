//Genes

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		if(a.charAt(0) == 'R' || b.charAt(0) == 'R')
		System.out.println("R");
		else if (a.charAt(0) == 'B' || b.charAt(0) == 'B')
		System.out.println("B");
		else
		System.out.println("G");
	}
}
