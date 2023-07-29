//CodeChef Streak

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
		    int addy[] = new int [n];
		    int maxa = 0, tempa = 0;
		    for (int i =0;i<n ;i++){
		    addy[i] = sc.nextInt();
		    tempa+=1;
		    if(addy[i] ==0){
		        if(tempa>maxa)
		        maxa = tempa-1;
		    tempa =0;
		    }
		    if(i == n-1){
		        if(tempa>maxa)
		        maxa = tempa;
		    }
		    }
		    int om[] = new int [n];
		    int maxo = 0,tempo = 0;
		    for (int j =0;j<n ;j++ ){
		    om[j] = sc.nextInt();
		    tempo+=1;
		    if(om[j] ==0){
		        if(tempo>maxo)
		        maxo = tempo-1;
		    tempo =0;
		    }
		    if(j == n-1){
		        if(tempo>maxo)
		        maxo = tempo;
		    }
		    }
		    //System.out.println(maxa);
		    //System.out.println(maxo);
		    if(maxa> maxo)
		    System.out.println("Om");
		    else if(maxa == maxo)
		    System.out.println("Draw");
		    else
		    System.out.println("Addy");
		}
	}
}
