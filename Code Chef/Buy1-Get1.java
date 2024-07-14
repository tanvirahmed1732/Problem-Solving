//Buy1-Get1
import java.util.*;
class Codechef
{
	public static void main (String[] args)
	{
		 Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-->0){

            String str = sc.next();
            int n = str.length();
            HashMap<Character,Integer> hm = new HashMap<>();
            for(int j=0;j<n;j++){
                if(!hm.containsKey(str.charAt(j))){
                    hm.put(str.charAt(j),1);
                }
                else{
                    hm.put(str.charAt(j),hm.get(str.charAt(j))+1);
                }
            }
            int c=0;
            for(char key:hm.keySet()){
                if(hm.get(key)%2==0){
                    c =c+ (hm.get(key)/2);
                }
                else{
                    c = c + ((hm.get(key)+1)/2);
                }
            }
            System.out.println(c);


        }
	}
}
