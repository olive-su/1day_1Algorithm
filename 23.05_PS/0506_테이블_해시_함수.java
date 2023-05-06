// time: 20'

import java.util.*;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int answer = 0;
        
        Arrays.sort(data, (int[] o1, int[] o2) -> {
            if(o1[col - 1] == o2[col - 1]){
                return o2[0] - o1[0];
            }
            return o1[col - 1] - o2[col - 1];
        });
        
        answer = sumRow(row_begin, data[row_begin - 1]);
        
        for (int i = row_begin; i < row_end; i++){
            int newSumRow = sumRow(i + 1, data[i]);
            answer = answer ^ newSumRow;
        }
            
        return answer;
    }
    
    int sumRow(int n, int[] row){
        int rst = 0;
        
        for (int r : row){
            rst += (r % n);
        }
        return rst;
    }
}