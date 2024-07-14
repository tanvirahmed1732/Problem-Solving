//Good Quality Bulbs

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
		    int ar[] = new int [n-1];
		    int sum = 0;
		    for(int i =0; i<n-1; i++){
		        ar[i] = sc.nextInt();
		        sum += ar[i];
		    }
		    int cal = (n * x) - sum;
		    if(cal<0)
		    System.out.println("0");
		    else
		    System.out.println(cal);
		}
	}
}
