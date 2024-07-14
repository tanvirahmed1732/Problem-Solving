//Easy Pronunciation

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
		    for (int i = 0;i<n-3 ;i++ ){
		        check = true;
		        for (int j = i ;j< i+4;j++){
		            if(s.charAt(j) == 'a' || s.charAt(j) == 'e' || s.charAt(j) == 'i' || s.charAt(j) == 'o' || s.charAt(j) == 'u'){
		                check = false;
		                break;
		            }
		        }
		        if(check)
		        break;
		    }
		    if(check && n>=4)
		    System.out.println("NO");
		    else
		    System.out.println("YES");
		}
	}
}
