 document.addEventListener('DOMContentLoaded', () => {
   var socket = io();

   let room = "Lounge";
   joinRoom("Lounge");
   // Display The Messages
   socket.on('message', data => {
     const p = document.createElement('p');
     const span_username = document.createElement('span');
     const span_timestamp = document.createElement('span');
     const br = document.createElement('br');
     if (data.username) {
       span_username.innerHTML = data.username;
       span_timestamp.innerHTML = data.time_stamp;
       p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;
       document.querySelector('#display-message-section').append(p);
     } else {
       printSysMsg(data.msg);
     }
   });

   // Send Message
   document.querySelector('#send-message').onclick = () => {
     socket.send({'msg': document.querySelector('#user_message').value, 'username': username, 'room': room});
     // Clear Input Area
     document.querySelector('#user_message').value = '';
   }

   // Room Selection
   document.querySelectorAll('.select-room').forEach(p => {
     p.onclick = () => {
       let newRoom = p.innerHTML;
       if (newRoom == room) {
         msg = `You are already in the ${room} room.`;
         printSysMsg(msg);
       } else {
         leaveRoom(room);
         joinRoom(newRoom);
         room = newRoom;
       }
     }
   });

   // Leave room
   function leaveRoom(room) {
     socket.emit('leave', {'username': username, 'room': room});
   }

   // Join room
   function joinRoom(room) {
     socket.emit('join', {'username': username, 'room': room});
     // Clear the screen
     document.querySelector('#display-message-section').innerHTML = '';
     // Autofocus the text entry box
     document.querySelector('#user_message').focus();
   }

   // Print system message
   function printSysMsg(msg) {
     const p = document.createElement('p');
     p.innerHTML = msg;
     document.querySelector('#display-message-section').append(p);
   }

 })
