import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        String[] subStr = s.split("");
        StringBuffer sb;
        
        while (subStr.length > 1){
            int cnt = 0;
            for (int i = 0; i < subStr.length; i++){
        
                if (subStr[i].equals("0")){
                    cnt++;
                }
            }
            String newStr = Integer.toBinaryString(subStr.length - cnt);
            subStr = newStr.split("");
            answer[1] += cnt;
            answer[0]++;
        }
        
        return answer;
    }
}