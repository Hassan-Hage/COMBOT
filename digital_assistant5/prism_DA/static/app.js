class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // show or hides the box
        if(this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          .then(r => {
            let msg2 = { name: "Cubot", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }

    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Cubot")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }
}


const chatbox = new Chatbox();
chatbox.display();

function uploadFile(form)
{
 const formData = new FormData(form);
 var oOutput = document.getElementById("static_file_response")
 var oReq = new XMLHttpRequest();
     oReq.open("POST", "upload_static_file", true);
 oReq.onload = function(oEvent) {
     if (oReq.status == 200) {
       oOutput.innerHTML = "File uploaded succesfully!";
       console.log(oReq.response)
     } else {
       oOutput.innerHTML = "Error! No file selected<br \/>";
     }
     };
 oOutput.innerHTML = "Sending file!";
 console.log("Sending file!")
 oReq.send(formData);
}

// Array.prototype.forEach.call(
//     document.querySelectorAll(".file-upload__button"),
//     function(button) {
//       const hiddenInput = button.parentElement.querySelector(
//         ".file-upload__input"
//       );
//       const label = button.parentElement.querySelector(".file-upload__label");
//       const defaultLabelText = "No file selected";
  
//       // Set default text for label
//       label.textContent = defaultLabelText;
//       label.title = defaultLabelText;
  
//       button.addEventListener("click", function() {
//         hiddenInput.click();
//       });
  
//       hiddenInput.addEventListener("change", function() {
//         const filenameList = Array.prototype.map.call(hiddenInput.files, function(
//           file
//         ) {
//           return file.name;
//         });
  
//         label.textContent = filenameList.join(", ") || defaultLabelText;
//         label.title = label.textContent;
//       });
//     }
//   );


// const inpFile = document.getElementById("inpFile");

// inpFile.addEventListener("change", function () {
//     console.log(inpFile.files);
// });


const myForm = document.getElementById("myForm");
const inpFile = document.getElementById("inpFile");

myForm.addEventListener("submit", e => {
  e.preventDefault();

  const endpoint = "upload.php";
  const formData = new FormData();

  console.log(inpFile.files);


  formData.append("inpFile",inpFile.files[0]);

  fetch(endpoint, {
    method: "post",
    body: formData
    
  }).catch(console.error);

});



