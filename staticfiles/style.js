

let card= document.getElementById('cardtext');
let main= document.querySelectorAll('.img');
let mybutton = document.getElementById("myBtn");
let likealert = document.getElementById('likealert')
let toggle= document.getElementById('navlinks')
const xbar = document.getElementById('x')
const ham = document.getElementById('ham')
let commentalert= document.getElementById('commentalert')
let commentlert= document.getElementById('episodecommentalert')



function Toggle(){
  
  if (toggle.style.display == "none"){ 
    toggle.style.display ="flex"; 
    xbar.style.display ="block";
    ham.style.display ="none";
}
else{
  toggle.style.display ="none";
  xbar.style.display ="none";
  ham.style.display ="block";
 
}
}

function Verify(){
  likealert.innerText='You must be Logged in to like this post ';
  setTimeout(() => {
  
    likealert.innerText = '';
  }, 3000);
  console.log('wotking like');
}


function commentAlert(){
  commentalert.innerText='You must be Logged in to Comment ';
  setTimeout(() => {
  
    commentalert.innerText = '';
  }, 2000);
  console.log('wotking like');
}

function topFunction() {
 
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}




function cardEffect(){
  console.log('this is card');
  card.style.zIndex = "3";

}
function VerifyComment(){
  commentlert.innerText='You must be Logged in to comment ';
  setTimeout(() => {
  
    commentlert.innerText = '';
  }, 3000);
 
}
