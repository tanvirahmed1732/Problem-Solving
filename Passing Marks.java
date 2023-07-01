//Passing Marks

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
		    int n = sc.nextInt();
		    int x = sc.nextInt();
		    int ar[] =  new int [n];
		    for (int i =0;i<n ;i++ )
		    ar[i] = sc.nextInt();
		    Arrays.sort(ar);
		    System.out.println(ar[n-x]-1);
		}
	}
}
