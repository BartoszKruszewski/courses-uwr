// zamiana z funkcji strzalkowej na zwykla

console.log(capitalize("alice"));

function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
};
