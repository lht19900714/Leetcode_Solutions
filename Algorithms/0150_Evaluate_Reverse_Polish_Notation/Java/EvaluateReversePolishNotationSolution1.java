
// Space: O(n)
// Time: O(n)

class Solution {
    public int evalRPN(String[] tokens) {
        if (tokens.length == 1) return Integer.parseInt(tokens[0]);
        Stack<String> stack = new Stack<>();
        HashSet<String> operators = Stream.of("+", "-", "*", "/").collect(Collectors.toCollection(HashSet::new));
        for (String token : tokens) {
            if (operators.contains(token)) {
                String right = stack.pop();
                String left = stack.pop();
                stack.add(calc(left, right, token));
            } else {
                stack.add(token);
            }
        }
        return Integer.parseInt(stack.peek());
    }

    private String calc(String left, String right, String operator) {
        int leftNum = Integer.parseInt(left);
        int rightNum = Integer.parseInt(right);
        if (operator.equals("+")) return Integer.toString(leftNum + rightNum);
        if (operator.equals("-")) return Integer.toString(leftNum - rightNum);
        if (operator.equals("*")) return Integer.toString(leftNum * rightNum);
        if (operator.equals("/")) return Integer.toString(leftNum / rightNum);
        return "";
    }
}





