// boj. 1874

import java.util.*;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        boolean flag = true;
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Stack<Integer> stack = new Stack<>();
        StringBuffer bf = new StringBuffer();

        int num = 1;
        for (int i = 0; i < n; i++){
            int target = arr[i]; // 현재 수열의 수
            if (target >= num) { // num : 오름차순을 지키며 스택에 넣을 다음 수
                while (target >= num) {
                    stack.push(num++);
                    bf.append("+\n");
                }
                stack.pop();
                bf.append("-\n");
            }
            else{
                if (stack.peek() > target){
                    flag = false;
                    break;
                } else {
                    stack.pop();
                    bf.append("-\n");
                }
            }

        }
        if (flag) {
            System.out.println(bf.toString());
        } else {
            System.out.println("NO");
        }
    }
}
