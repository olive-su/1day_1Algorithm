// boj. 10986
// 시간초과

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class do_it_05 {
    public static void main(String args[]) throws IOException{
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        int answer = 0;

        int[] originArr = new int[n + 1];
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        for (int i = 1; i < n + 1; i++){
            originArr[i] = Integer.parseInt(stringTokenizer.nextToken());
        }

        int[] sumArr;
        for (int i = 1; i < n + 1; i++) {
            sumArr = new int[n + 1];
            for (int j = i; j < n + 1; j++) {
                sumArr[j] = sumArr[j - 1] + originArr[j];
                if (sumArr[j] % m == 0){
                    answer += 1;
                }
            }
        }

        System.out.println(answer);
    }
}
