//ATM Machine

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
		    int k = sc.nextInt();
		    int ar[] = new int [n];
		    int arr[] = new int [n];
		    for (int i = 0;i<n;i++){
		        ar[i] = sc.nextInt();
		        if(ar[i]<=k){
		            k = k - ar[i];
		            arr[i] = 1;
		        }
		        else{
		            arr[i] = 0;
		        }
		    }
		    for (int i = 0;i<n ;i++ )
		    System.out.print(arr[i]);
		    System.out.println();
		    
		}
	}
}
