// boj. 1715

import java.io.*;
import java.util.*;

public class Main {
    static PriorityQueue<Integer> priorityQueue  = new PriorityQueue<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;
        int n = Integer.parseInt(br.readLine());
        priorityQueue = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            priorityQueue.add(Integer.parseInt(br.readLine()));
        }

        while (priorityQueue.size() > 1) {
            int target = priorityQueue.poll() + priorityQueue.poll();
            priorityQueue.add(target);
            answer += target;
        }

        System.out.println(answer);
    }
}