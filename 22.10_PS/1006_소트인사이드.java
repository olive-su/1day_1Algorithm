// boj. 1427
// 선택 정렬

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException{
        Scanner sc = new Scanner(System.in);
        StringBuffer sb = new StringBuffer();
        String[] sArr = sc.next().split("");
        int length = sArr.length;
        int[] iArr = new int[length];

        for (int i = 0; i < length; i++) {
            iArr[i] = Integer.parseInt(sArr[i]);
        }

        for (int i = 0; i < length; i++) {
            int idx = i;
            for (int j = i + 1; j < length; j++) {
                if (iArr[idx] < iArr[j]) {
                    idx = j;
                }
            }
            int tmp = iArr[i];
            iArr[i] = iArr[idx];
            iArr[idx] = tmp;
            sb.append(iArr[i]);
        }
        System.out.println(sb);
    }
}