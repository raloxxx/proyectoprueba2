var marcada = 0;
function asignarNota(valor) {
   marcada = valor;
   desmarcarNotas();
}
function desmarcarNotas() {
   document.getElementById('input1').style.backgroundColor='red';
   
   document.getElementById('input2').style.backgroundColor='yellow';
   document.getElementById('input2').style.color='black';
   
   document.getElementById('input3').style.backgroundColor='green';
   
   marcarNota(marcada);
}
function marcarNota(id) {
   if(id>0)
   {
      document.getElementById("input"+id).style.backgroundColor='#000000';
      document.getElementById("input"+id).style.color='white';
   }
}

function mensaje() {
  var login_name = document.getElementById("login-name")
  alert(login_name.value)
}

var button = document.getElementById("button")
button.addEventListener("click", mensaje)