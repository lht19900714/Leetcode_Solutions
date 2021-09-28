
// Space: O(n)
// Time: O(n)

class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> res = new HashSet<>();
        for (String email : emails) {
            res.add(cleanEmail(email));
        }
        return res.size();
    }

    private String cleanEmail(String email) {
        StringBuilder res = new StringBuilder();
        int index = email.indexOf('@');
        for (char c : email.toCharArray()) {
            if (c == '@' || c == '+') break;
            else if (c != '.') res.append(c);
        }
        res.append(email.substring(index));
        return res.toString();
    }
}




