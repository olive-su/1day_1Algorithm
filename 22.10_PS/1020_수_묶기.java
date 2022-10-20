// boj. 1744

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int answer = 0;
        boolean zeroCount = false;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < n; i++) {
            int t = Integer.parseInt(br.readLine());
            if (t < 0)
                minHeap.add(t);
            else if (t > 0)
                maxHeap.add(t);
            else
                zeroCount = true;
        }

        while (minHeap.size() > 1)
            answer += minHeap.poll() * minHeap.poll();

        if (zeroCount && !minHeap.isEmpty())
            minHeap.poll();

        while (maxHeap.size() > 1) {
            int a = maxHeap.poll();
            int b = maxHeap.poll();
            if (a == 1 || b == 1) {
                answer += a + b;
                break;
            }
            answer += a * b;
        }

        while (!minHeap.isEmpty())
            answer += minHeap.poll();

        while (!maxHeap.isEmpty())
            answer += maxHeap.poll();

        System.out.println(answer);
    }
}