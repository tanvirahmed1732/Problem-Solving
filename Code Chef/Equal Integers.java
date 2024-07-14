//Equal Integers

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
		    int x = sc.nextInt();
		    int y = sc.nextInt();
		    if(x == y)
		    System.out.println("0");
		    else if(x<y){
		        System.out.println(y-x);
		    }
		    else
		    {
		        if(x%2 != 0 && y%2 != 0){
		            System.out.println((x - y)/2);
		        }
		        else if(x%2 == 0 && y%2 == 0)
		        System.out.println((x-y)/2);
		        else{
		            System.out.println(((x-y+1)/2)+1);
		        }
		    }
		}
	}
}
