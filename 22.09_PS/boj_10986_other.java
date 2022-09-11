// boj. 10986

import java.io.*;
import java.util.*;

public class boj_10986_other {
    public static void main(String args[]) throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        long[] sumArr = new long[n];
        long[] countArr = new long[m];
        long answer = 0;

        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        sumArr[0] = Long.parseLong(stringTokenizer.nextToken());
        for (int i = 1; i < n; i++) {
            sumArr[i] = sumArr[i - 1] + Long.parseLong(stringTokenizer.nextToken());
        }

        for (int i = 0; i < n; i++) {
            countArr[(int)(sumArr[i] % m)]++;
        }
        answer += countArr[0];

        for (int i = 0; i < m; i++) {
            if (countArr[i] > 1) {
                answer += countArr[i] * (countArr[i] - 1) / 2;
            }
        }
        System.out.println(answer);
    }
}