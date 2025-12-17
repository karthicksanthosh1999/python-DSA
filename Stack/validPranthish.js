class Stack {
    constructor() {
        this.item = {}
        this.top = -1
    }
    isEmpty() {
        return this.top === -1
    }
    push(val) {
        this.top++
        this.item[this.top] = val
    }
    pop() {
        let popped = this.item[this.top]
        delete this.item[this.top]
        this.top--
        return popped
    }
    peak() {
        return this.item[this.top]
    }
    size() {
        return this.top + 1
    }
}

function validParanthish(str) {
    const stackObj = new Stack()
    const pairs = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    for (let char of str) {
        if (char === "[" || char === "{" || char === "(") {
            stackObj.push(char)
        } else if (char === "]" || char === "}" || char === ")") {
            if (char === pairs[char]) {

            }
        }
    }
}