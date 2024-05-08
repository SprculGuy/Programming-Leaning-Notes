// const a = {1:"One", 2:"Two"}
// console.log(a)
// // delete a.1
// // console.log(a)
// var b = {1:"One", 2:"Two"}
// console.log(b)
// // delete b.1
// // console.log(b)
// let c = {1:"One", 2:"Two"}
// console.log(c);
// // delete c.1;
// // console.log(b)

const person = {
    name: ["Bob", "Smith"],
    age: 32,
    bio: function () {
      console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
    },
    introduceSelf: function () {
      console.log(`Hi! I'm ${this.name[0]}.`);
    },
  };

console.log(person.name)
person.name[2] = 'Ankit'
console.log(person.name)
console.log(person.name[2])
console.log(person.age)
console.log(person.bio())
console.log(person.introduceSelf())

console.log(person)
delete person.name
console.log(person)
