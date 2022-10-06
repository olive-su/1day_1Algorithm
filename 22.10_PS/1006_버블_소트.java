// boj. 1377
// 버블 정렬

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int v = 0; // 인덱스 차이 최댓값
        mData[] arr = new mData[n];

        for (int i = 0; i < n; i++) {
            arr[i] = new mData(Integer.parseInt(br.readLine()), i);
        }

        Arrays.sort(arr);

        for (int i = 0; i < n; i++) {
            int target = arr[i].index;
            if (v < target - i)
                v = target - i;
        }
        
        System.out.println(v + 1);
    }
}

// value와 index를 저장하기 위한 새로운 자료형 생성
// hashMap이 안되는 이유 -> key(value)가 동일한 값이 있을 경우 value(index)값을 중복해서 찾아온다.
class mData implements Comparable<mData> {
    int value;
    int index;

    public mData(int value, int index) {
        super();
        this.value = value;
        this.index = index;
    }

    @Override
    public int compareTo(mData o) {
        return this.value - o.value;
    }
}