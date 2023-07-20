const form = document.querySelector(".feedback__form");

form.addEventListener("submit", function (event) {
  event.preventDefault();

  const formData = new FormData(event.target); // получаем данные формы

  // создаем объект с данными формы
  const obj = {};
  formData.forEach((value, key) => {
    obj[key] = value;
  });

  // преобразуем объект в JSON
  const json = JSON.stringify(obj);

  // отправляем запрос
  fetch("http://127.0.0.1:5000/api/forma/", {
    method: "POST",
    body: json,
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => {
      if (response.ok) {
        return response.text(); // возвращаем текст ответа
      }
      throw new Error("Network response was not ok");
    })
    .then((text) => {
      console.log(text); // выводим текст ответа в консоль
      // console.log("123");
    })
    .catch((error) => {
      console.error("There was a fetch problem:", error);
    });
});
