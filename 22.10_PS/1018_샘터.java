// boj. 18513

import java.io.*;
import java.util.*;

public class Main {
    static int[] arr;
    static HashMap<Integer, Integer> visited;
    static Queue<Integer> queue;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        arr = new int[n];
        queue = new LinkedList<>();
        visited = new HashMap<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            queue.add(arr[i]);
            visited.put(arr[i], 0);
        }

        System.out.println(BFS(k));
    }

    static long BFS(int k) {
        long result = 0;
        int count = 0;
        while (!queue.isEmpty()) {
            int q = queue.poll();
            for (int i = -1; i < 2; i += 2) {
                if (!visited.containsKey(q + i)) {
                    visited.put((q + i), (visited.get(q) + 1));
                    result += visited.get(q + i);
                    queue.add(q + i);
                    count++;
                }
                if (count == k)
                    return result;
            }
        }
        return result;
    }
}