//Wordle

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		while(T-->0){
		    String s = sc.next();
		    String t = sc.next();
		    StringBuilder m = new StringBuilder();
		    for (int i =0;i<5 ;i++ ){
		        if(s.charAt(i) == t.charAt(i))
		        m.append('G');
		        else
		        m.append('B');
		    }
		    System.out.println(m);
		}
	}
}
