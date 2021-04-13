
// Space: O(n)
// Time: O(n)

class MyQueue {
    private Stack<Integer> stack = new Stack<>();
    private int front;
    /** Initialize your data structure here. */
    public MyQueue() {}

    /** Push element x to the back of queue. */
    public void push(int x) {
        if (stack.size() == 0) this.front = x;
        stack.add(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        Stack<Integer> tempStack = new Stack<>();
        int res;
        if (stack.size() == 1) {
            res = stack.pop();
            return res;
        }

        while (stack.size() > 2) {
            tempStack.add(stack.pop());
        }
        this.front = stack.pop();
        tempStack.add(this.front);
        res = stack.pop();

        while (tempStack.size() > 0) {
            stack.add(tempStack.pop());
        }

        return res;
    }

    /** Get the front element. */
    public int peek() {
        return this.front;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack.size() == 0;
    }
}




