// This code runs when the webpage's content is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    // For now, we will just request a fake product with id '123'
    const productId = '123';

    // Use the browser's fetch API to call our backend endpoint
    fetch(`/api/v1/products/${productId}`)
        .then(response => response.json()) // When the server responds, parse the JSON data
        .then(product => {
            // Now we have the product data, let's update the HTML
            document.getElementById('product-name').textContent = product.name;
            document.getElementById('product-price').textContent = `$${product.price}`;
            // Future task: You could also update the description and images here.
        })
        .catch(error => console.error('Error fetching product details:', error)); // Handle any errors
});