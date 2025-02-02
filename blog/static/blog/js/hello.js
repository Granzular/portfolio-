
function hello(){
	let a = document.getElementsByClassName("link");
	if (a[0].hasAttribute("hidden")){
	for(i of a){i.removeAttribute("hidden")}
	}
	else{
	for (j of a){j.setAttribute("hidden","");}}
}

function hi(){
	const newel = document.createElement("p");
	newel.textContent = "hi";
	document.body.appendChild(newel);

}

function i(){
 alert("Hii:");
}
