class Solution
{
    public int solution(int n, int a, int b)
    {
        int answer = 0;
        a--;
        b--;

        for (int i = 1; i <= 20; i++){
            if ((int)(a / Math.pow(2, i)) == (int)(b / Math.pow(2, i))){
                answer = i;
                break;
            }
        }

        return answer;
    }
}