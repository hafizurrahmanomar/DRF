//Before axios used must install=>  python -m pip install django-cors-headers


// Get Request=>List

// axios.get('http://127.0.0.1:8000/apiV1/status/list/')
//     .then(response => {
//         console.log(response.data);
//          // Display fetched data
//     })
//     .catch(error => {
//         console.error('Error fetching data:', error);
//     });

// // Get Request=>details
// axios.get('http://127.0.0.1:8000/apiV1/status/detail/5/')
//     .then(response => {
//         console.log(response.data);
//          // Display fetched data
//     })
//     .catch(error => {
//         console.error('Error fetching data:', error);
//     });


// // POST Request

//   let myStatus = {
//         user: 3,
//         content: "This is Api practice file",
//         image: null,
//       };
    
// axios.post('http://127.0.0.1:8000/apiV1/status/create/', myStatus, {
//     headers: {
//     "Content-Type": "application/json"
// }})
//     .then(response => {
//         console.log(response.data);
//          // Display fetched data
//     })
//     .catch(error => {
//         console.error('Error fetching data:', error);
//     });


// // delete
// axios.delete('http://127.0.0.1:8000/apiV1/status/delete/4/')
//     .then(response => {
//         console.log(response.data);
//          // Display fetched data
//     })
//     .catch(error => {
//         console.error('Error fetching data:', error);
//     });


//   let update_Status = {
//         user: 4,
//         content: "Update data",
//         image: null,
// };
      
// // put
// axios.put('http://127.0.0.1:8000/apiV1/status/update/0/', update_Status,{
//     headers: {
//         "Content-Type": "application/json"
//     }
// })
//     .then(response => {
//         console.log(response.data);
//          // Display fetched data
//     })
//     .catch(error => {
//         console.error('Error fetching data:', error);
//     });

// patch
  let u_Status = { 
        content: "Hafizur Rahman",
    
};
    
axios.patch('http://127.0.0.1:8000/apiV1/status/update/6/', u_Status,{
    headers: {
        "Content-Type": "application/json"
    }
})
    .then(response => {
        console.log(response.data); 
         // Display fetched data
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });