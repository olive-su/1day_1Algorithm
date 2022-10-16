// boj. 1920

import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] compareArray;
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        compareArray = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            compareArray[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(compareArray);

        st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            System.out.println(binarySearch(Integer.parseInt(st.nextToken())));
        }
    }

    static int binarySearch(int target) {
        int start = 0;
        int end = n - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (compareArray[mid] == target)
                return 1;
            else if (compareArray[mid] > target)
                end = mid - 1;
            else
                start = mid + 1;
        }
        return 0;
    }
}