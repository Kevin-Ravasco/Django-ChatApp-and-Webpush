let chatId = null;
let participantName = '';
let chatMessageArea = null;
let chatTextArea = null;

function focusOnLastMsg(){
    var ele = document.querySelectorAll('.entete button');
    if (ele.length > 1){
        ele[ele.length - 1].focus();
    }
}

$(document).ready(function(){
    const validatePaymentUrl = "/messages/"
    const participantInfoUrl = "/participant/"
    let chatListBtns = document.getElementsByClassName('chat-list');
    chatMessageArea = document.getElementById('chat-messages-area');
    chatTextArea = document.getElementById('chat-message-input');
//    chatTextArea.focus();

    for (i = 0; i < chatListBtns.length; i++) {
        chatListBtns[i].addEventListener('click', function(){
            chatId = this.id;
            participantName = document.getElementById('name-' + chatId).innerHTML;
            getChats(chatId);
            getParticipantInfo(chatId);
            appendWebsocketScripts()
        })
    }

    function appendWebsocketScripts() {
        var tag = document.createElement("script");
        tag.src = "/static/js/websocket.js";
        document.getElementsByTagName("script")[0].appendChild(tag);
    }


    function getChats(id){
        $.ajax({
            type: 'GET',
            url: validatePaymentUrl + id,
            success: function (response) {
                // update the messages area
                chatMessageArea.innerHTML = response;
                //focus on the last message
                focusOnLastMsg()
            },
            error: function(error) {
               console.log(error)
            }
        })
    }


    function getParticipantInfo(id){
        $.ajax({
            type: 'GET',
            url: participantInfoUrl + id,
            success: function (response) {
                // change the header
                let chatHeader = document.getElementById('chat-header');
                chatHeader.innerHTML = response;
            },
            error: function(error) {
               console.log(error)
            }
        })
    }

})