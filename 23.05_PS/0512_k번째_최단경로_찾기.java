// boj. 1854

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n, m, k; // n: 도시 개수, m:  도로 개수, k: k번째 도시
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        boolean[] visited = new boolean[n + 1];
        ArrayList<Node>[] graph = new ArrayList[n + 1];
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>((o1, o2) -> {
            int w1 = o1.weight;
            int w2 = o2.weight;

            return w1 - w2;
        });
        PriorityQueue<Integer>[] distance = new PriorityQueue[n + 1];
        for (int i = 1; i < n + 1; i++){
            graph[i] = new ArrayList<>();
            distance[i] = new PriorityQueue<>((o1, o2) -> {
                int w1 = o1;
                int w2 = o2;

                return w2 - w1;
            });
        }

        int a, b, c;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            graph[a].add(new Node(b, c));
        }
        distance[1].add(0);
        priorityQueue.add(new Node(1, 0));

        while(!priorityQueue.isEmpty()){
            Node target = priorityQueue.poll();
            int now = target.node;
            int cost = target.weight;

            for (Node next : graph[now]) {
                if (distance[next.node].size() < k) {
                    distance[next.node].add(cost + next.weight);
                    priorityQueue.add(new Node(next.node, cost + next.weight));
                }
                else if (distance[next.node].peek() > cost + next.weight){
                    distance[next.node].poll();
                    distance[next.node].add(cost + next.weight);
                    priorityQueue.add(new Node(next.node, cost + next.weight));
                }
            }

        }

        for (int i = 1; i < n + 1; i++) {
            if (distance[i].size() == k)
                System.out.println(distance[i].poll());
            else {
                System.out.println(-1);
            }
        }
    }

}

class Node{
    int node;
    int weight;

    Node(int _node, int _weight) {
        this.node = _node;
        this.weight = _weight;
    }
}
