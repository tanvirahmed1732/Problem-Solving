//Chef and Dolls

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
		    int ar[] = new int[n];
		    for (int i =0;i<n ;i++ )
		    ar[i] = sc.nextInt();
		    for(int i = 0; i<n-1; i++){
		        //System.out.print(ar[i]);
		        boolean check = true;
		        for(int j = i+1; j<n; j++){
		            if(ar[i] == -1)
		            check = false;
		            if(ar[i] == ar[j] && ar[i] != -1){
		                check = false;
		                ar[j] = -1;
		                break;
		            }
		        }
		        if(check){
		            System.out.println(ar[i]);
		        }
		    }
		    if(ar[n-1] != -1)
		    System.out.println(ar[n-1]);
		}
	}
}
