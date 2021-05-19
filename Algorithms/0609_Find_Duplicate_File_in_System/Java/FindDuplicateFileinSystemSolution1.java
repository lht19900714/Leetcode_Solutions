
// Space: O(n)
// Time: O(n)

import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> cache = new HashMap<>();
        List<List<String>> res = new ArrayList<>();
        Pattern p = Pattern.compile("^(.+)\\((.+)\\)$");
        for (String s : paths) {
            String[] temp = s.split(" ");
            StringBuilder root = new StringBuilder(temp[0]);
            for (int i = 1; i < temp.length; i++) {
                Matcher m = p.matcher(temp[i]);
                m.find();
                StringBuilder fileName = new StringBuilder(m.group(1));
                StringBuilder fileContent = new StringBuilder(m.group(2));
                StringBuilder key = new StringBuilder();
                key.append(root).append("/").append(fileName);
                if (!cache.containsKey(fileContent.toString())) cache.put(fileContent.toString(), new ArrayList<>());
                cache.get(fileContent.toString()).add(key.toString());
            }
        }
        for (Map.Entry<String, List<String>> entry : cache.entrySet()) {
            if (entry.getValue().size() > 1) res.add(entry.getValue());
        }
        return res;
    }
}





