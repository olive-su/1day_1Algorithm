// boj. 11659

import java.util.Scanner;

public class boj_11659 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int sum = 0;
        int t;

        int a[] = new int[n + 1];
        a[0] = 0;
        for (int i = 1; i < n + 1; i++){
            t = sc.nextInt();
            sum += t;
            a[i] = sum;
        }
        for (int i = 0; i < m; i++){
            int j = sc.nextInt() - 1;
            int k = sc.nextInt();
            System.out.println(a[k] - a[j]);
        }
    }
}

