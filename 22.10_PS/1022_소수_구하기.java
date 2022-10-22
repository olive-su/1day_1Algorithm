// boj. 1929

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[] arr = new int[n + 1];
        arr[0] = 1;
        arr[1] = 1;
        for (int i = 2; i <= Math.sqrt(n) + 1; i++) {
            int num = 2;
            if (arr[num] == 0) {
                while (i * num <= n) {
                    arr[i * num] = 1;
                    num++;
                }
            }
        }
        for (int j = m; j <= n; j++) {
            if (arr[j] == 0) {
                System.out.println(j);
            }
        }
    }
}