const now = new Date(new Date("2024-01-01T00:00:00.000Z").getTime() + 5.5*60*60*1000)
const now1 = new Date("2024-01-01T00:00:00.000Z")
const now2 = new Date().toISOString()
console.log(now);
console.log(now1);
console.log(now2);