window.addEventListener("load",registerEvents,false)

function registerEvents(e){
document.getElementById("submit-button").addEventListener("click",getIp,false);
}

function getIp(e){
let xhttp = new XMLHttpRequest();
	xhttp.onload = function(res){  document.getElementsByName("textarea")[0].innerHTML = JSON.parse(this.responseText).msg  }
	xhttp.open("get","http://localhost:8000/xml")
	xhttp.send();
}
