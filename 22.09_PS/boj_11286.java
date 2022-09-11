// boj. 11286

import java.io.*;
import java.util.*;

public class boj_11286 {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>((o1, o2) -> {
            int fAbs = Math.abs(o1);
            int sAbs = Math.abs(o2);
            if (fAbs == sAbs) {
                return o1 > o2 ? 1 : -1;
            } else {
                return fAbs - sAbs;
            }
        });

        for (int i = 0; i < n; i++) {
            int command = Integer.parseInt(br.readLine());
            if (command == 0) {
                if (queue.isEmpty())
                    System.out.println(0);
                else
                    System.out.println(queue.poll());
            } else {
                queue.add(command);
            }
        }
    }
}
