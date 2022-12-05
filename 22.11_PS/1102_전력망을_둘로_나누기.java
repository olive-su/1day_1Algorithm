import java.util.*;

class Solution {
    ArrayList[] nodeConnections;
    boolean[] nodeVisted;
    
    public int solution(int n, int[][] wires) {
        int answer = -1;

        nodeConnections = new ArrayList[n + 1]; // 노드간 연결상태 담음
        nodeVisted = new boolean[n + 1]; // 방문 상태 배열

        for (int i = 1; i < n + 1; i++) {
            nodeConnections[i] = new ArrayList<>();
        }

        for (int i = 0; i < wires.length; i++) {
            int a = wires[i][0];
            int b = wires[i][1];
            nodeConnections[a].add(b);
            nodeConnections[b].add(a);
        }

        for (int i = 0; i < wires.length; i++) {
            Integer a = wires[i][0];
            Integer b = wires[i][1];
            nodeConnections[b].remove(a); // 연결된 줄을 끊었을 경우
            nodeConnections[a].remove(b);

            nodeVisted = new boolean[n + 1];
            int cntA = dfs(a, 1); // 연결 상태에서의 노드 개수를 구하기 위해 dfs 수행
            nodeVisted = new boolean[n + 1];
            int cntB = dfs(b, 1);

            if (answer == -1 || answer > Math.abs(cntA - cntB)) {
                answer = Math.abs(cntA - cntB);
            }
            nodeConnections[b].add(a); // 반복문의 다음 루프를 위해 다시 원소 추가
            nodeConnections[a].add(b);
        }

        return answer;
    }

    int dfs(int start, int cnt) {
        nodeVisted[start] = true;
        for (int i = 0; i < nodeConnections[start].size(); i++) {
            Integer target = (Integer) nodeConnections[start].get(i);
            if (!nodeVisted[target]) { // 노드 미방문시, dfs 및 노드 개수에 +1
                cnt = dfs(target, cnt + 1);
            }
        }
        return cnt;
    }

}