// time: 38'
// BFS

import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        
        int n = maps.length;
        int m = maps[0].length;
        int[][] visited = new int[n][m];
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        Queue<Place> queue = new LinkedList<>();
        queue.add(new Place(0, 0));
        visited[0][0] = 1;

        while (!queue.isEmpty()){
            Place now = queue.poll();
            int y = now.y;
            int x = now.x;
            for (int i = 0; i < 4; i++){
                int ny = y + dy[i];
                int nx = x + dx[i];
                if (0 <= nx && nx < m && 0 <= ny && ny < n){
                    if (maps[ny][nx] == 1 && visited[ny][nx] == 0){
                        visited[ny][nx] = visited[y][x] + 1;
                        
                        queue.add(new Place(ny, nx));
                    }
                }
            }
        }
        
        answer = (visited[n - 1][m - 1] == 0) ? -1 : visited[n - 1][m - 1];
        
        return answer;
    }
}

class Place{
    int x;
    int y;
    
    Place(int y, int x){
        this.x = x;
        this.y = y;
    }
    
}