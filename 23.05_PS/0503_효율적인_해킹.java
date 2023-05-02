import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph;
    static int[] answer;
    static boolean[] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int a, b;
        int v = 0;

        answer = new int[n + 1];
        graph = new ArrayList[n + 1];
        for (int i = 1; i < n + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            graph[b].add(a);
        }

        for (int i = 1; i < n + 1; i++){
            visited = new boolean[n + 1];
            bfs(i);
        }

        for (int i = 1; i < n + 1; i++){
            v = Math.max(v, answer[i]);
        }

        for (int i = 1; i < n + 1; i++){
            if (answer[i] == v) {
                bw.write(i + " ");
            }
        }
        bw.flush();
    }

    static void bfs(int x) {
        int y;
        int cnt = 0;
        visited[x] = true;

        Queue<Integer> queue = new LinkedList<>();
        queue.add(x);

        while (!queue.isEmpty()) {
            y = queue.poll();
            for (int i : graph[y]) {
                if (!visited[i]){
                    queue.add(i);
                    visited[i] = true;
                    answer[x]++;
                }
            }
        }
    }
}