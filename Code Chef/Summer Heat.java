//Summer Heat

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
		    int xa = sc.nextInt();
		    int xb = sc.nextInt();
		    int Xa = sc.nextInt();
		    int Xb = sc.nextInt();
		    int sum = 0;
		    if(Xa % xa == 0){
		        sum += Xa/ xa;
		    }
		    else
		    sum += Xa/xa + 1;
		    if(Xb % xb == 0)
		    sum+= Xb/xb;
		    else
		    sum+=Xb/xb + 1;
		    System.out.println(sum);
		}
	}
}
