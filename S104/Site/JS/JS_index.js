/*Changement de texte sans chargement */
var button_next = document.getElementById('change_phrase_suivant');
var button_prev = document.getElementById('change_phrase_precedent');
content = document.getElementById('phrase');
stxt = document.getElementById('sous_titre')

const texte_options = 
["Je m’appelle Valentin Torres j’ai 18 ans et je suis actuellement étudiant en Réseau et Télécommunication.<br>Moitié Alsacien moitié espagnol j’ai toujours vécu dans le Bas-Rhin mais je me retrouve désormais dans le haut Rhin pour suivre mes études.<br>Sans transition ce qui permet le mieux de cerner quelqu’un selon moi c’est ces passions par conséquent voici les miennes.<br>Mon domaine passion n°1 a été l’informatique mais étant de nature très curieux j’ai toujours cherché à découvrir de nouveau domaine par conséquent je dénombre bon nombre de passion les jeux vidéo, l’automobile, les sport mécanique, la mécanique sous toutes ces formes, le spatial, la vidéo, la photo etc…"
,"Ayant toujours été passionner d’informatique via mon père il fut normal pour moi de me tourner vers des études dans le domaine.<br>L’informatique étant un très large spectre il ma fallu avoir une réflexion sur les élément me plaisant le plus dans l’informatique il s’est avérer que mes domaine favoris sont les réseau et les infrastructure informatique.<br>De plus n’étant pas un fanatique des études je ne souhaite pas aller au-delà de Bac+3.<br>Ainsi il m’a paru tout a fait cohérent de choisir de continuer mes études dans un BUT R&T  "
,"Etude : <br> 2019 – 2022 Bac général mention assez bien <br> 2022-En cours BUT Réseau et Télécommunication <br> Emploi : <br> 2018 Stage Département informatique -Lactalis Deutchland <br> Aout 2022 Temporaire vacance – Usocome Brumath"];
const soustxt_options = ["Qui suis-je","Pourquoi R&T","Historique"];

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