//Mario and the Broken String

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
		    String s = sc.next();
		    boolean check = true;
		    for (int i=0;i<n/2 ;i++ ){
		        if(s.charAt(i) != s.charAt(n/2+i)){
		            check = false;
		            break;
		        }
		    }
		    if(check)
		    System.out.println("YES");
		    else
		    System.out.println("NO");
		}
	}
}
