

function getPosts() {
    console.log('getting posts')
    fetch(`/api/timeline_post`, {
        method: 'GET'
    })
        .then(res => res.json())
        .then((data) => {
            data.timeline_posts.forEach((post) => generatePost(post))
        })
        .catch(err => console.log(err))
}


/* Sending the formData object as payload using Fetch */

const form = document.getElementById('form');


form.addEventListener('submit', function (e) {
    // Prevent default behavior:
    e.preventDefault()
    // Create payload as new FormData object:
    console.log('submit')
    const payload = new FormData(form);
    // Post the payload using Fetch:
    fetch(`/api/timeline_post`, {
        method: 'POST',
        body: payload,
    })
        .then(res => res.json())
        .then((data) => {
            generatePost(data)
        })
        .catch(err => console.log(err))

    const inputs = document.getElementsByClassName('timeline_input')

    for (input of inputs) {
        input.value = ""
    }
})

function generatePost(data) {

    const timeline_posts = document.getElementById("timeline_posts")

    const timeline_card = document.createElement('div')
    timeline_card.classList.add('timeline_card')

    const timeline_header = document.createElement('div')
    timeline_header.classList.add('timeline_header')

    const timeline_person = document.createElement('div')
    timeline_person.classList.add('timeline_person')

    const timeline_photo = document.createElement('h2')
    timeline_photo.classList.add('timeline_photo')
    timeline_photo.textContent = data.name[0]

    const timeline_personInfo = document.createElement('div')
    timeline_personInfo.classList.add('timeline_personInfo')

    const timeline_personInfo_h3 = document.createElement('h3')
    timeline_personInfo_h3.textContent = data.name

    const timeline_personInfo_p = document.createElement('p')
    timeline_personInfo_p.textContent = data.email

    timeline_personInfo.appendChild(timeline_personInfo_h3)
    timeline_personInfo.appendChild(timeline_personInfo_p)

    timeline_person.appendChild(timeline_photo)
    timeline_person.appendChild(timeline_personInfo)

    const timeline_date = document.createElement('p')
    timeline_date.classList.add('timeline_date')
    timeline_date.textContent = data.created_at

    timeline_header.appendChild(timeline_person)
    timeline_header.appendChild(timeline_date)

    const timeline_content = document.createElement('p')
    timeline_content.classList.add('timeline_content')
    timeline_content.textContent = data.content

    timeline_card.appendChild(timeline_header)
    timeline_card.appendChild(timeline_content)

    timeline_posts.prepend(timeline_card)

}