// time: 22'
// 구간 합
import java.util.*;

class Solution {
    public int solution(int n) {
        int answer = 1;
        int sumValue;
        int[] sumArr = new int[(n / 2) + 2];
        for (int i = 1; i < (n / 2) + 2; i++){
            sumArr[i] = sumArr[i - 1] + i;
        }
        
        for (int i = (n / 2) + 1; i > 1; i--){
            int num = i - 2;
            sumValue = sumArr[i] - sumArr[num];
            
            while (sumValue <= n){
                if (sumValue == n){
                    answer++;
                    break;
                }
                num--;
                if (num < 0) break;
                sumValue = sumArr[i] - sumArr[num];
            }
        }
        
        return answer;
    }
}