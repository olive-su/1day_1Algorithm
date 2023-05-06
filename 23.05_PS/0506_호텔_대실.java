// time: 23'

import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        int[] time = new int[60 * 24];
        
        for (int i = 0; i < book_time.length; i++){
            String[] start = book_time[i][0].split(":");
            String[] end = book_time[i][1].split(":");
            int startTime = 60 * Integer.parseInt(start[0]) + Integer.parseInt(start[1]);
            int endTime = 60 * Integer.parseInt(end[0]) + Integer.parseInt(end[1]) + 10;
            
            for(int j = startTime; j < endTime; j++){
                int t = j % 1440;
                time[t]++;
            }
        }
        
        for (int i = 0; i < (60 * 24); i++){
            answer = Math.max(answer, time[i]);
        }
        
        return answer;
    }
}