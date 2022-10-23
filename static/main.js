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
    // console.log(data);
    displayStudentData(data);
  })
  .catch((error) => console.error("FETCH ERROR:", error));

function capitalize(string) {
  return string.charAt(0).toUpperCase() + string.slice(1);
}

function displayStudentData(data) {
  const username = data[0].user.username;
  const email = data[0].user.email;
  const first_name = data[0].user.first_name;
  const last_name = data[0].user.last_name;

  // getelementsbyclassname and set innerhtml to username
  document.getElementsByClassName("username")[0].innerHTML =
    capitalize(username);
  document.getElementsByClassName("username")[1].innerHTML =
    capitalize(username);

  if (email) {
    document.getElementById("email").innerHTML = email;
  }
  // concat first_name and last_name
  document.getElementById("fullname").innerHTML =
    capitalize(first_name) + " " + capitalize(last_name);

  document.getElementById("classname").innerHTML = data[0].class_name;
  document.getElementById("fathername").innerHTML = capitalize(
    data[0].father_name
  );
  document.getElementById("mothername").innerHTML = capitalize(
    data[0].mother_name
  );
  document.getElementById("phone").innerHTML = data[0].phone;
  document.getElementById("address").innerHTML = data[0].address;
  document.getElementById("regno").innerHTML = data[0].registration_number;

  var avg_marks = 0,
    total_marks = 0;

  let tab = `<tr>
      <th>Subject Name</th>
      <th>Obtained Marks</th>
      <th>Total Marks</th>
    </tr>`;

  // Loop to access all rows
  for (let r of data[0].submarks) {
    // console.log(r);
    avg_marks += r.obtained_marks;
    total_marks += r.total_marks;
    tab += `<tr> 
      <td>${capitalize(r.subject.subject_name)} </td>
      <td>${r.obtained_marks}</td>
      <td>${r.total_marks}</td> 
    </tr>`;
  }
  // console.log(data[0].submarks.length);
  // Setting innerHTML as avg_marks and total_marks variable
  document.getElementById("avg_marks").innerHTML = avg_marks;
  document.getElementById("total_marks").innerHTML = total_marks;
  document.getElementById("percentage").innerHTML =
    (avg_marks / total_marks) * 100;

  document.getElementById("studentmarks").innerHTML = tab;
}

fetch("http://127.0.0.1:8000/api-student-marks/?format=json")
  .then((response) => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error("NETWORK RESPONSE ERROR");
    }
  })
  .then((data) => {
    // console.log(data);
    displaySubjectMarks(data);
  })
  .catch((error) => console.error("FETCH ERROR:", error));

function displaySubjectMarks(data) {
  // console.log(data);

  var uniq = {}; // contains all the unique names

  for (var i = 0; i < data.length; i++) {
    var el = data[i].student.user.username;
    if (!uniq[el]) uniq[el] = []; // start the array
    var result = {}; // contains the final result

    result["subject"] = data[i].subject.subject_name
    result["marks"] = data[i].obtained_marks;

    uniq[el].push(result);
  }

  // console.log(uniq);

  var highest_marks = `<tr>
      <th>Student Name</th>
      <th>Highest Marks</th>
      <th>Subject Name</th>
    </tr>`;
  var max1 = -1;
  var user = "";
  Object.entries(uniq).forEach(([key, value]) => {
    
    var max = 0;
    var subject = "";
    var top = 0;
    
    for (var i = 0; i < value.length; i++) {
      top += value[i].marks;
      if (value[i].marks > max) {
        max = value[i].marks;
        subject = value[i].subject;
      }
    }

    if(max1 < top)
    {
      max1 = top;
      user = key;
    }

    highest_marks += `<tr> 
      <td>${capitalize(key)}</td>
      <td>${max}</td>
      <td>${capitalize(subject)}</td>
    </tr>`;
  });

  document.getElementsByClassName('topper')[0].innerHTML = capitalize(user) + " achieved top rank" + " with score of " + max1 + ".";

  document.getElementById("highestmarks").innerHTML = highest_marks;
}
