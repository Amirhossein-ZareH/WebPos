document.addEventListener("DOMContentLoaded", function() {
    const tableBody = document.querySelector("#productTable tbody");
    const nextButton = document.getElementById("nextPage");
    const prevButton = document.getElementById("prevPage");

    let products = []; // داده‌ها از API
    let currentPage = 1;
    const pageSize = 50;

    function renderPage() {
        const start = (currentPage - 1) * pageSize;
        const end = start + pageSize;
        const pageData = products.slice(start, end);

        tableBody.innerHTML = "";
        pageData.forEach(p => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${p.Code}</td>
                <td>${p.Name}</td>
                <td>${p.MoenCode}</td>
                <td>${p.MoenName}</td>
                <td>${p.Price}</td>
                <td>${p.Mojode}</td>
            `;
            tableBody.appendChild(row);
        });
    }

    nextButton.addEventListener("click", () => {
        if (currentPage * pageSize < products.length) {
            currentPage++;
            renderPage();
        }
    });

    prevButton.addEventListener("click", () => {
        if (currentPage > 1) {
            currentPage--;
            renderPage();
        }
    });

    // گرفتن داده‌ها از API
    fetch('/api/kala/')
        .then(res => res.json())
        .then(data => {
            products = data;
            renderPage();
        })
        .catch(err => console.error("خطا در دریافت کالاها:", err));
});
