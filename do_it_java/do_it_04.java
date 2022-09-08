// boj. 11660
// 시간 초과

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class do_it_04 {
    public static void main(String args[]) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());

        int[][] numArr = new int[n][n];
        for (int i = 0; i < n; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            for (int j = 0; j < n; j++) {
                numArr[i][j] = Integer.parseInt(stringTokenizer.nextToken());
            }
        }

        int[] coordinate = new int[4];
        int sum;
        for (int i = 0; i < m; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            sum = 0;
            for (int j = 0; j < 4; j++) {
                coordinate[j] = Integer.parseInt(stringTokenizer.nextToken()) - 1;
            }

            for (int k = coordinate[0]; k <= coordinate[2]; k++){
                for (int l = coordinate[1]; l <= coordinate[3]; l++) {
                    sum += numArr[k][l];
                }
            }
            System.out.println(sum);
        }
    }
}
