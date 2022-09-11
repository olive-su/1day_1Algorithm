// boj. 2018

import java.io.*;
import java.util.*;

public class boj_2018 {
    public static void main(String args[]) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int answer = 1;
        int start = 1;
        int end = 1;
        int sum = 1;

        while (end != n){
            if (sum == n) {
                answer++;
                end++;
                sum += end;
            } else if (sum < n) {
                end++;
                sum += end;
            } else {
                sum -= start;
                start++;
            }
        }

        System.out.println(answer);

    }
}
