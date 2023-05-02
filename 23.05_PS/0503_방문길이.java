import java.util.*;

class Solution {
    HashMap<String, Boolean> load = new HashMap<>();
    public int solution(String dirs) {
        String[] dirsArr = dirs.split("");
        Place now = new Place(0, 0);
        for (int i = 0; i < dirsArr.length; i++){
            now = move(now, dirsArr[i]);
        }
        
        return load.size() / 2;
    }
    
    Place move(Place now, String d){
        int nx = now.x; 
        int ny = now.y;
        
        if (d.equals("U"))
            ny++;
        else if (d.equals("D"))
            ny--;
        else if (d.equals("L"))
            nx--;
        else
            nx++;
        
        Place newNow = new Place(nx, ny);

        if (nx >= -5 && nx <= 5 && ny >= -5 && ny <= 5){
            String pA = Integer.toString(now.x) + Integer.toString(now.y) + Integer.toString(newNow.x) + Integer.toString(newNow.y);
            String pB = Integer.toString(newNow.x) + Integer.toString(newNow.y) + Integer.toString(now.x) + Integer.toString(now.y);
            
            if (!load.containsKey(pA) && !load.containsKey(pB)){
                load.put(pA, true);
                load.put(pB, true);
            }
            return newNow;
        }
        else
            return now;
        
    }
}

class Place {
    int x;
    int y;
    
    Place (int x, int y){
        this.x = x;
        this.y = y;
    }
}