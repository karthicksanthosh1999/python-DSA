class Stack {
    constructor() {
        this.item = {}
        this.top = -1
    }

    push(val) {
        this.top++
        this.item[this.top] = val
    }
    isEmpty() {
        return this.top === -1
    }
    pop() {
        if (this.isEmpty()) return "Stack is empty"
        let popped = this.item[this.top]
        delete this.item[this.top]
        this.top--
        return popped
    }
    peak() {
        if (this.isEmpty()) return "Stack is empty";
        return this.item[this.top]
    }
    size() {
        return this.top + 1
    }
}

const stackObj = new Stack()

stackObj.push(10)
stackObj.push(20)
stackObj.push(30)
stackObj.push(40)
stackObj.push(50)
console.log(stackObj.pop())
console.log(stackObj.peak())
console.log(stackObj.size())