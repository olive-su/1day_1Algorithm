// boj. 2343

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        int start = 0;
        int end = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            if (start < arr[i]) {
                start = arr[i];
            }
            end += arr[i];
        }

        while (start <= end) {
            int mid = (start + end) / 2;
            int total = 0;
            int count = 0;

            for (int i = 0; i < n; i++) {
                if (arr[i] + total > mid) {
                    total = 0;
                    count++;
                }
                total += arr[i];
            }
            if (total > 0)
                count++;

            if (count > m) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }

        System.out.println(start);
        }
}