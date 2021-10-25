
// Space: O(n)
// Time: O(n)

class MinStack {
    private Stack<int[]> stack;
    private int min = Integer.MAX_VALUE;

    public MinStack() {
        stack = new Stack<>();
    }

    public void push(int val) {
        min = Math.min(min, val);
        int[] temp = new int[]{val, min};
        stack.add(temp);
    }

    public void pop() {
        stack.pop();
        min = stack.isEmpty()? Integer.MAX_VALUE:getTop()[1];
    }

    public int top() {
        return getTop()[0];
    }

    public int getMin() {
        return getTop()[1];
    }

    private int[] getTop() {
        return stack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */




