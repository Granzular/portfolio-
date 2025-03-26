window.addEventListener("load",imageSlide,false);

function doAjax(e){
    function listener(){
      if (this.status==200){     
     let dct = JSON.parse(this.responseText);
        for (i in dct){
          console.log(dct[i].title);
        }
        let lst = [];
        for (j in dct){
          lst.push(j);
          
        }
        startCarousel(dct,lst,0);
      }
      else{
        alert("An error occured !");
      }
    }
    let xhttp = new XMLHttpRequest();
    xhttp.onload = listener;
    xhttp.open('get',AJAX_URL,true);
    xhttp.send();
  }
  function startCarousel(posts,id_lst,c){
    if (c>2){c=0}
    if (c <3){
      console.log(id_lst.length);
      let post = posts[id_lst[c]];
    let titleEl = document.getElementById("title");
      let urlEl = document.getElementById("url");
    let bodyEl = document.getElementById("preview");
      titleEl.innerHTML = post.title; 
     urlEl.href = post.url;  
    bodyEl.innerHTML= post.preview;
    c++;
      setTimeout(startCarousel,2000,posts,id_lst,c);}
     
}
console.log("hello");

function imageSlide(e){
   slides= ["test_image/tech_background01.jpg","test_image/tech_background02.jpg","test_image/tech_background03.jpg"];

    imgEl = document.getElementsByClassName("featuredImage")[0];
    slider(slides,imgEl,0);
	function slider(slides,imgEl,c){
    if (c>2){c=0;}
	imgEl.src = STATIC_URL + slides[c];
	c++;
	setTimeout(slider,3000,slides,imgEl,c);
	}
  
}
