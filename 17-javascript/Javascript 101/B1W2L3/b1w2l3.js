// begin hier je JavaScript commandos
// 1. Maak een JavaScript applicatie die de tafel van 3 en 6 uitrekent.

/* program to generate a multiplication table
upto a range */

// Take number input from the user
const number = parseInt(prompt('Enter an integer: '));

// Take range input from the user
const range = parseInt(prompt('Enter a range: '));

// Creating a multiplication table
for(let i = 1; i <= range; i++) {
    const result = i * number;
    console.log(`${number} * ${i} = ${result}`);
    document.write(`${i} * ${number} = ${result} <br />`)
}