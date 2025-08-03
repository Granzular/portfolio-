
window.addEventListener("load",registerEvents,false);
  function registerEvents(e){
    document.getElementById("top-menu-icon").addEventListener("click",toggleMenu,false);
   // document.getElementById("top-menu-home").addEventListener("click",toggleMenu,false);
  }
  
  function toggleMenu(e){
    let menuEl= document.getElementById("top-menu");
    
    let compStyle = window.getComputedStyle(menuEl);
    
    let propValue = compStyle.getPropertyValue("display");
    console.log("this "+ propValue);
    if (propValue==="none"){
      menuEl.style.display = "block";
      e.target.src = STATIC_URL + "images/close.png";
    }
    else{
      menuEl.style.display = "";
      e.target.src = STATIC_URL + "images/menuicon01.png"
    }

  }
