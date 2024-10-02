<template>
  <header>
    <nav>
      <div class="container">
        <div class="logo">
          <a href="#"><img src="./icons/PROCES SCHOOL.png" alt="Logo de la aplicación"></a>
        </div>
        <div class="title">
          <h1>PROCESSCHOOL</h1>
        </div>
        <div class="menu-toggle" @click="toggleMenu">
          <span class="bar"></span>
          <span class="bar"></span>
          <span class="bar"></span>
        </div>
        <ul :class="{ 'show': menuOpen }">
          <li><router-link to="/Home">Home</router-link></li>
          <li><router-link to="/">Consultar</router-link></li>
          <li><router-link to="/Registrar">Registrar</router-link></li>
          <li><router-link to="/login">Login</router-link></li>
          <li><router-link to="/Docente">Docente</router-link></li>
          <li><router-link to="/Estudiante">Estudiante</router-link></li>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from 'vue';

const menuOpen = ref(false);

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value;
};
</script>

<style scoped>
/* Estilo para el encabezado */
header {
  background-color: #007bff; /* Color de fondo azul */
  color: #fff; /* Color del texto blanco */
  padding: 10px 20px; /* Padding alrededor del contenido */
  position: relative; /* Posicionamiento relativo para el menú desplegable */
}

/* Estilo para el contenedor del encabezado */
.container {
  display: flex; /* Usa Flexbox para el diseño */
  justify-content: space-between; /* Espacio entre el logo, título y menú */
  align-items: center; /* Centra verticalmente los elementos */
}

/* Estilo para el logo */
.logo a {
  color: #fff; /* Color del texto blanco para el logo */
  text-decoration: none; /* Elimina el subrayado del enlace */
}

/* Estilo para la imagen del logo */
.logo img {
  height: 50px; /* Ajusta la altura de la imagen del logo */
}

/* Estilo para el título */
.title h1 {
  margin: 0; /* Elimina el margen por defecto */
  font-size: 1.5rem; /* Tamaño de fuente para el título */
}

/* Estilo para el botón de alternancia del menú */
.menu-toggle {
  display: none; /* Oculta el botón por defecto en pantallas grandes */
  flex-direction: column; /* Organiza las barras verticalmente */
  cursor: pointer; /* Cursor tipo puntero al pasar sobre el botón */
}

.menu-toggle .bar {
  background-color: #fff; /* Color de las barras blancas */
  height: 3px; /* Altura de las barras */
  width: 25px; /* Ancho de las barras */
  margin: 3px 0; /* Espacio entre las barras */
  transition: 0.3s; /* Transición suave al cambiar */
}

/* Estilo para la lista de navegación */
nav ul {
  list-style: none; /* Elimina los puntos de la lista */
  margin: 0; /* Elimina el margen por defecto */
  padding: 0; /* Elimina el padding por defecto */
  display: flex; /* Usa Flexbox para el diseño horizontal */
  align-items: center; /* Alinea verticalmente los elementos */
}

nav ul li {
  margin-left: 20px; /* Espacio entre los elementos de navegación */
}

nav ul li a {
  color: #fff; /* Color del texto blanco para los enlaces */
  text-decoration: none; /* Elimina el subrayado de los enlaces */
  font-size: 1rem; /* Tamaño de fuente para los enlaces */
  transition: color 0.3s; /* Transición suave del color de los enlaces */
}

nav ul li a:hover {
  color: #e0e0e0; /* Color gris claro al pasar el cursor */
}

/* Estilo adaptativo para pantallas pequeñas */
@media (max-width: 768px) {
  .menu-toggle {
    display: flex; /* Muestra el botón de alternancia en pantallas pequeñas */
  }

  nav ul {
    display: none; /* Oculta el menú por defecto en pantallas pequeñas */
    flex-direction: column; /* Organiza el menú verticalmente */
    width: 100%; /* Ancho completo del menú */
    position: absolute; /* Posiciona el menú en relación al encabezado */
    top: 60px; /* Espacio desde la parte superior del encabezado */
    right: 0; /* Alinea el menú al borde derecho */
    background-color: #007bff; /* Color de fondo azul del menú desplegable */
    border-radius: 5px; /* Bordes redondeados */
    padding: 10px 0; /* Padding dentro del menú desplegable */
    z-index: 10; /* Asegura que el menú esté sobre otros elementos */
  }

  nav ul.show {
    display: flex; /* Muestra el menú cuando está abierto */
  }

  nav ul li {
    margin: 10px 0; /* Espacio entre los elementos de navegación en el menú desplegable */
    text-align: center; /* Centra el texto en el menú desplegable */
  }
}

@media (max-width: 480px) {
  .title h1 {
    font-size: 1.2rem; /* Tamaño de fuente más pequeño para pantallas muy pequeñas */
  }

  .logo img {
    height: 40px; /* Ajusta la altura de la imagen del logo para pantallas pequeñas */
  }

  nav ul li a {
    font-size: 0.9rem; /* Tamaño de fuente más pequeño para enlaces en pantallas pequeñas */
  }
}
</style>
