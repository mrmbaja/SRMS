document.querySelector("form").addEventListener("submit", function(event) {
    const username = document.querySelector("input[name='username']").value;
    const email = document.querySelector("input[name='email']").value;
    const password = document.querySelector("input[name='password']").value;
    const student_id = document.querySelector("input[name='student_id']").value;

    if (username === "" || email === "" || password === "" || student_id === "") {
        alert("All fields are required!");
        event.preventDefault();
    }
});
