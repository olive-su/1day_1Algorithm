// boj. 18352

import java.io.*;
import java.util.*;

public class Main {
    static int[] visited;
    static ArrayList<Integer>[] graph;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuffer sb = new StringBuffer();

        int n;
        int m;
        int k;
        int x;
        int a;
        int b;

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n + 1];
        for (int i = 0; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            graph[a].add(b);
        }

        visited = new int[n + 1];

        bfs(x);

        for (int i = 1; i < n + 1; i++) {
            if (visited[i] - 1 == k) {
                sb.append(i);
                sb.append('\n');
            }
        }
        if (sb.toString().equals("")){
            System.out.print(-1);
        } else {
            System.out.print(sb);
        }

    }

    static void bfs(int n){
        int cnt = 1;
        visited[n] = cnt;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);

        while (!queue.isEmpty()) {
            int x = queue.poll();
            for (int i = 0; i < graph[x].size(); i++) {
                int t = graph[x].get(i);
                if (visited[t] == 0){
                    visited[t] = visited[x] + 1;
                    queue.add(t);
                }
            }
        }
    }
}