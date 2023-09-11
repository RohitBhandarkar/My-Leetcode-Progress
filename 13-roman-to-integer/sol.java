import java.util.*;

class Solution {

    static HashMap<Character, Integer> map = new HashMap<>();

    Solution() {
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);
    }

    static int val(char c) {
        if (map.containsKey(c)) {
            return map.get(c);
        }
        return -1;
    }

    public int romanToInt(String s) {
        int num = 0, temp;
        char c, tempc;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            temp = val(c);
            try {
                tempc = s.charAt(i + 1);
                if (val(tempc) > temp) {
                    temp = -temp;
                }
            } catch (Exception e) {
            } finally {
                num += temp;
            }

        }
        return num;
    }
}