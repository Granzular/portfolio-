window.addEventListener("load",registerEvents,false);

function registerEvents(e){
    
    const sun = "/media/images/sun.svg";
    const moon = "/media/images/moon.svg";
    
    const toggle_icon = document.querySelector("#theme-toggle-icon");
    
    const root = document.querySelector("html");
    init_theme(localStorage.getItem("theme"));
    toggle_icon.addEventListener("click",toggle_theme,false);
    
    /* helper functions definitions */
    
    function init_theme(theme){
        
        if (theme=="dark-theme"){
            root.classList.add("dark");
            toggle_icon.alt = "🌞";
            toggle_icon.src = sun;
        }
        else if(theme == "light-theme"){
            root.classList.remove("dark");
            toggle_icon.alt = "🌙";
            toggle_icon.src = moon;
        }
        else if(theme == null){
            localStorage.setItem("theme","light-theme");
            root.classList.remove("dark");
            toggle_icon.alt = "🌙";
            toggle_icon.src = moon;
        }
    }
    
    function toggle_theme(e){
        
        let theme = localStorage.getItem("theme");
        
        if (theme == "dark-theme"){
            root.classList.remove("dark");
            toggle_icon.alt = "🌙";
            toggle_icon.src = moon;
            localStorage.setItem("theme","light-theme")
        }
        else if(theme == "light-theme"){
            root.classList.add("dark");
            toggle_icon.alt = "🌞";
            toggle_icon.src = sun;
            localStorage.setItem("theme","dark-theme");
        }
    }
}
