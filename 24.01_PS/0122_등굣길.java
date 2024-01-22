import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] graph = new int[n + 1][m + 1];
        graph[1][1] = 1;
        
        if (puddles.length > 1){
            Arrays.sort(puddles, ((int[] o1, int[] o2) -> {
                    return o1[1] != o2[1] ? o1[1] - o2[1] : o1[0] - o2[0]; // x, y 좌표 바뀐 것 감안
                })
            );
        };
        
        int pIdx = 0;
        for (int i = 1; i < n + 1; i++){
            for (int j = 1; j < m + 1; j++){
                if (i == 1 && j == 1) continue;
                if (pIdx < puddles.length && puddles[pIdx][0] == j && puddles[pIdx][1] == i){
                    graph[i][j] = 0;
                    pIdx++;
                } else {
                    graph[i][j] = (graph[i - 1][j] + graph[i][j - 1]) % 1000000007;
                }           
            }
        }
            
        int answer = graph[n][m];
        return answer;
    }
}


/*
Comparator Override Code

import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] graph = new int[n + 1][m + 1];
        graph[1][1] = 1;
        
        if (puddles.length > 1){
            Arrays.sort(puddles, new Comparator<int[]>() {
                @Override
                public int compare(int[] o1, int[] o2) {
                    return o1[1] != o2[1] ? o1[1] - o2[1] : o1[0] - o2[0]; // x, y 좌표 바뀐 것 감안
                }
            });
        };
        
        
        int pIdx = 0;
        for (int i = 1; i < n + 1; i++){
            for (int j = 1; j < m + 1; j++){
                if (i == 1 && j == 1) continue;
                if (pIdx < puddles.length && puddles[pIdx][0] == j && puddles[pIdx][1] == i){
                    graph[i][j] = 0;
                    pIdx++;
                } else {
                    graph[i][j] = (graph[i - 1][j] + graph[i][j - 1]) % 1000000007;
                }           
            }
        }
            
        int answer = graph[n][m];
        return answer;
    }
}
*/

/*
효율성 테스트 TC6 시간초과 코드

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] graph = new int[n + 1][m + 1];
        graph[1][1] = 1;
        for (int i = 1; i < n + 1; i++){
            for (int j = 1; j < m + 1; j++){
                if (i == 1 && j == 1) continue;
                int[] target = {j, i};
                if (checkPuddles(puddles, target) == true){
                    graph[i][j] = 0;
                } else {
                    graph[i][j] = (graph[i - 1][j] + graph[i][j - 1]) % 1000000007;
                }
                    
            }
        }
            
        int answer = graph[n][m];
        return answer;
    }
    
    boolean checkPuddles(int[][] puddles, int[] target){
        for(int[] p : puddles){
            if (p[0] == target[0] && p[1] == target[1]){
                return true;
            }
        }
        return false;
    }
}
*/