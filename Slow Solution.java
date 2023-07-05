//Slow Solution

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
		    int mt = sc.nextInt();
		    int mn = sc.nextInt();
		    int sn = sc.nextInt();
		    int x = sn;
		    int count = 0;
		    int i = 0;
		    while(x != 0){
		        if(x>=mn){
		            x = x - mn;
		            i++;
		            count++;
		        }
		        else{
		            x = x - x;
		            i++;
		            count++;
		        }
		        //System.out.println(i);
		        if(i == mt){
		        //System.out.println("ok");
		        break;
		        }
		    }
		    int sum = 0;
		    //int ar[] = new int [count];
		    int y = sn;
		    for (int j = 0;j < count ;j++ ){
		        if(y>=mn){
		            y = y - mn;
		            sum += mn*mn;
		        }
		        else{
		            sum += y*y;
		        }
		    }
		    System.out.println(sum);
		}
	}
}
