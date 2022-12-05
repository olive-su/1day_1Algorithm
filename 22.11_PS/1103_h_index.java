import java.util.*;

class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        int maxV = 0;

        for (int i = 0; i < citations.length; i++) {
            maxV = Math.max(maxV, citations[i]);
        }

        for (int i = 1; i < maxV; i++) {
            int cnt = 0;
            for (int j = 0; j < citations.length; j++) {
                if (i <= citations[j])
                    cnt++;
            }
            if (cnt >= i)
                answer = Math.max(answer, i);
        }
        return answer;
    }
}