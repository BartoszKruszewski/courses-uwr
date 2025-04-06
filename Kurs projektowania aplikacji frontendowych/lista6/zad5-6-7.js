let library = [];

const addBookToLibrary = (title, author, pages, isAvailable, ratings) => {
    if (typeof title !== "string" || title.trim() === "") {
        throw new Error("Title must be a non-empty string");
    }
    if (typeof author !== "string" || author.trim() === "") {
        throw new Error("Author must be a non-empty string");
    }
    if (typeof pages !== "number" || pages <= 0) {
        throw new Error("Pages must be a positive number");
    }
    if (typeof isAvailable !== "boolean") {
        throw new Error("isAvailable must be a boolean");
    }
    if (!Array.isArray(ratings)) {
        throw new Error("Ratings must be an array");
    }
    for (let r of ratings) {
        if (typeof r !== "number" || r < 0 || r > 5) {
            throw new Error("Each rating must be a number between 0 and 5");
        }
    }

    library.push({
        title,
        author,
        pages,
        available: isAvailable,
        ratings,
    });
};

function testAddingBooks(testCases) {
    for (let { testCase, shouldFail } of testCases) {
        try {
            addBookToLibrary(...testCase);
            if (shouldFail) {
                console.log("Test failed:", testCase);
            } else {
                console.log("Test passed:", testCase);
            }
        } catch (e) {
            if (shouldFail) {
                console.log("Test passed:", testCase, "-", e.message);
            } else {
                console.log("Test failed:", testCase, "-", e.message);
            }
        }
    }
}

const testCases = [
    { testCase: ["", "Author", 200, true, []], shouldFail: true },
    { testCase: ["Title", "", 200, true, []], shouldFail: true },
    { testCase: ["Title", "Author", -1, true, []], shouldFail: true },
    { testCase: ["Title", "Author", 200, "yes", []], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 6]], shouldFail: true },
    {
        testCase: ["Title", "Author", 200, true, [1, 2, 3, "yes"]],
        shouldFail: true,
    },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, {}]], shouldFail: true },
    { testCase: ["Title", "Author", 200, true, []], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3]], shouldFail: false },
    { testCase: ["Title", "Author", 200, true, [1, 2, 3, 4]], shouldFail: false },
    {
        testCase: ["Title", "Author", 200, true, [1, 2, 3, 4, 5]],
        shouldFail: false,
    },
];

testAddingBooks(testCases);

library = [];

function addBooksToLibrary(books) {
    for (let args of books) {
        addBookToLibrary(...args);
    }
}

const books = [
    ["Alice in Wonderland", "Lewis Carroll", 200, true, [1, 2, 3]],
    ["1984", "George Orwell", 300, true, [4, 5]],
    ["The Great Gatsby", "F. Scott Fitzgerald", 150, true, [3, 4]],
    ["To Kill a Mockingbird", "Harper Lee", 250, true, [2, 3]],
    ["The Catcher in the Rye", "J.D. Salinger", 200, true, [1, 2]],
    ["The Hobbit", "J.R.R. Tolkien", 300, true, [4, 5]],
    ["Fahrenheit 451", "Ray Bradbury", 200, true, [3, 4]],
    ["Brave New World", "Aldous Huxley", 250, true, [2, 3]],
    ["The Alchemist", "Paulo Coelho", 200, true, [1, 2]],
    ["The Picture of Dorian Gray", "Oscar Wilde", 300, true, [4, 5]],
];

addBooksToLibrary(books);
console.log(library);
