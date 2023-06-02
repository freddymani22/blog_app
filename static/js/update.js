// Get the article slug from local storage
const slug = localStorage.getItem('article-title');

// Define the API URL
let apiUrl = `http://localhost:8000/api/${slug}/`;


function fetchData() {
  fetch(apiUrl)
    .then(response => response.json())
    .then(post => {
      let container = document.querySelector('.detail-container');
      container.innerHTML = ''; // clear the container
      // create a new article element
      let article = document.createElement('article');
      article.classList.add('media', 'content-section');

      // create the author image
      let img = document.createElement('img');
      img.classList.add('rounded-circle', 'article-img');
      img.src = post.profile_pic;
      article.appendChild(img);

      // create the media body
      let mediaBody = document.createElement('div');
      mediaBody.classList.add('media-body');
      article.appendChild(mediaBody);

      // create the article metadata
      let articleMetadata = document.createElement('div');
      articleMetadata.classList.add('article-metadata');
      mediaBody.appendChild(articleMetadata);

      // create the thumbnail
      let thumbnail = document.createElement('div');
      thumbnail.classList.add('thumbnail');
      articleMetadata.appendChild(thumbnail);

      // create the author link
      let authorLink = document.createElement('a');
      authorLink.classList.add('mr-2');
      authorLink.href = `/user/${post.author}/`;
      authorLink.innerText = post.author;
      thumbnail.appendChild(authorLink);

      // create the date posted
      let datePosted = document.createElement('small');
      datePosted.classList.add('date', 'text-left');
      datePosted.innerText = new Date(post.date_posted).toLocaleDateString('en-US', {
        month: 'long',
        day: '2-digit',
        year: 'numeric'
      });
      thumbnail.appendChild(datePosted);

      // create the article title
      let title = document.createElement('h2');
      let titleLink = document.createElement('a');
      titleLink.classList.add('article-title', 'text-center');
      titleLink.setAttribute('id', post.slugs);
      titleLink.href = `post/${post.slugs}`;
      titleLink.innerText = post.title;
      title.appendChild(titleLink);
      thumbnail.appendChild(title);

      // create the post image
      if (post.img_post) {
        let imgPost = document.createElement('img');
        imgPost.classList.add('img-thumbnail', 'd-flex');
        imgPost.src = post.img_post;
        imgPost.alt = post.title;
        thumbnail.appendChild(imgPost);
      }

      // create the post content
      let caption = document.createElement('div');
      caption.classList.add('caption');
      let content = document.createElement('p');
      content.classList.add('lead');
      content.innerText = post.content;
      caption.appendChild(content);
      thumbnail.appendChild(caption);

      container.appendChild(article);
      const h2 = document.createElement('h2');
      h2.innerText = 'Comments'
      container.appendChild(h2)

      if (post.comments && post.comments.length > 0) {
        const commentsSection = document.createElement('article');

        commentsSection.classList.add('media', 'content-section');
        const commentArticleMetadata = document.createElement('div')
        commentArticleMetadata.classList.add('article-metadata')
        commentsSection.appendChild(commentArticleMetadata)
        const commentMaindiv = document.createElement('div')
        commentArticleMetadata.appendChild(commentMaindiv)
        for (let comment of post.comments) {
          const commentText = document.createElement('p');
          commentText.classList.add('article-content')
          const commentUserLink = document.createElement('a');
          commentUserLink.classList.add('d-inline', 'link-white')
          commentUserLink.innerText = comment.username
          commentUserLink.href = 'http://localhost:8000/user/' + comment.username;
          commentText.innerText = comment.comment_text
          const hr = document.createElement('hr')
          commentText.append(hr)
          commentMaindiv.appendChild(commentUserLink)
          commentMaindiv.appendChild(commentText);
        }


        container.appendChild(commentsSection);

      } 

    })
    .catch(error => {
      console.error(error);
    });
}



const commentForm = document.querySelector('#commentsForm');
commentForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const comment = document.querySelector('#comment').value;
  const data = { comment_text: comment };
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  document.querySelector('#comment').value = '';


  axios.post(`http://localhost:8000/api/comments/${slug}/`, data,
    {
      headers: {
        'X-CSRFToken': csrfToken
      }

    })
})

const deletePost = document.querySelector('#post-delete')
deletePost.addEventListener('click', () => {

  alert('do you want to delete the post?')
  postDelete()
  window.location.href = 'http://localhost:8000/';

})


const postDelete = async () => {
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  const deleteSlug = localStorage.getItem('article-title')
  try {
    await axios.delete(`http://localhost:8000/api/${deleteSlug}/`,{ headers: { 'X-CSRFToken': csrfToken } })
  } catch (e) {
    console.log(e)
  }
}



const updatePost = document.querySelector('#post-update')
updatePost.addEventListener('click', () => {

 const slugs = localStorage.getItem('article-title')
  window.location.href = `http://localhost:8000/post/${slugs}/update/`;

})


// const postUpdate = async () => {
//   const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//   const updateSlug = localStorage.getItem('article-title')
//   try {
//     await axios.update(`http://localhost:8000/api/${updateSlug}/`,{ headers: { 'X-CSRFToken': csrfToken } })
    
//   } catch (e) {
//     console.log(e)
//   }
// }