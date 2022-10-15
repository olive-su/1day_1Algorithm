// boj. 1167
// BFS

import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Node>[] tree;
    static int[] weightArray;
    static boolean[] visited;

    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int v = Integer.parseInt(st.nextToken());

        tree = new ArrayList[v + 1];
        visited = new boolean[v + 1];
        weightArray = new int[v + 1];


        for (int i = 1; i < v + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());

            tree[num] = new ArrayList<>();
            while (true) {
                int a = Integer.parseInt(st.nextToken());
                if (a == -1) {
                    break;
                }
                int b = Integer.parseInt(st.nextToken());

                tree[num].add(new Node(a, b));
            }
        }

        int nextStep = BFS(1);

        visited = new boolean[v + 1];
        weightArray = new int[v + 1];
        int answer = BFS(nextStep);

        System.out.println(weightArray[answer]);
    }

    static int BFS(int n) {
        int maxVertex = n;
        int maxValue = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(n);
        visited[n] = true;

        while (!queue.isEmpty()) {
            int a = queue.poll();
            for (Node t : tree[a]) {
                int v = t.vertex;
                int w = t.weight;

                if (!visited[v]) {
                    visited[v] = true;
                    queue.add(v);
                    weightArray[v] = weightArray[a] + w;
                    if (weightArray[v] > maxValue) {
                        maxValue = weightArray[v];
                        maxVertex = v;
                    }
                }
            }
        }

        return maxVertex;
    }

    static class Node {
        public int vertex;
        public int weight;

        Node(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }
    }
}
