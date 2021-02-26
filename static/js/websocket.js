// Js to enable websocket when a chat is selected

chatSocket = new ReconnectingWebSocket(
    'ws://' + window.location.host + '/ws/chat/' + chatId + '/'
);

// if we receive message from websocket, append to text area
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    let receivedMsg = data.message;

    // if message is from sender
    let newBubble = `<li class="you">
                        <div class="entete">
                            <button class="status green"></button>
                            <h2>` + receivedMsg.by + `</h2>
                            <h3>` + receivedMsg.time + `</h3>
                        </div>
                        <div class="triangle"></div>
                        <div class="message">
                          ` + receivedMsg.message + `
                        </div>
                    </li>`
    if (receivedMsg.by == participantName) {
        newBubble = `<li class="me">
                        <div class="entete">
                            <h3>` + receivedMsg.time + `</h3>
                            <h2>` + receivedMsg.by + `</h2>
                            <button class="status blue"></button>
                        </div>
                        <div class="triangle"></div>
                        <div class="message">
                          ` + receivedMsg.message + `
                        </div>
                    </li>`
    }
    chatMessageArea.innerHTML += newBubble;
    //focus on the last message
    focusOnLastMsg()
}
chatSocket.onclose = function(e) {
    console.error('Socket closed, I repeat, socket closed');
};

// send the message to websocket on send button click
//const chatTextArea = document.getElementById('chat-message-input');
//let sendBtn = null;
let sendBtn = document.getElementById('chat-message-submit');

sendBtn.addEventListener('click', function(){
    const message = chatTextArea.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    chatTextArea.value = "";
});
