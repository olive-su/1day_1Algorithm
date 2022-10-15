// boj. 2178

import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int m;
    static int[][] graph;
    static int[][] visited;
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {-1, 1, 0, 0};

    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        graph = new int[n][m];
        visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            String[] a = br.readLine().split("");
            for (int j = 0; j < m; j++) {
                graph[i][j] = Integer.parseInt(a[j]);
            }
        }

        BFS(0, 0);

        System.out.println(visited[n-1][m-1]);

    }

    static void BFS(int x, int y){
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(x, y));
        visited[y][x] = 1;
        int nx;
        int ny;

        while (!queue.isEmpty()){
            Node nextElement = queue.poll();
            x = nextElement.x;
            y = nextElement.y;
            for (int i = 0; i < 4; i++) {
               nx = x + dx[i];
               ny = y + dy[i];

                if (0 <= nx && nx < m && 0 <= ny && ny < n) {
                    if (graph[ny][nx] == 1 && visited[ny][nx] == 0) {
                        queue.add(new Node(nx, ny));
                        visited[ny][nx] = visited[y][x] + 1;
                    }
                }
            }
        }
    }

    static class Node {
        public int x;
        public int y;

        Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}
