// time: 35'

import java.util.*;

class Solution {
    public int[] solution(int n, long left, long right) {
        int[] answer;
        answer = new int[(int)(right - left + 1)];
        
        long num = left;
        
        while (num <= right){
            answer[(int)(num - left)] = Math.max((int)(num / (long)n) + 1, (int)(num % (long)n) + 1);
            num++;
        }
        
        return answer;
    }
}