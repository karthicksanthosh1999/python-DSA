// PALINDROME
function palindrome(str) {
    let j = str.length - 1;

    for (let i = 0; i < str.length / 2; i++) {
        if (str[i] != str[j]) {
            return false
        }
        j--
    }
    return true
}

console.log(palindrome("joseph"))

// FACTORIAL
function factorial(val) {
    let res = 1;
    for (let i = 1; i <= val; i++) {
        res *= i
    }
    return res
}
console.log("Normal Factorial " + factorial(10))


function recrusionFactorial(val) {
    if (val === 0 || val === 1) return 1;
    return val * recrusionFactorial(val - 1)
}
console.log("Recurtion Factorial " + recrusionFactorial(10))
