// boj. 11724

import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] A;
    static boolean visited[];
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int u;
        int v;
        A = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        for (int i = 1; i < n + 1; i++) {
            A[i] = new ArrayList<>(); // 인접 리스트 초기화
        }

        for (int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            u = Integer.parseInt(st.nextToken());
            v = Integer.parseInt(st.nextToken());
            A[u].add(v); // 양방향 연결
            A[v].add(u);
        }
        int count = 0;

        for (int i = 1; i < n + 1; i++) {
            if (!visited[i]) {
                count++;
                DFS(i);
            }
        }
        System.out.println(count);


    }
    static void DFS(int v) {
        if (visited[v]) {
            return;
        }
        visited[v] = true;
        for (int i : A[v]) {
            if (visited[i] == false) {
                DFS(i);
            }
        }
    }
}
