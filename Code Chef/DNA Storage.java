//DNA Storage

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Main {

    public static void main(String[] args) throws java.lang.Exception {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            sc.nextLine();
            String s = sc.nextLine();
            String s2 = "";
            for (int i = 0; i < n; i += 2) {
                if (s.charAt(i) == '0' && s.charAt(i + 1) == '0') {
                    s2+= "A";
                }
                if (s.charAt(i) == '0' && s.charAt(i + 1) == '1') {
                    s2+= "T";
                }
                if (s.charAt(i) == '1' && s.charAt(i + 1) == '0') {
                    s2+= "C";
                }
                if (s.charAt(i) == '1' && s.charAt(i + 1) == '1') {
                    s2+= "G";
                }
            }
            System.out.println(s2);
        }
    }
}
