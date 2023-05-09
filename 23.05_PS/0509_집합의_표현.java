// boj. 1717
// union-find
// time: 40'

import java.io.*;
import java.util.*;

public class Main {
    public static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x, a, b;

        arr = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            arr[i] = i;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            if (x == 0){
                union(a, b);
            } else {
                if (findOpt(a) == findOpt(b)){
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }

    // 기존 방식 대로 -> 연결 관계가 끊어질 수 있음..!
    static void union(int a, int b) {
        a = findOpt(a);
        b = findOpt(b);
        if (a != b)
            arr[b] = a;
    }

    static int findOpt(int x){
        if (x == arr[x])
            return x;
        else
            return arr[x] = findOpt(arr[x]);
    }
}
