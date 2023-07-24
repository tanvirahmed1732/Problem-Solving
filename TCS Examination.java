//TCS Examination

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
		    int dd = sc.nextInt();
		    int dt = sc.nextInt();
		    int ddm = sc.nextInt();
		    int sd = sc.nextInt();
		    int st = sc.nextInt();
		    int sdm = sc.nextInt();
		    
		    int dsum = dd + dt + ddm;
		    int ssum = sd + st + sdm;
		    if(dsum>ssum)
		    System.out.println("Dragon");
		    else if(dsum<ssum)
		    System.out.println("Sloth");
		    else{
		        if(dd>sd)
		        System.out.println("Dragon");
		        else if(sd>dd)
		        System.out.println("Sloth");
		        else{
		            if(dt>st)
		            System.out.println("Dragon");
		            else if(st>dt)
		            System.out.println("Sloth");
		            else{
		                System.out.println("Tie");
		            }
		        }
		    }
		    
		}
	}
}
