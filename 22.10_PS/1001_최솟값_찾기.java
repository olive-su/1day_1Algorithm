// boj. 11003

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        
        Deque<Node> deque = new LinkedList<>();
        Node frontNode;
        Node rearNode;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        deque.add(new Node(0, arr[0]));
        sb.append(arr[0]);

        for (int i = 1; i < n; i++) {
            frontNode = deque.peekFirst();
            rearNode = deque.peekLast();
            if (frontNode.index <= i - l) {
                deque.pollFirst();
            }
            while (!deque.isEmpty() && rearNode.value >= arr[i]) {
                deque.pollLast();
                rearNode = deque.peekLast();
            }
            deque.add(new Node(i, arr[i]));
            frontNode = deque.peekFirst();

            sb.append(' ');
            sb.append(frontNode.value);
        }

        System.out.println(sb);

    }

    static class Node {
        public int index;
        public int value;

        Node(int index, int value) {
            this.index = index;
            this.value = value;
        }
    }
}
