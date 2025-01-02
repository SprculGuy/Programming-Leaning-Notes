const groups = Object.groupBy([{name: "ankit", type: "saving"}, {name: "Nikita", type: "saving"}, {name: "Bharti", type: "current"}], function(current, i) {
	return current.type;
});
console.log(groups);
