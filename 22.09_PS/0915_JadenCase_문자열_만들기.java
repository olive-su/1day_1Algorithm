import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuffer sb = new StringBuffer();
        s = s.toLowerCase();
        char[] cArr = s.toCharArray();
        sb.append(Character.toString(cArr[0]).toUpperCase());

        for (int i = 1; i < s.length(); i++){
            if (cArr[i - 1] == ' ') {
                sb.append(Character.toString(cArr[i]).toUpperCase());
            } else {
                sb.append(cArr[i]);
            }
        }
        return sb.toString();
    }
}