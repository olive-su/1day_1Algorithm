// boj. 1541

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<String> arr = new ArrayList<>();
        String[] input = br.readLine().split("");
        int answer = 0;
        int now = 0;

        String number = "";
        for (String i : input) {
            if (i.equals("-") || i.equals("+")) { // 연산자와 피연산자 분리
                arr.add(number);
                number = "";
                arr.add(i);
            } else {
                number += i;
            }
        }
        arr.add(number);

        for (int i = arr.size() - 1; i >= 0; i--) { // 뒤에서부터 반복문 돌며 숫자끼리 더하고 '-'가 나오면 감산해줌
            if (arr.get(i).equals("-")) {
                answer -= now;
                now = 0;
            } else if (arr.get(i).equals("+")) {
              continue;
            } else {
                now += Integer.parseInt(arr.get(i));
            }
        }
        answer += now;
        System.out.println(answer);

    }
}