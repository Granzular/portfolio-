window.addEventListener("load",registerEvents,false);

function registerEvents(e){
	const list = document.querySelectorAll('.list-item-link');
	const current_href = window.location.href;
	for ( item of list){
		if (item.href == current_href){
			item.classList.add('current-page-nav-link');		
		}
		else{
			item.classList.remove('class','current-page-nav-link');
		}
	}

}

