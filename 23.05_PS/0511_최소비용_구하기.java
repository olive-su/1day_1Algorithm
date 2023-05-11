// boj. 1916

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int a, b, w;
        int src, dest;
        ArrayList<Node>[] arr = new ArrayList[n + 1];
        int[] distances = new int[n + 1];
        boolean[] visited = new boolean[n + 1];

        PriorityQueue<Node> priorityQueue  = new PriorityQueue<>((n1, n2) -> {
                    int w1 = n1.weight;
                    int w2 = n2.weight;
                return w1 - w2;
        });

        for (int i = 1; i < n + 1; i++) {
            arr[i] = new ArrayList<>();
        }

        for (int i = 1; i < n + 1; i++) {
            distances[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            w = Integer.parseInt(st.nextToken());
            arr[a].add(new Node(b, w));
        }

        st = new StringTokenizer(br.readLine());
        src = Integer.parseInt(st.nextToken());
        dest = Integer.parseInt(st.nextToken());

        distances[src] = 0;

        priorityQueue.add(new Node(src, 0)); // node, cost

        while (!priorityQueue.isEmpty()){
            Node target = priorityQueue.poll();
            int now = target.node;
            int cost = target.weight;

            if (!visited[now]) {
                visited[now] = true;
                for (Node next : arr[now]) {
                    if (!visited[next.node] && distances[next.node] > cost + next.weight) {
                        distances[next.node] = cost + next.weight;
                        priorityQueue.add(new Node(next.node, cost + next.weight));
                    }
                }
            }
        }

        bw.write(distances[dest] + "\n");
        bw.flush();
        bw.close();
        br.close();
    }

}

class Node {
    int node;
    int weight;

    Node(int _node, int _weight){
        this.node = _node;
        this.weight = _weight;
    }
}
