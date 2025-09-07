// 1️⃣ آدرس API
const API_URL = "http://127.0.0.1:8000/api/tafzili/";

// 2️⃣ گرفتن عناصر فرم و جدول
const form = document.getElementById("tafziliForm");
const tableBody = document.querySelector("#tafziliTable tbody");

// 3️⃣ دریافت و نمایش داده‌ها
async function fetchTafzili() {
  const res = await fetch(API_URL);
  const data = await res.json();
  renderTable(data);
}

// 4️⃣ ارسال رکورد جدید
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const payload = {
    tafzily_code: document.getElementById("TafzilyCode").value,
    moen_code: document.getElementById("MoenCode").value,
    all_code: document.getElementById("AllCode").value,
    fname: document.getElementById("Fname").value,
    lastname: document.getElementById("Lastname").value,
    city: document.getElementById("City").value,
    tel: document.getElementById("Tel").value,
    bad: parseFloat(document.getElementById("Bad").value) || 0,
    change: parseFloat(document.getElementById("Change").value) || 0,
    mandeh: parseFloat(document.getElementById("Mandeh").value) || 0,
    atbar: parseFloat(document.getElementById("Atbar").value) || 0,
    moen_name: document.getElementById("MoenName").value,
    daftar: document.getElementById("Daftar").value,
    moarref: document.getElementById("Moarref").value,
    sms: document.getElementById("SMS").value,
    ashxas: document.getElementById("Ashxas").value,
    atabarok: document.getElementById("Atabarok").value,
    ozv: document.getElementById("Ozv").checked,
    tafzily_sharh: document.getElementById("TafzilySharh").value,
  };

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  form.reset();
  fetchTafzili();
});

// 5️⃣ نمایش جدول
function renderTable(data) {
  tableBody.innerHTML = "";
  data.forEach(item => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${item.tafzily_code}</td>
      <td>${item.fname || ""} ${item.lastname || ""}</td>
      <td>${item.city || ""}</td>
      <td>${item.tel || ""}</td>
      <td>${item.bad || 0}</td>
      <td>${item.atbar || 0}</td>
      <td>${item.mandeh || 0}</td>
    `;
    tableBody.appendChild(tr);
  });
}

// 6️⃣ لود اولیه داده‌ها
fetchTafzili();
