
import java.util.*;
class Codechef
{
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){
		    int n = sc.nextInt();
		    int count = 0;
		    while(n!=0){
		    if(n>=100){
		    n = n-100;
		    count++;}
		    else if(n>=50){
		    n=n-50;
		    count++;}
		    else if(n>=10){
		    n=n-10;
		    count++;}
		    else if(n>=5){
		    n=n-5;
		    count++;}
		    else if(n>=2){
		    n=n-2;
		    count++;}
		    else{
		    n=n-1;
		    count++;}
		    }
		    System.out.println(count);
		}
	}
}
