//Complete the credits

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
		    int x = sc.nextInt();
		    if(x>65)
		    System.out.println("Overload");
		    else if(x<35)
		    System.out.println("Underload");
		    else
		    System.out.println("Normal");
		}
	}
}
