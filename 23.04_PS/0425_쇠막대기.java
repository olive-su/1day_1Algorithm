// boj. 10799

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] pieces = br.readLine().split("");
        int answer = 0;
        Stack<String> stack = new Stack<>();

        stack.push(pieces[0]);
        for (int i = 1; i < pieces.length; i++) {
            if (pieces[i].equals("(")){
                stack.push("(");
            } else{
                if(pieces[i - 1].equals("(")){
                    stack.pop();
                    answer += stack.size();
                } else {
                    answer += 1;
                    stack.pop();
                }
            }
        }
        System.out.println(answer);
    }
}