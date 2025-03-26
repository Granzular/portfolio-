window.addEventListener("load",{()=>
questionDict = {}
for (i=1;i<=document.forms.length;i++){questionDict[i]=""}
                                                                        [... document.getElementsByName("option")].map((f)=> f.addEventListener("click",select,false));                                                                                                                 function select(e){
  questionDict[e.target.form.id]=e.target.value;
        for (i=1;i<= document.forms.length;i++){console.log(questionDict[i])}                                                               

}                                                                     document.getElementById("submit-button").addEventListener("click",submit,false);                                                                                                                                  function listener(){                                                          if (this.status == 200){                                              var data = JSON.parse(this.responseText);
        console.log(data.username);
        console.log(data.score);
        Alert("Sumbited successfully! Arigatou");
        window.location.reload();
}
        else{console.log(this.status);                                        }       }
function submit(e){
        var csrftoken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
        xhtml = new XMLHttpRequest();
        xhtml.onload = listener;
        xhtml.open("POST","http://localhost:8081/tools/adderTest/test/",true);
        xhtml.setRequestHeader("Content-Type","application/json");            xhtml.setRequestHeader("X-CSRFToken",csrftoken);
        xhtml.send(JSON.stringify(questionDict));
} },false);
