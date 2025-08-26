document.addEventListener('DOMContentLoaded', () => {
    const productGrid = document.getElementById('product-grid');

    if (productGrid && typeof Isotope !== 'undefined') {

        const iso = new Isotope(productGrid, {
            itemSelector: '.isotope-item',
            layoutMode: 'fitRows'
        });

        fetch('/api/v1/products')
            .then(response => response.json())
            .then(products => {
                const placeholderItem = productGrid.querySelector('.isotope-item');
                if (placeholderItem) {
                    iso.remove(placeholderItem);
                    productGrid.removeChild(placeholderItem);
                }

                const newItems = document.createDocumentFragment();

                products.forEach(product => {
                    const productCard = document.createElement('div');
                    productCard.className = `col-sm-6 col-md-4 col-lg-3 p-b-35 isotope-item women`;
                    productCard.innerHTML = `
                        <div class="block2">
                            <div class="block2-pic hov-img0">
                                <img src="${product.image}" alt="${product.name}">
                                <a href="#" class="block2-btn ...">Quick View</a>
                            </div>
                            <div class="block2-txt ...">
                                <a href="product-detail.html" class="...">
                                    ${product.name}
                                </a>
                                <span class="stext-105 cl3">
                                    $${product.price.toFixed(2)}
                                </span>
                            </div>
                        </div>
                    `;
                    newItems.appendChild(productCard);
                });

                productGrid.appendChild(newItems);
                iso.appended(productGrid.querySelectorAll('.isotope-item'));

                // --- THIS IS THE MAGIC PART THAT FIXES THE OVERLAP ---
                // We are now using the imagesLoaded library.
                // It will wait until all images inside the productGrid are fully downloaded.
                // ONLY THEN will it run the code inside the 'progress' function.
                imagesLoaded(productGrid, function() {
                    console.log('All images loaded, now arranging layout!');
                    // Now that the images have their real size, we tell Isotope to calculate the final layout.
                    iso.layout();
                });
            })
            .catch(error => console.error('Error fetching products:', error));
    } else {
        console.error('Isotope library or product grid is missing.');
    }
});