/*Changement de texte sans chargement */
var button_next = document.getElementById('change_phrase_suivant');
var button_prev = document.getElementById('change_phrase_precedent');
content = document.getElementById('phrase');
stxt = document.getElementById('sous_titre')

const texte_options = 
["My name is Valentin Torres I’m 18 and I’m currently studying Networking and Telecomunication.<br>Half Alsacian and Half Spanish I spend my whole life in Bas-Rhin but I’m currently living in Haut-Rhin for my studies.<br>Without transition what allows the best to define someone according to me is there passions so here are mine.<br>My domain passion n°1 was the computer science but being very curious by nature I always wanted to discover new hobbies consequently I count good number of passion video games, cars , mechanical sport, all forms of mechanics , space, video, photography etc..."
,"Being always passionate about computer science thanks to my dad it was obvious for me that I would study this subject.<br>L’informatique étant un très large spectre il ma fallu avoir une réflexion sur les élément me plaisant le plus dans l’informatique il s’est avérer que mes domaine favoris sont les réseau et les infrastructure informatique.<br>Computer science is a huge domain so I had to think about what exactly I liked in computer science  and its networking and computer infrastructure.<br>Also I’m not a big fan of long studies I think that 3 year will be enough.<br>So it was finally an evidence to go to studies in the BUT N&T "
,"Studies : <br> 2019 – 2022 General baccalaureate with honors  <br> 2022-In progress BUT Networking and Telecomunication <br> Work : <br> 2018 Traineeship at the computer science department -Lactalis Deutchland <br> August 2022 Holiday replacement – Usocome Brumath"];
const soustxt_options = ["Who Am I","Why N&T","Experience"];

var i = 0;
content.innerHTML = texte_options[i];
stxt.innerHTML = soustxt_options[i];

button_next.onclick = function() {
  if (i == 2){
    i = 0;
  }else{
    i = i + 1;
  }
  content.innerHTML = texte_options[i];
  stxt.innerHTML = soustxt_options[i];
}

button_prev.onclick = function() {
  if (i == 0){
    i = 2;
  }else{
    i = i - 1;
  }
  content.innerHTML = texte_options[i];
  stxt.innerHTML = soustxt_options[i];
}


/*Animation de l'avatar */
let el = document.getElementById('avatar')

const height = el.clientHeight
const width = el.clientWidth


el.addEventListener('mousemove', handleMove)

function handleMove(e) {

  const xVal = e.layerX

  const yVal = e.layerY
  
  /* Calcul des valeurs de rotation 
  le multiplicateur change l'intensiter de la rotation
    */
  const yRotation = 30 * ((xVal - width / 2) / width)
  
  const xRotation = -30 * ((yVal - height / 2) / height)
  

  const string = 'perspective(500px) scale(1.1) rotateX(' + xRotation + 'deg) rotateY(' + yRotation + 'deg)'
  
  el.style.transform = string
}


el.addEventListener('mouseout', function() {
  el.style.transform = 'perspective(500px) scale(1) rotateX(0) rotateY(0)'
})

el.addEventListener('mousedown', function() {
  el.style.transform = 'perspective(500px) scale(0.9) rotateX(0) rotateY(0)'
})

el.addEventListener('mouseup', function() {
  el.style.transform = 'perspective(500px) scale(1.1) rotateX(0) rotateY(0)'
})