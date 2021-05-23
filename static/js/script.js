
/* LOADER TIMING ANIMATION */
setTimeout(function(){
			$('.loader').fadeToggle();
		},3000);

/* PERCENTAGE ANIMATION */
var percent = document.querySelector('.percentage');
var count=10;
var per=16;
var loading=setInterval(animate,50);
function animate(){
	if(count==100 && per==100){
		clearInterval();
	}else{
		per=per+10;
		count=count+1;
		percent.textContent=count+'%';
	}
};

/* HAMBURGER ANIMATION */
var ham=document.querySelector('#navigation .nav-list .ham');
	var mobile_menu=document.querySelector('#navigation .nav-list .nav-menu');
	var header=document.querySelector('#navigation .nav-list');

	ham.addEventListener('click',()=>{
		ham.classList.toggle('active');
		mobile_menu.classList.toggle('active');
	});

