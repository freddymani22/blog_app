
const form = document.querySelector('#post-form');



form.addEventListener('submit', async (e) => {
  e.preventDefault()
  const title = document.querySelector('#title').value;
  const content = document.querySelector('#content').value;
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  const data = { title: title, content: content }
  const headers = {
    headers: {
      'X-CSRFToken': csrfToken
    }
  }
  try {
    await axios.post('http://localhost:8000/api/', data, headers);
    window.location.href = 'http://localhost:8000/';

  }
  catch (error) {
    console.log(error);
  }

});



