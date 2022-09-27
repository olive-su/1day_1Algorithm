// boj. 17298

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[] answer = new int[n];
        int p;
        Stack<Integer> stack = new Stack<>();
        StringBuffer sb = new StringBuffer();

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        stack.push(0);
        for (int i = 1; i < n; i++) {
            if (!stack.empty()){
                p = stack.peek();
                while (arr[i] > arr[p]) {
                    answer[stack.pop()] = arr[i];
                    if (stack.empty())
                        break;
                    p = stack.peek();
                }
            }
            stack.push(i);
        }

        // 나머지
        while (!stack.empty()) {
            answer[stack.pop()] = -1;
        }
        for (int i = 0; i < n; i++) {
            sb.append(answer[i]);
            sb.append(" ");
        }
        System.out.print(sb);
    }
}
