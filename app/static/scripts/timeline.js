/* Sending the formData object as payload using Fetch */

const form = document.getElementById('form');
console.log('hello')
form.addEventListener('submit', function (e) {
    // Prevent default behavior:
    e.preventDefault();
    // Create payload as new FormData object:
    console.log('submit')
    // const payload = new FormData(form);
    // // Post the payload using Fetch:
    // fetch('https://httpbin.org/post', {
    // method: 'POST',
    // body: payload,
    // })
    // .then(res => res.json())
    // .then(data => console.log(data))
})