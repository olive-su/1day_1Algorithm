// time: 29'

class Solution {
    public int[] solution(int[][] arr) {
        int[] answer = {0, 0};
        
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr.length; j++){
                int color = arr[i][j];
                answer[color]++;
            }
        }
        
        subRec(arr, arr.length, new Node(0, 0), answer);
        
        return answer;
    }
    
    void subRec(int[][] arr, int n, Node node, int[] answer){
        int rst = 0;
        int x = node.x;
        int y = node.y;
        int[] dx = {0, 1, 0, 1};
        int[] dy = {0, 0, 1, 1};
        boolean flag = true;
        int initColor = arr[y][x];
        
        if (n == 1)
            return;
        
        // 압축 여부 판단
        for (int i = y; i < y + n; i++){
            for (int j = x; j < x + n; j++){
                if (arr[i][j] != initColor)
                    flag = false;
            }
        }
        
        if (flag == true){ // 압축 성공
            answer[initColor] -= (n * n) - 1;
        } else {
            for (int i = 0; i < 4; i++){
                int nx = x + (dx[i] * n / 2);
                int ny = y + (dy[i] * n / 2);
                subRec(arr, n / 2, new Node(nx, ny), answer);
            }
        }
    }
}

class Node {
    int x;
    int y;
    
    Node(int _x, int _y){
        this.x = _x;
        this.y = _y;
    }
}