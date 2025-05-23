window.addEventListener('load',registerEvents,false);

function  registerEvents(e){
	document.getElementById('message-form').addEventListener('submit',(e)=>{
		const msgform = e.target;
		e.preventDefault();
		const alertBox = document.getElementById('alert-box');
		const formdata = new FormData();
		formdata.append('email',document.getElementById('id_email').value);
		formdata.append('message', msgform.message.value);
		let csrf = msgform.csrfmiddlewaretoken.value;
		
		let xhttp = new XMLHttpRequest();
		xhttp.onload = (response)=>{
			if (xhttp.status == 200){
				alertBox.innerHTML = (`<div class='alert alert-success' role='alert'>
				Message Sent
			</div>	`);
			}
			else{
				alertBox.innerHTML = (`<div class='alert alert-danger' role='alert'>
				oops! an error occured
					</div>  `)
			}
		}
		xhttp.open('POST',MESSAGE_URL,true);
	
		xhttp.setRequestHeader('X-CSRFToken',csrf);
		xhttp.send(formdata);
	},false);
}
