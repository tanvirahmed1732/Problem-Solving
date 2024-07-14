//Zero Ones Equal One Zeros

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
		    String even = "100";
		    String odd = "";
		    if(n%2==0){
		        for (int i = 3;i<n-1 ;i++ )
		        even+='0';
		        even+='1';
		        System.out.println(even);
		    }
		    else{
		        int temp = n/2;
		        for(int i =0; i<temp; i++)
		        odd+='0';
		        odd+='1';
		        for(int i= temp +1; i<n; i++)
		        odd+='0';
		        System.out.println(odd);
		    }
		}
	}
}
