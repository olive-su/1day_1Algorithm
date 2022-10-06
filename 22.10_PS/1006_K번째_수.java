// boj. 11004
// 퀵 정렬

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        quickSort(arr, 0, n - 1, k - 1);
        System.out.println(arr[k-1]);
    }

    public static void quickSort(int[] A, int S, int E, int K) {
        if (S < E) {
            int pivot = partition(A, S, E);
            if (pivot == K)
                return;
            else if (K < pivot)
                quickSort(A, S, pivot - 1, K);
            else
                quickSort(A, pivot + 1, E, K);
        }
    }

    public static int partition(int[] A, int S, int E) {
        if (S + 1 == E) {
            if(A[S] > A[E]) swap(A, S, E);
            return E;
        }
        int M = (S + E) / 2;
        swap(A, S, M);
        int pivot = A[S];
        int i = S + 1, j = E;
        while (i <= j) {
            while (pivot < A[j] && j > 0)
                j--;
            while (pivot > A[i] && i < A.length - 1)
                i++;
            if (i <= j)
                swap(A, i++, j--);
        }
        A[S] = A[j];
        A[j] = pivot;
        return j;
    }

    public static void swap(int[] A, int i, int j) {
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }
}