// boj. 11399
// 삽입 정렬

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException{
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int answer = 0;
        int[] arr = new int[n];
        int[] answerArr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 1; i < n; i++) { // 삽입 위치 찾기
            int target = arr[i];
            int idx = i;
            for (int j = 0; j < i; j++) {
                if (target < arr[j]) {
                    idx = j;
                    break;
                }
            }

            int tmp = target;
            for (int k = idx; k < i + 1; k++){ // 삽입 위치부터 뒤로 한 칸씩 밀기
                int v = arr[k];
                arr[k] = tmp;
                tmp = v;
            }
        }

        for (int i = 0; i < n; i++) {
            answer += arr[i];
            for (int j = 0; j < i; j++) {
                answer += arr[j];
            }
        }

        System.out.println(answer);
    }
}