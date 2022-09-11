// boj. 1253
// 복기 : 음수 고려 X, 인덱스 0 제외, numArr[i] 로 value 값을 추출해야하는 데 인덱스값으로 비교

import java.io.*;
import java.util.*;

public class boj_1253 {
    public static void main(String args[]) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bufferedReader.readLine());
        long[] numArr = new long[n];
        int answer = 0;
        int start, end;
        long sum;

        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 0; i < n; i++) {
            numArr[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
        Arrays.sort(numArr);
        for (int i = 0; i < n; i++) {
            start = 0;
            end = n - 1;
            while (start < end) {
                if (start == i){
                    start++;
                    continue;
                } else if (end == i) {
                    end--;
                    continue;
                }

                sum = numArr[start] + numArr[end];
                if (sum == numArr[i]) {
                    answer++;
                    break;
                }
                else if (sum < numArr[i]){
                    start++;
                }
                else {
                    end--;
                }
            }
        }

        System.out.println(answer);
        bufferedReader.close();
    }
}
