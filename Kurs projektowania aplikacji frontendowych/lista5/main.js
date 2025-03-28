/**
 * @typedef {object} Product
 * @property {number} id - Product ID
 * @property {string} name - Product name
 * @property {number} quantity - Quantity to buy
 * @property {Date} purchaseDate - Deadline date
 * @property {boolean} purchased - Purchased status
 * @property {number} [pricePerItem] - Price per item (only if purchased)
 */

/** @type {Product[]} */
let productList = [];

/**
 * @param {string} name
 * @param {number} quantity
 * @param {string} dateString
 * @returns {number} New product ID
 */
function addProduct(name, quantity, dateString) {
    const id = Math.floor(Math.random() * 1_000_000_000);
    const purchaseDate = new Date(dateString);
    productList.push({
        id,
        name,
        quantity,
        purchaseDate,
        purchased: false
    });
    return id;
}

/**
 * @param {number} id
 * @returns {boolean} True if removed
 */
function removeProduct(id) {
    const index = productList.findIndex((p) => p.id === id);
    if (index === -1) return false;
    productList.splice(index, 1);
    return true;
}

/**
 * @param {number} id
 * @param {string} newName
 * @returns {boolean} True if edited
 */
function editName(id, newName) {
    const product = productList.find((p) => p.id === id);
    if (!product) return false;
    product.name = newName;
    return true;
}

/**
 * @param {number} id
 * @param {boolean} newStatus
 * @returns {boolean} True if edited
 */
function editPurchased(id, newStatus) {
    const product = productList.find((p) => p.id === id);
    if (!product) return false;
    product.purchased = newStatus;
    if (!newStatus && product.pricePerItem !== undefined) {
        delete product.pricePerItem;
    }
    return true;
}

/**
 * @param {number} id
 * @param {number} newQuantity
 * @returns {boolean} True if edited
 */
function editQuantity(id, newQuantity) {
    const product = productList.find((p) => p.id === id);
    if (!product) return false;
    product.quantity = newQuantity;
    return true;
}

/**
 * @param {number} id
 * @param {string} newDateString
 * @returns {boolean} True if edited
 */
function editPurchaseDate(id, newDateString) {
    const product = productList.find((p) => p.id === id);
    if (!product) return false;
    product.purchaseDate = new Date(newDateString);
    return true;
}

/**
 * @param {number} id
 * @param {number} newIndex
 * @returns {boolean} True if reordered
 */
function reorderProducts(id, newIndex) {
    const oldIndex = productList.findIndex((p) => p.id === id);
    if (oldIndex === -1) return false;

    const [product] = productList.splice(oldIndex, 1);
    if (newIndex < 0) newIndex = 0;
    if (newIndex > productList.length) newIndex = productList.length;
    productList.splice(newIndex, 0, product);
    return true;
}

/**
 * @returns {Product[]} Products to buy today
 */
function getProductsToPurchaseToday() {
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    return productList.filter((product) => {
        const productDate = new Date(product.purchaseDate);
        productDate.setHours(0, 0, 0, 0);
        return (
            productDate.getTime() === today.getTime() &&
            product.purchased === false
        );
    });
}

/**
 * @param {number} id
 * @param {number} price
 * @returns {boolean} True if price set
 */
function setPrice(id, price) {
    const product = productList.find((p) => p.id === id);
    if (!product || !product.purchased) return false;
    product.pricePerItem = price;
    return true;
}

/**
 * @param {string} dateString
 * @returns {number} Total cost
 */
function calculateCostForDate(dateString) {
    const requestedDate = new Date(dateString);
    requestedDate.setHours(0, 0, 0, 0);

    return productList.reduce((acc, product) => {
        const productDate = new Date(product.purchaseDate);
        productDate.setHours(0, 0, 0, 0);
        if (
            productDate.getTime() === requestedDate.getTime() &&
            product.purchased
        ) {
            const price = product.pricePerItem || 0;
            return acc + product.quantity * price;
        }
        return acc;
    }, 0);
}

/**
 * @callback ModifyCallback
 * @param {Product} product
 * @returns {Product} Modified product
 */

/**
 * @param {number[]} ids
 * @param {ModifyCallback} modifyCallback
 */
function massModify(ids, modifyCallback) {
    productList = productList.map((p) => {
        if (ids.includes(p.id)) {
            return modifyCallback(p);
        }
        return p;
    });
}

const id1 = addProduct("Bread", 2, "2025-03-28");
const id2 = addProduct("Milk", 1, "2025-03-28");
const id3 = addProduct("Butter", 2, "2025-03-29");
console.log("Initial list:", productList);

editName(id2, "Milk 2%");
editPurchased(id2, true);
setPrice(id2, 5.5);
reorderProducts(id3, 0);
console.log("Reordered list:", productList);

console.log("Products to purchase today:", getProductsToPurchaseToday());
editQuantity(id1, 3);

massModify([id1, id2], (p) => {
    p.name = "[SALE] " + p.name;
    return p;
});
console.log("After mass modify:", productList);

console.log("Total cost on 2025-03-28:", calculateCostForDate("2025-03-28"));

removeProduct(id1);
console.log("After removing product with id1:", productList);
