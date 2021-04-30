var script = document.createElement('script');
script.src = 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

document.addEventListener('DOMContentLoaded', function() {

  function compose_post() {
    document.querySelector('form').onsubmit = function() {
      const content = document.querySelector('#new_post').value;
      fetch('/posts' {
        method: 'POST',
        body: JSON.stringify({
            content: content
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
          console.log(result);

      })

    }
  }

})
