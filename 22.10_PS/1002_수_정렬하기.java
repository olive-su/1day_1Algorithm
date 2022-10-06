// boj. 2750
// 버블정렬

import java.io.*;
import java.util.*;

public class Main {
    static int[] arr;
    public static void ma기n(String args[]) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        arr = new int[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - 1 - i; j++) {
                Swap(j, j+1);
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.println(arr[i]);
        }

    }

    static void Swap(int i, int j) {
        int tmp;
        if (arr[i] > arr[j]){
            tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }
    }
}