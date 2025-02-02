window.addEventListener("load",registerEvents,false);


function registerEvents(e){
	getPosts();
}

function getPosts(){
    var xhttp = new XMLHttpRequest();
    xhttp.onload = startSlide;
    xhttp.open("get","http://localhost:8000/ajaxIndex/",true);
    xhttp.send();}	

function startSlide(){
 if (this.status == 200){ 
	 let data = JSON.parse(this.responseText);
	 console.log(data.name);
 }}

function updateSlide(){
	let frame = document.getElementsByClassName("post-title");
	console.log(BASE_URL);
	console.log(DETAIL_URL);
	for (i of frame){
		console.log(i);
	}
}
