import java.util.*;

class Solution {
    boolean solution(String s) {
        int cnt = 0;
        
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == '(')
                cnt++;
            else {
                cnt--;
                if (cnt < 0) return false;
            }
        }
        if (cnt == 0) return true;
        else return false;
    }
}

/** split 사용 - 효율성 불통
 import java.util.*;

class Solution {
    boolean solution(String s) {
        int cnt = 0;
        
        String[] newStr = s.split("");
        for (int i = 0; i < newStr.length; i++){
            if (newStr[i].equals("("))
                cnt++;
            else {
                cnt--;
                if (cnt < 0) return false;
            }
        }
        if (cnt == 0) return true;
        else return false;
    }
}
 */