window.addEventListener("load",registerEvents,false);

function registerEvents(e){
    
    const toggle_icon = document.querySelector("#theme-toggle-icon");
    
    const theme_link = document.querySelector("#dark-theme");//link tag for dark theme css
    init_theme(localStorage.getItem("theme"));
    toggle_icon.addEventListener("click",toggle_theme,false);
    
    /* helper functions definitions */
    
    function init_theme(theme){
        if (theme=="dark-theme"){
            theme_link.disabled = false;
            toggle_icon.innerHTML = "🌞";
        }
        else if(theme == "light-theme"){
            theme_link.disabled = true;
            toggle_icon.innerHTML = "🌙";
        }
        else if(theme == null){
            localStorage.setItem("theme","light-theme");
            theme_link.disabled = true;
            toggle_icon.innerHTML = "🌙";
        }
    }
    
    function toggle_theme(e){
        
        let theme = localStorage.getItem("theme");
        
        if (theme == "dark-theme"){
            theme_link.disabled = true;
            toggle_icon.innerHTML = "🌙";
            localStorage.setItem("theme","light-theme")
        }
        else if(theme == "light-theme"){
            theme_link.disabled = false;
            toggle_icon.innerHTML = "🌞";
            localStorage.setItem("theme","dark-theme");
        }
    }
}