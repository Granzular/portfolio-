function setBox(){
 document.write(`
    <div class="alert-box">
    <p class="alert-box-msg">Text</p>
    <button class="alert-ok">OK</button>
  </div>
    `);
}

function __Alert(text="",next=false){
    document.write(`<style>
  .alert-box{
    background-color:white;                                                                 width:80%;                                                                              height:150px;                                                                           padding-left:20px;
    padding-right:20px;
    margin-left:10px;
    margin-right:10px;
    top:30%;                                                              text-align:center;
    border-style:groove;
    border-radius:5px;
    z-index:10000;
    position:relative;
    display:none;
    box-shadow:0 0 300px rgba(0,0,0,0.8);

  }
  .alert-ok{
    position:absolute;
    top:70%;
    left:80%;
    width:15%;
  } </style>                                                                                `);
    var box = document.getElementsByClassName("alert-box")[0];
    box.style.display = "block";

    box.querySelector("p").innerHTML = text;
    box.querySelector("button").addEventListener("click",()=>{box.style.display="none";
	    if (next != false){next();}
    },false)                                                }
function Alert(text="",next=false){
	setBox();
	__Alert(text=text,next=next)

}
