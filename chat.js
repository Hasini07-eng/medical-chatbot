async function sendMessage(){

let input = document.getElementById("userInput");
let text = input.value.trim();

if(text==="") return;

addMessage(text,"user");

let response = await fetch("http://127.0.0.1:5000/chat",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({message:text})
});

let data = await response.json();

addMessage(data.response,"bot");

input.value="";
}

function addMessage(text,type){

let msg=document.createElement("div");
msg.classList.add("message",type);
msg.innerText=text;

document.getElementById("messages").appendChild(msg);
}