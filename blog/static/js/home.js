function fetchData() {
    fetch('http://localhost:8000/api/')
      .then(response => response.json())
      .then(data => {
        let container = document.getElementById('my-data-container');
        container.innerHTML = ''; // clear the container
        
        for (let post of data) {
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
          datePosted.classList.add('text-muted');
          datePosted.innerText = new Date(post.date_posted).toLocaleDateString();
          thumbnail.appendChild(datePosted);
  
          // create the article title
          let title = document.createElement('h2');
          title.classList.add('display-5');
          let titleLink = document.createElement('a');
          titleLink.classList.add('article-title');
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
          content.classList.add('text-muted');
          content.innerText = post.content;
          caption.appendChild(content);
          thumbnail.appendChild(caption);
  
          container.appendChild(article);
        }
        setTimeout(fetchData, 1000);
      })
      .catch(error => {
        console.error(error);
      });
  }
  
  fetchData(); // Start polling, set timeout so that it can request for 1 sec
  
  
  fetchData(); // Start fetching data
  