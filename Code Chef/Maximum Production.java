//Maximum Production

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
		    int d = sc.nextInt();
		    int x = sc.nextInt();
		    int y = sc.nextInt();
		    int z = sc.nextInt();
		    int mul = 0;
		    mul = x *7;
		    int mul2 = 0;
		    mul2 = (y * d) + (z * ( 7 - d));
		    if(mul<=mul2)
		    System.out.println(mul2);
		    else
		    System.out.println(mul);
		}
	}
}
