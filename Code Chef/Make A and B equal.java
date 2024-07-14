//Make A and B equal

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
		    boolean check = false;
		    if(a == b)
		    check = true;
		    else if(a<b){
		        while(a<=b){
		            if(a == b){
		            check = true;
		            break;
		            }
		            a *= 2;
		        }
		    }
		    else
		    {
		        while(b<=a){
		            if(a == b){
		            check = true;
		            break;
		            }
		            b *= 2;
		        }
		    }
		    if(check)
		    System.out.println("YES");
		    else
		    System.out.println("NO");
		}
	}
}
