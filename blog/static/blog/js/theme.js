window.addEventListener("load",function(e){
    const theme_link = document.querySelector("#dark-theme");
    
    const toggle_icon = document.querySelector("#theme-toggle-icon");
    toggle_icon.addEventListener("click",change_theme);
    function change_theme(e){
        e.target.classList.toggle("dark-theme");
        if (e.target.classList.contains("dark-theme")){
            e.target.innerHTML = "☀️";
            theme_link.disabled = false;
        }
        else{
         e.target.innerHTML =  "🌙";
            theme_link.disabled = true;
        }
    }
}
);

