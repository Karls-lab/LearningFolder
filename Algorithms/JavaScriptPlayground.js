// Welcome to my JavaScript Playground! :)

// always use const or let for varialbes ;)

Rectangle = class Rectangle2 {
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  getHello() {
    console.log("Hello World! :)")
  }
  getHeight() {
      return this.height;
  }
  calculatePerimeter() {
      return (this.height * 2) + (this.width * 2);
  }

};

let square = new Rectangle(10, 10);
square.getHello();
console.log(square.getHeight());
console.log(square.calculatePerimeter());


(function(){
  "use strict";
  /* Start of your code */
  const PLAYArray = [0, 6, 1, 4, 2, 9, 5, 3]


  function greetMe(yourName) {
    console.log(`Hello ${yourName}`);
  }
  greetMe('World');

  function getFee(isMember) {
    return (isMember ? '2.00' : '10.00'); // if member, return 10, else return 2
  }
  console.log(getFee(true));


  let unusualPropertyNames = {
    '': 'This is a JavaScript Object, but kinda like a Dictionary!',
    '!': 'Bang!'
  }
  console.log(unusualPropertyNames['']);  // An empty string
  console.log(unusualPropertyNames['!']); // Bang!


  function map(f, a) {
    const result = [];
    for (let i = 0; i < a.length; i++) {
      result[i] = f(a[i]);
    }
    return result;
  }
  function addTwo(x) { return x += 2; }
  let result = map(addTwo, PLAYArray);
  let output = "";
  for(let i = 0; i < result.length; i++) {
    output += result[i].toString() + " "
  }
  console.log(output);


  var rank= [7,8,9];
  var display = rank.map((num) => num*num);
  console.log(display);

  

  /* End of your code */
})();





