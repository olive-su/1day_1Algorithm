// boj. 12891

import java.io.*;
import java.util.*;

public class Main {
    static HashMap<Character, Integer> goal;
    static HashMap<Character, Integer> cnt;
    static char[] dnaArr;

    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int answer = 0;
        dnaArr = "ACGT".toCharArray();
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        char[] str = br.readLine().toCharArray();

        goal = new HashMap<>();
        cnt = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            goal.put(dnaArr[i], Integer.parseInt(st.nextToken()));
            cnt.put(dnaArr[i], 0);
        }

        for (int i = 0; i < p; i++) {
            char target = str[i];
            cnt.put(target, cnt.get(target) + 1);
        }

        if (validation())
            answer++;

        for (int i = 0; i < s - p; i++) {
            char head = str[i];
            char tail = str[p + i];

            cnt.put(head, cnt.get(head) - 1);
            cnt.put(tail, cnt.get(tail) + 1);

            if (validation())
                answer++;
        }

        System.out.println(answer);
    }

    static boolean validation(){
        for (int i = 0; i < 4; i++) {
            char dna = dnaArr[i];
            if (cnt.get(dna) < goal.get(dna))
                return false;
        }
        return true;
    }
}
