// boj. 2164

import java.util.*;

public class boj_1264 {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            queue.add(i);
        }

        while (queue.size() > 1) {
            queue.remove();
            queue.add(queue.remove());
        }
        System.out.println(queue.remove());
    }
}
