window.addEventListener("load",registerEvents);


function set_active_link(){
    /* Only works properly for a multipage website; if the links are on the same page, unwanted behaviours. shall be updated.*/
    const nav_links = document.querySelectorAll(".nav-link");
    for(i of nav_links){
        console.log(i.href);
        if(i.href === window.location.href){
            
            i.classList.add("active-link");
        }
        else{
            i.classList.remove("active-link");
        }
    }
    }

function registerEvents(e){
    set_active_link();
    const nav_links = document.querySelectorAll(".nav-link");
    const menu_icon = document.querySelector("#menu-icon");
    const close_icon = 
    document.querySelector("#close-icon");
    const navbar_ul = document.querySelector("#navbar-ul"); // navbar_ul is the navbar that is seen presentationally, it is a ul tag, the actual nav tag is used as a container
    menu_icon.addEventListener("click",open_navbar);
    close_icon.addEventListener("click",close_navbar);
    
    function  open_navbar(e){
        navbar_ul.style.display = "block";
    }
    
    function close_navbar(e){
        navbar_ul.style.display = "none";
    }
    
}


