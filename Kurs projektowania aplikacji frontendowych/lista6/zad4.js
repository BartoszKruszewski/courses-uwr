function compareObjects(obj1, obj2) {
    const keys1 = Object.keys(obj1);
    const keys2 = Object.keys(obj2);

    if (keys1.length !== keys2.length) return false;

    for (let key of keys1) {
        const val1 = obj1[key];
        const val2 = obj2[key];

        const areObjects =
            typeof val1 === "object" &&
            val1 !== null &&
            typeof val2 === "object" &&
            val2 !== null;

        if (areObjects) {
            if (!compareObjects(val1, val2)) return false;
        } else {
            if (val1 !== val2) return false;
        }
    }

    return true;
}

const obj1 = {
    name: "Alice",
    age: 25,
    address: {
        city: "Wonderland",
        country: "Fantasy",
    },
};

const obj2 = {
    name: "Alice",
    age: 25,
    address: {
        city: "Wonderland",
        country: "Fantasy",
    },
};

const obj3 = {
    age: 25,
    address: {
        city: "Wonderland",
        country: "Fantasy",
    },
    name: "Alice",
};

const obj4 = {
    name: "Alice",
    age: 25,
    address: {
        city: "Not Wonderland",
        country: "Fantasy",
    },
};

const obj5 = {
    name: "Alice",
};

console.log("Should be True:", compareObjects(obj1, obj2));
console.log("Should be True:", compareObjects(obj1, obj3));
console.log("Should be False:", compareObjects(obj1, obj4));
console.log("Should be True:", compareObjects(obj2, obj3));
console.log("Should be False:", compareObjects(obj2, obj4));
console.log("Should be False:", compareObjects(obj3, obj4));
console.log("Should be False:", compareObjects(obj1, obj5));
console.log("Should be False:", compareObjects(obj5, obj1));
