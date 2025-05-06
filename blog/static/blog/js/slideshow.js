window.addEventListener("load",imageSlide,false);


function imageSlide(e){
   slides= ["test_image/tech_background01.jpg","test_image/tech_background02.jpg","test_image/tech_background03.jpg"];

    imagelist = document.getElementsByClassName("featured-image")
    imgEl = document.getElementById("url");
    slider(imagelist,imgEl,0);

	function slider(slides,imgEl,c){
    if (c>2){c=0;}
	 imgEl.children[0]= slides[c];
	c++;
	setTimeout(slider,3000,slides,imgEl,c);
	}
  
}
