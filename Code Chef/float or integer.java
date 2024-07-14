// float or integer
package com.mycompany.problemsolving;

import java.util.Scanner;

public class float_or_integer_number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.next();
        int dump = n.length();
        for (int i = 0; i < n.length(); i++) {
            if(n.charAt(i) == '.')
                dump = i;
        }
        boolean check = true;
        for (int i = dump+1; i < n.length(); i++) {
            if(n.charAt(i) != '0'){
                check = false;
                break;
            }
        }
        String a = "";
        if(check){
            for (int i = 0; i < dump; i++) {
                a += n.charAt(i);
            }
            System.out.println("int "+a);
        }
        String b = "";
        if(check == false){
            for (int i = 0; i < dump; i++) {
                a += n.charAt(i);
            }
            b += '0';
            for (int i = dump; i < n.length(); i++) {
                b += n.charAt(i);
            }
            System.out.println("float " +a+ " " +b);
        }
    } 
}
