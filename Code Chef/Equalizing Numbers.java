//Equalizing Numbers

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
		    int div = 0;
		    if(a>=b)
		    div = a-b;
		    else
		    div = b - a;
		    if(a==b){
		    System.out.println("YES");
		    }
		    if(div%2 == 0 && div != 0)
		    System.out.println("YES");
		    else if(div % 2 == 1)
		    System.out.println("NO");
		}
	}
}
