//Before axios used must install=>  python -m pip install django-cors-headers

// Get Request

axios.get("http://127.0.0.1:8000/apiV1/status/")
  .then(response => console.log(response.data))
  .catch(error=> console.log("Error fetching data:", error.message))

  
// Post Request

// let postData = {
//   user: 8,
//   content: 'This i test data',
//   image: null
// }


// axios.post("http://127.0.0.1:8000/apiV1/status/create/", postData, {
//   headers: {
//     "Content-Type": "application/json"
//   }
// })
//   .then(response => console.log(response.data))
//   .catch(error => console.log("Error fetching data:", error.message))
  
// Than Other option call here