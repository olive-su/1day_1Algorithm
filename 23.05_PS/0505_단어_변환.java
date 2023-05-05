// bfs
// time: 35'

import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        HashMap<String, Integer> wordsDict = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(begin);
            
        for (String w : words){
            wordsDict.put(w, 0);
        }
        wordsDict.put(begin, 1);
        wordsDict.put(target, 0);
        
        while(!queue.isEmpty()){
            String x = queue.poll();
            int cnt = wordsDict.get(x);
            for (String w : words){
                
                if (wordsDict.get(w) == 0 && posWord(x, w)){
                    queue.add(w);
                    wordsDict.put(w, cnt + 1);
                }
            }
        }
        
        answer = wordsDict.get(target);
        if (answer > 0) answer--;
        
        return answer;
    }
    
    boolean posWord (String dest, String src){
        String targetDest;
        String targetSrc;

        boolean rst = false;
        
        for (int i = 0; i < dest.length(); i++){
            boolean[] flag = {false, false};
            
            targetDest = dest.substring(0, i);
            targetSrc = src.substring(0, i);
            
            if (targetDest.equals(targetSrc))
                flag[0] = true;
            
            targetDest = dest.substring(i + 1);
            targetSrc = src.substring(i + 1);
            
            if (targetDest.equals(targetSrc))
                flag[1] = true;
            
            if (flag[0] == true && flag[1] == true){
                rst = true;
                break;
            }
        }
        
        return rst;
    }
}