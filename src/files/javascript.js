// Advanced JavaScript Example: Fetch API, Classes, and Promises

// Define a class
class Calculator {
    add(a, b) {
        return a + b;
    }

    subtract(a, b) {
        return a - b;
    }
}

// Create an instance and use it
const calc = new Calculator();
console.log("Addition: ", calc.add(10, 20));
console.log("Subtraction: ", calc.subtract(20, 10));

// Fetch data from an API
fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(response => response.json())
    .then(data => {
        console.log("Fetched Data:", data);
    })
    .catch(error => {
        console.error("Error fetching data:", error);
    });
