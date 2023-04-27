import java.util.*;

public class Solution {
    public int solution(int n) {
        int ans = 0;
        while (n > 0){
            if (n % 2 == 0)
                n = n / 2;
            else{
                n--;
                ans++;
            }
        }
        return ans;
    }
}

/** DP 방식 - 효율성 불통
public class Solution {
    public int solution(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i < n + 1; i++){
            dp[i] = (int)1e9;
        }
        
        for (int i = 0; i < n; i++){
            dp[i + 1] = Math.min(dp[i + 1], dp[i] + 1);
            
            if (i * 2 < n + 1){
                dp[i * 2] = Math.min(dp[i * 2], dp[i]);
            }
        }
        
        return dp[n];
    }
}
 */