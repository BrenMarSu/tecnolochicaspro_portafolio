/*Conexion HTML*/
let app = document.getElementById('typewriter');
 
let typewriter = new Typewriter(app, {
  loop: true,
  delay: 75,
});
 
typewriter
  .pauseFor(2500)
  .typeString('<span style= "color:#8D7C74"> Desarrolladora | Estudiante de Ingeniería en TICs</span>')
  .pauseFor(200)
  .deleteChars(10)
  .start();
 
  let app2 = document.getElementById('typewriter2');

  let typewriter2 = new Typewriter(app2, {
    loop: true,
    delay: 75,
  });
  
  typewriter2
    .pauseFor(2500)
    .typeString('<span style="color:#8D7C74">Developer | ICT Engineer Student</span>')
    .pauseFor(200)
    .deleteChars(10)
    .start();

// Función para mostrar la alerta al recargar la página
function mostrarAlerta() {
  // Obtener parámetros de la URL para verificar si el formulario se ha enviado correctamente
  const urlParams = new URLSearchParams(window.location.search);
  const enviado = urlParams.get('enviado');

  // Mostrar la alerta si el formulario se ha enviado correctamente
  if (enviado === 'true') {
    const alerta = document.getElementById('successAlert');
    alerta.style.display = 'block';

  // Ocultar la alerta después de tres segundos
  setTimeout(function() {
    alerta.style.display = 'none';
  }, 5000);
  }
}

 // Función para cerrar la alerta al hacer clic en el botón de cerrar (x)
 function cerrarAlerta() {
  const alerta = document.getElementById('successAlert');
  alerta.style.display = 'none';
}

function changeLanguage(lang) {
  let url = '';
  if (lang === 'es') {
    url = '/es';
  } else if (lang === 'en') {
    url = '/';
  }
  console.log(lang)
  window.location.href = url;
}

// Llamar a la función mostrarAlerta cuando se cargue la página
window.addEventListener('load', mostrarAlerta);