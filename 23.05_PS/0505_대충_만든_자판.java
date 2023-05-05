// time: 17'

import java.util.*;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        
        for (int i = 0; i < targets.length; i++){
            int cnt = 0;
            String[] tarStr = targets[i].split("");
            
            for (String t : tarStr){
                int idx = Integer.MAX_VALUE;
                for (String key : keymap){
                    if (key.indexOf(t) != -1){
                        idx = Math.min(idx, key.indexOf(t));
                    }
                }
                
                if (idx == Integer.MAX_VALUE){
                    cnt = -1;
                    break;
                } else{
                    cnt += (idx + 1);
                }
            }
            
            answer[i] = cnt;
        }
        
        return answer;
    }
}