//Ambiguous Permutations

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		while(true){
		    int n = sc.nextInt();
		    if(n==0)
		    break;
		    int ar[] = new int [n+1];
		    for (int i =1;i<=n ;i++ ) 
		    ar[i] = sc.nextInt();
		    boolean check = true;
		    for (int i = 1; i<=n ;i++ ){
		        if(ar[ar[i]] != i){
		            check = false;
		            break;
		        }
		    }
		    if(check)
		    System.out.println("ambiguous");
		    else
		    System.out.println("not ambiguous");
		}
	}
}
