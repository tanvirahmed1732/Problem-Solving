//Good Weather

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		// your code goes here
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){
		    int ar[] = new int [7];
		    for (int i = 0;i<7 ;i++ ){
		        ar[i] = sc.nextInt();
		    } 
		    int count1 = 0, count2 = 0;
		    for(int i = 0; i<7; i++){
		        if(ar[i]==0)
		        count1++;
		        else
		        count2++;
		    }
		    if(count1>count2)
		    System.out.println("NO");
		    else
		    System.out.println("YES");
		}
	}
}
