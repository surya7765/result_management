// fetch api using Jquery http://127.0.0.1:8000/api-student/?format=json
// fetch api using Jquery http://

fetch("http://127.0.0.1:8000/api-student/?format=json")
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("NETWORK RESPONSE ERROR");
    }
  })
  .then((data) => {
    console.log(data);
    displayCocktail(data);
  })
  .catch((error) => console.error("FETCH ERROR:", error));

function displayCocktail(data) {


  const username = data[0].user.username;
  const email = data[0].email;
  const first_name = data[0].user.first_name;
  const last_name = data[0].user.last_name;

  // getelementsbyclassname and set innerhtml to username
  document.getElementsByClassName("username")[0].innerHTML = username;
  document.getElementsByClassName("username")[1].innerHTML = username;

  if (email) {
    document.getElementById("email").innerHTML = email;
  }
  // concat first_name and last_name
  document.getElementById("fullname").innerHTML = first_name + " " + last_name;

  document.getElementById('classname').innerHTML = data[0].class_name;
  document.getElementById("fathername").innerHTML = data[0].father_name;
  document.getElementById('mothername').innerHTML = data[0].mother_name;
  document.getElementById("phone").innerHTML = data[0].phone;
  document.getElementById("address").innerHTML = data[0].address;


}   