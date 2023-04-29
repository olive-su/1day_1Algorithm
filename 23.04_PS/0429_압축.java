import java.util.*;

class Solution {
    public int[] solution(String msg) {
        int[] a;
        LinkedList<Integer> answer = new LinkedList<>();
        String[] s = msg.split("");
        StringBuffer sb;
        HashMap<String, Integer> alpha = new HashMap<>();
        for (int i = 0; i < 26; i++){
            char ascii = (char)((int)'A' + i);
            alpha.put(Character.toString(ascii), i + 1);
        }
        
        int printIdx = 0;
        int idx = 0;
        while (idx < s.length){
            sb = new StringBuffer();
            sb.append(s[idx]);
            while (alpha.containsKey(sb.toString())){
                printIdx = alpha.get(sb.toString());
                idx++;
                if (idx >= s.length) break;
                sb.append(s[idx]);
            }
            alpha.put(sb.toString(), alpha.size() + 1);
            answer.add(printIdx);
        }
        
        a = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++){
            a[i] = answer.get(i);
        }
        
        return a;
    }
}