document.addEventListener('DOMContentLoaded', () => {
  // Make enter/return key send message
  let msg = document.querySelector('#user_message');
  msg.addEventListener('keyup', event => {
    event.preventDefault();
    if (event.keyCode === 13) {
      document.querySelector('#send-message').click();
    }
  })
})
