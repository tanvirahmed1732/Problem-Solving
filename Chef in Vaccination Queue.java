//Chef in Vaccination Queue

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
		    int p = sc.nextInt();
		    int x = sc.nextInt();
		    int y = sc.nextInt();
		    int ar[] = new int[n];
		    for (int i =0;i<n ;i++ ){
		        ar[i] = sc.nextInt();
		    }
		    int count = 0;
		    for(int i =0; i<p; i++){
		        if(ar[i] == 0)
		        count+=x;
		        else
		        count+=y;
		    }
		    System.out.println(count);
		}
	}
}
