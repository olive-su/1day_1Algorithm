// boj. 1976

import java.io.*;
import java.util.*;

public class Main {
    public static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        arr = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            arr[i] = i;
        }

        for (int i = 1; i < n + 1; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n + 1; j++) {
                int a = Integer.parseInt(st.nextToken());
                if (a == 1) {
                    union(i, j);
                }
            }
        }

        String[] inputStr = br.readLine().split(" ");
        int start = Integer.parseInt(inputStr[0]);
        for (int i = 1; i < inputStr.length; i++){
            int end = Integer.parseInt(inputStr[i]);
            if (find(start) != find(end)) {
                System.out.println("NO");
                return;
            }
            start = end;
        }

        System.out.println("YES");
    }

    static void union(int a, int b){
        a = find(a);
        b = find(b);
        if (a != b) {
            arr[b] = a;
        }
    }

    static int find(int a){
        while (arr[a] != a){
            a = arr[a];
        }
        return a;
    }
}
