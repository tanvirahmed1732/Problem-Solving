//Chefland Visa

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
		    int x1 = sc.nextInt();
		    int x2 = sc.nextInt();
		    int y1 = sc.nextInt();
		    int y2 = sc.nextInt();
		    int z1 = sc.nextInt();
		    int z2 = sc.nextInt();
		    if(x1<=x2 && y1<=y2 && z1>=z2)
		    System.out.println("YES");
		    else
		    System.out.println("NO");
		}
	}
}
