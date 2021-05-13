
// Space: O(1)
// Time: O(n)

import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public List<String> ambiguousCoordinates(String s) {
        String data = s.substring(1, s.length() - 1);
        List<String> res = new ArrayList<>();
        for (int i = 1; i < data.length(); i++) {
            List<String> leftRes = generateNumber(data.substring(0, i));
            List<String> rightRes = generateNumber(data.substring(i, data.length()));
            if (leftRes.size() == 0 || rightRes.size() == 0) continue;
            for (String left : leftRes) {
                for (String right : rightRes) {
                    String temp = "(" + left + ", " + right + ")";
                    res.add(temp);
                }
            }
        }
        return res;
    }

    public List<String> generateNumber(String s) {
        if (s.length() == 1) return new ArrayList<>(Collections.singletonList(s));
        List<String> res = new ArrayList<>();
        Pattern pattern = Pattern.compile("(^[1-9]+[0-9]*\\.[0-9]*[1-9]$)|(^0\\.[0-9]*[1-9]$)");

        int j = 0;
        while (j < s.length() && s.charAt(j) == '0') {
            j++;
        }
        String ltrim = s.substring(j);
        if (ltrim == s) res.add(s);

        for (int i = 1; i < s.length(); i++) {
            String temp = s.substring(0, i) + "." + s.substring(i, s.length());
            Matcher matcher = pattern.matcher(temp);
            if (matcher.find()) res.add(temp);
        }
        return res;
    }
}




