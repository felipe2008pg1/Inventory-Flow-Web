let stock = JSON.parse(localStorage.getItem('stock')) || [];

function updateScreen() {
    const tableBody = document.getElementById('table-body');
    const emptyMessage = document.getElementById('empty-message');
    tableBody.innerHTML = '';

    if (stock.length === 0) {
        emptyMessage.classList.remove('hidden');
    } else {
        emptyMessage.classList.add('hidden');
        stock.forEach((item, index) => {
            tableBody.innerHTML += `
                <tr>
                    <td>${index + 1}</td>
                    <td>${item.product}</td>
                    <td>R$ ${parseFloat(item.price).toFixed(2)}</td>
                    <td><button class="btn-remove" onclick="removeProduct(${index})">Remove</button></td>
                </tr>
            `;
        });
    }
    localStorage.setItem('stock', JSON.stringify(stock));
}

function addProduct() {
    const name = document.getElementById('product-name').value.toUpperCase();
    const price = document.getElementById('product-price').value;

    if (name && price) {
        stock.push({ product: name, price: price });
        document.getElementById('product-name').value = '';
        document.getElementById('product-price').value = '';
        updateScreen();
    } else {
        alert("Fill in all fields!");
    }
}

function removeProduct(index) {
    if (confirm(`Remove ${stock[index].product}?`)) {
        stock.splice(index, 1);
        updateScreen();
    }
}

function updateTime() {
    const now = new Date();
    document.getElementById('date-time').innerText = `🕐 | Date: ${now.toLocaleString('en-US')}`;
}

setInterval(updateTime, 1000);
updateScreen();
