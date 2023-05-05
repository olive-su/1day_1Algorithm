// time: 24'
// Greedy

class Solution {
    public String solution(String number, int k) {
        StringBuffer sb = new StringBuffer();
        int finalLength = number.length() - k;
        
        while(k > 0 && sb.length() < finalLength){
            for(int i = 9; i > -1; i--){
                char now = (char)(i + '0');
                int place = number.indexOf(now);
                
                if (place != -1 && place <= k){
                    k -= place;
                    sb.append(now);
                    number = number.substring(place + 1);
                    break;
                }
            }
        }
        
        if (sb.length() < finalLength && number.length() > 0){
            sb.append(number);
        }
        String answer = sb.toString();
        
        return answer;
    }
}