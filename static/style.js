let circle = document.getElementById('circle');
let fadeLeft = document.querySelectorAll('.fadeleft');
let fadeRight=document.querySelectorAll ('.faderight');
let fadeForward=document.querySelectorAll ('.fadeforward');
let card= document.getElementById('cardtext');
let main= document.querySelectorAll('.img');
let mybutton = document.getElementById("myBtn");
let likealert = document.getElementById('likealert')
 let toggle= document.getElementById('navlinks')
 let commentalert= document.getElementById('commentalert')


function Toggle(){
  
  if (toggle.style.display ==="none" ){ 
    toggle.style.display ="flex";

    
}
else{
  toggle.style.display ="none";
 
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
  console.log('message top')
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


observer = new IntersectionObserver((entries) =>{
  
  entries.forEach(entry=>{

  if (entry.intersectionRatio > 0){ 
      entry.target.style.animation = 'fadesleft 1s ease-out';

      
  }
  else{
    entry.target.style.animation='none';
   
  }
})
})

fadeLeft.forEach(fadeleft => {
    observer.observe(fadeleft)
})


observer = new IntersectionObserver((entries) =>{
  
  entries.forEach(entry=>{

  if (entry.intersectionRatio > 0){ 
      entry.target.style.animation = 'fadesright 2s ease-out';
      
  }
  else{
    entry.target.style.animation='none';
   
  }
})
})

fadeRight.forEach(faderight => {
    observer.observe(faderight)
})

fadeLeft.forEach(fadeleft => {
  observer.observe(fadeleft)
})


observer = new IntersectionObserver((entries) =>{

entries.forEach(entry=>{

if (entry.intersectionRatio > 0){ 
    entry.target.style.animation = 'fadesforward 3s ease-out';
    
}
else{
  entry.target.style.animation='none';
 
}
})
})

fadeForward.forEach(fadeforward => {
  observer.observe(fadeforward)
})


const onMouseMove = (e) =>{
  circle.style.left = e.pageX + 'px';
  circle.style.top = e.pageY + 'px';



}
document.addEventListener('mousemove', onMouseMove);

function pointLarge(){
circle.style.height ="180px";
circle.style.width ="180px";
circle.style.color="white";
circle.innerText="exploring every thought";
circle.style.opacity=".8"

}


function pointNormal(){
    circle.style.height ="10px";
    circle.style.width ="10px";
    circle.innerText="";
    
  }

function cardEffect(){
  console.log('this is card');
  card.style.zIndex = "3";

}
