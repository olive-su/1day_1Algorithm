// boj. 1456

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        int c = (int)Math.sqrt(b);
        long answer = 0;

        long[] arr = new long[c + 1];
        arr[0] = 1;
        arr[1] = 1;

        for (int i = 2; i < Math.sqrt(c); i++) {
            if (arr[i] == 0) {
                int num = 2;
                while (i * num <= c) {
                    arr[i * num] = 1;
                    num++;
                }
            }
        }
수
        for (int j = 2; j <= c; j++) {
            double powNum = 2;
            if (arr[j] == 0) {
                while (Math.pow(j, powNum) <= b) {
                    if (Math.pow(j, powNum) >= a)
                        answer++;
                    powNum++;
                }
            }
        }
        System.out.println(answer);
    }
}