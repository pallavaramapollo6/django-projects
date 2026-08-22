fetch("http://127.0.0.1:8000/api/students/")
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });