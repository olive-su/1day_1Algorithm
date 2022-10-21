// boj. 1931

import java.io.*;
import java.util.*;

// 제일 적게 걸리고 빨리 끝나는 회의
class Time {
    public int start;
    public int end;

    Time(int start, int end) {
        this.start = start;
        this.end = end;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        int start = 0;
        int end = 0;
        int now = 0;
        int index = 0;
        int count = 0;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        ArrayList<Time> meeting = new ArrayList<>();

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            Time time = new Time(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            meeting.add(time);
        }

        // 빨리 시작하는 회의 순으로 오름차순 정렬
        Collections.sort(meeting, new Comparator<Time>() {
            @Override
            public int compare(Time o1, Time o2) {
                return o1.start - o2.start;
            }
        });

        // 빨리 끝나는 회의 순으로 오름차순 정렬
        Collections.sort(meeting, new Comparator<Time>() {
            @Override
            public int compare(Time o1, Time o2) {
                return o1.end - o2.end;
            }
        });

        while (!meeting.isEmpty()) {
            Time t = meeting.remove(0);
            if (t.start >= now) {
                count++;
                now = t.end;
            }
        }

        System.out.println(count);
    }
}