//Id and Ship

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
		    char c = sc.next().charAt(0);
		    if(c == 'B' || c == 'b')
		    System.out.println("BattleShip");
		    else if (c == 'C' || c == 'c')
		    System.out.println("Cruiser");
		    if(c == 'D' || c == 'd')
		    System.out.println("Destroyer");
		    else if (c == 'F' || c == 'f')
		    System.out.println("Frigate");
		}
	}
}
