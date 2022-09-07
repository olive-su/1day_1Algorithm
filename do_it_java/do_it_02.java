// boj.1546

import java.util.Scanner;

public class do_it_02 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a[] = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        double sum = 0.0;
        long max = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] > max)
                max = a[i];
        }
        for (int i = 0; i < n; i++) {
            sum += (double)a[i] / max * 100;
        }
        System.out.print(sum / n);
    }
}
