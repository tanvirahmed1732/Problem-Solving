//Nearest Court

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
		    int sum = 0;
		    if(x<=y)
		    sum = y - x;
		    else
		    sum = x - y;
		    if(sum%2 == 0)
		    sum = sum / 2;
		    else
		    sum = sum / 2 + 1;
		    System.out.println(sum);
		}
	}
}
