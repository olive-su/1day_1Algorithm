import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] A;
    static boolean[] visited;
    static int count = 1;
    static boolean flag = false;
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int a;
        int b;

        A = new ArrayList[n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            A[i] = new ArrayList<>();
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            A[a].add(b);
            A[b].add(a);
        }


        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                DFS(i, 1);
                if (flag)
                    break;
            }
        }

        if (flag)
            System.out.println(1);
        else
            System.out.println(0);
    }

    static void DFS(int n, int sum){
        if (sum == 5 || flag) { // depth 가 5 이상이면 무조건 중단
            flag = true;
            return;
        }
        visited[n] = true;

        for (int i : A[n]){
            if (!visited[i]){
                DFS(i, sum + 1);
            }
        }
        visited[n] = false;
    }
}
