const input = document.querySelector("#input");
const city = document.querySelector("#city");

const cityName = document.querySelector("#cityName");
const Temp = document.querySelector("#temp");
const main = document.querySelector("#main");
const discription = document.querySelector("#discription");
const image = document.querySelector("#image");

input.onsubmit = (e) => {
  e.preventDefault();
  weatherUpdate(city.value);
  city.value = "";
};

weatherUpdate = (city) => {
  const xhr = new XMLHttpRequest();
  xhr.open(
    "GET",
    `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=f8859b2c913efb878328a752c7ab3dd9`);
  // in place of appid enter your open weather API Key
  // You can create it for free
  // https://home.openweathermap.org/users/sign_up

  xhr.send();
  xhr.onload = () => {
    if (xhr.status === 404) {
      alert("Place not found");
    } else {
      var data = JSON.parse(xhr.response);
      cityName.innerHTML = data.name;
      Temp.innerHTML = `${Math.round(((data.main.temp - 273.15) * 1.8) + 32)}°F`;
      main.innerHTML = data.weather[0].main;
      discription.innerHTML = data.weather[0].description;
      image.src = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;
    }
  };
};

weatherUpdate("logan");
