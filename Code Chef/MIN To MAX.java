import java.util.*;
public class Main
{
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		for(int i=0; i<a; i++){
		    int n = sc.nextInt();
		    int A[] = new int[n];
                    int m = Integer.MAX_VALUE;
		    for(int j=0; j<n; j++){
		        A[j] = sc.nextInt();
                        m = Math.min(m, A[j]);
		    }
		    int count =0;
		    for(int k=0; k<n; k++){
		        if(m != A[k]){
		            count++;
		        }
		    }
		    System.out.println(count);
		}
	}
}
