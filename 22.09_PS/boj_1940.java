// boj. 1940

import java.io.*;
import java.util.*;

public class boj_1940 {
    public static void main(String args[]) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bufferedReader.readLine());
        int m = Integer.parseInt(bufferedReader.readLine());
        int[] numArr = new int[n];
        int start = 0;
        int end = n - 1;
        int sum;
        int answer  = 0;

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 0; i < n; i++) {
            numArr[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        Arrays.sort(numArr);
        while (start != end) {
            sum = numArr[start] + numArr[end];
            if( sum == m ){
                answer++;
                end--;
            } else if (sum < m){
                start++;
            } else {
                end--;
            }
        }

        System.out.println(answer);

    }
}
