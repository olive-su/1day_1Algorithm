// boj. 1747

import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int MAX_VALUE = (int)1e7;
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[MAX_VALUE + 1];
        arr[0] = 1;
        arr[1] = 1;

        for (int i = 0; i <= Math.sqrt(MAX_VALUE); i++) {
            if (arr[i] == 0) {
                int num = 2;
                while (i * num <= MAX_VALUE) {
                    arr[i * num] = 1;
                    num ++;
                }
            }
        }

        for (int j = n; j <= MAX_VALUE; j++) {
            if (arr[j] == 0 && isPalindrome(j)) {
                System.out.println(j);
                break;
            }
        }

    }

    static boolean isPalindrome(int number) {
        String param = Integer.toString(number);
        String[] pArr = param.split("");
        int idx = 0;
        while (idx <= pArr.length / 2) {
            if (!pArr[idx].equals(pArr[pArr.length - 1 - idx]))
                return false;
            idx++;
        }
        return true;
    }
}