// boj. 2023
// 시간초과(11%) : 단순 반복문
package main;

import java.io.*;

public class boj_2023 {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int num = (int)Math.pow(10, (n - 1)); // 1000
        int divNum;

        boolean flag;
        for (int j = num; j < num * 10; j++) {
            divNum = num;
            flag = true;
            if (IsPrime(j)) {
                while (divNum > 1) {
                    if (!IsPrime(j / divNum)) {
                        flag = false;
                        break;
                    }
                    divNum /= 10;
                }
                if (flag)
                    System.out.println(j);
            }
        }

        br.close();

    }
    static boolean IsPrime(int n) {
        if (n == 1){
            return false;
        }
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
