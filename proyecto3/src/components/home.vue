<template>
  <div class="home-container">
    <!-- Título de bienvenida -->
    <h1 class="home-title">WELCOME TO PROCESSCHOOL</h1>

    <!-- Descripción -->
    <p class="home-description">
      Descubre nuestras características únicas y explora todas las posibilidades que ofrecemos para el proceso educativo. ¡Estamos encantados de tenerte aquí!
    </p>

    <!-- Botón de inicio -->
    <button class="home-button">Comenzar</button>

    <!-- Sección de características -->
    <div class="features">
      <div class="feature-item">
        <h2>Clases Interactivas</h2>
        <p>Ofrecemos clases interactivas que hacen el aprendizaje más dinámico y atractivo.</p>
      </div>
      <div class="feature-item">
        <h2>Soporte Personalizado</h2>
        <p>Recibe soporte personalizado de nuestros expertos para resolver cualquier duda.</p>
      </div>
      <div class="feature-item">
        <h2>Materiales de Estudio</h2>
        <p>Accede a una amplia gama de materiales de estudio actualizados y relevantes.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Elimina el código relacionado con el carrusel de imágenes
</script>

<style scoped>
/* Estilo para el contenedor principal */
.home-container {
  display: flex; /* Usa Flexbox para centrar el contenido */
  flex-direction: column; /* Organiza los elementos verticalmente */
  align-items: center; /* Centra los elementos horizontalmente */
  justify-content: center; /* Centra los elementos verticalmente */
  height: 160vh; /* Altura completa del viewport */
  text-align: center; /* Centra el texto */
  padding: 20px; /* Añade padding alrededor del contenido */
  background-color: rgba(244, 244, 244, 0.8); /* Color de fondo claro con opacidad */
  background-image: url('./icons/images.jpeg'); /* Imagen de fondo */
  background-size: cover; /* Asegura que la imagen cubra todo el contenedor */
  background-position: center; /* Centra la imagen de fondo */
  font-family: 'Arial', sans-serif; /* Fuente moderna y profesional */
  color: #000000; /* Color del texto blanco para contraste con la imagen de fondo */
}

/* Estilo para el título */
.home-title {
  font-size: 2.5rem; /* Tamaño de fuente grande para el título */
  color: #070707; /* Color blanco para el título */
  margin-bottom: 15px; /* Espacio debajo del título */
  font-weight: bold; /* Fuente en negrita */
}

/* Estilo para la descripción */
.home-description {
  font-size: 1rem; /* Tamaño de fuente más pequeño para la descripción en pantallas pequeñas */
  color: #0a0a0a; /* Color blanco para la descripción */
  margin-bottom: 25px; /* Espacio debajo de la descripción */
  max-width: 90%; /* Ancho máximo de la descripción con padding para pantallas pequeñas */
  line-height: 1.6; /* Espaciado de línea para mejor legibilidad */
}

/* Estilo para el botón */
.home-button {
  background-color: #007bff; /* Color de fondo azul */
  color: #000000; /* Color del texto blanco */
  border: none; /* Sin borde */
  border-radius: 5px; /* Bordes redondeados */
  padding: 12px 25px; /* Padding dentro del botón */
  font-size: 1rem; /* Tamaño de fuente para el texto del botón */
  cursor: pointer; /* Cursor tipo puntero al pasar sobre el botón */
  transition: background-color 0.3s, transform 0.2s; /* Transiciones suaves del color de fondo y escalado */
}

.home-button:hover {
  background-color: #0056b3; /* Azul más oscuro al pasar el cursor */
  transform: scale(1.05); /* Aumenta ligeramente el tamaño del botón */
}

/* Estilo para la sección de características */
.features {
  display: flex; /* Usa Flexbox para el diseño de las características */
  flex-wrap: wrap; /* Envuelve los elementos si es necesario */
  justify-content: center; /* Centra los elementos horizontalmente */
  margin-top: 40px; /* Espacio arriba de la sección de características */
}

.feature-item {
  background-color: #414141; /* Color de fondo blanco para los elementos de características */
  border: 1px solid #181515; /* Borde gris claro */
  border-radius: 8px; /* Bordes redondeados */
  padding: 20px; /* Padding dentro de cada elemento */
  margin: 10px; /* Espacio alrededor de cada elemento */
  width: 280px; /* Ancho fijo para cada elemento */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Sombra sutil para los elementos de características */
  transition: transform 0.3s; /* Transición suave para el escalado */
}

.feature-item:hover {
  transform: translateY(-5px); /* Eleva ligeramente el elemento al pasar el cursor */
}

.feature-item h2 {
  font-size: 1.4rem; /* Tamaño de fuente para los encabezados de características */
  color: #007bff; /* Color de texto azul para los encabezados */
  margin-bottom: 10px; /* Espacio debajo del encabezado */
  font-weight: bold; /* Fuente en negrita */
}

.feature-item p {
  font-size: 0.9rem; /* Tamaño de fuente para el texto de características */
  color: #000000; /* Color gris oscuro para el texto */
  line-height: 1.5; /* Espaciado de línea para mejor legibilidad */
}

/* Estilos adaptativos para pantallas pequeñas */
@media (max-width: 768px) {
  .home-title {
    font-size: 2rem; /* Tamaño de fuente del título en pantallas medianas */
  }

  .home-description {
    font-size: 0.9rem; /* Tamaño de fuente para la descripción en pantallas medianas */
    max-width: 95%; /* Ancho máximo de la descripción */
  }

  .home-button {
    font-size: 0.9rem; /* Tamaño de fuente del botón en pantallas medianas */
    padding: 10px 20px; /* Ajusta el padding del botón */
  }

  .features {
    flex-direction: column; /* Organiza los elementos verticalmente en pantallas pequeñas */
  }

  .feature-item {
    width: 90%; /* Ancho más flexible para cada elemento */
    margin: 10px 0; /* Espacio alrededor de cada elemento en pantallas pequeñas */
  }
}

@media (max-width: 480px) {
  .home-title {
    font-size: 1.5rem; /* Tamaño de fuente del título en pantallas pequeñas */
  }

  .home-description {
    font-size: 0.8rem; /* Tamaño de fuente para la descripción en pantallas pequeñas */
  }

  .home-button {
    font-size: 0.8rem; /* Tamaño de fuente del botón en pantallas pequeñas */
    padding: 8px 15px; /* Ajusta el padding del botón */
  }

  .feature-item h2 {
    font-size: 1.2rem; /* Tamaño de fuente para los encabezados de características en pantallas pequeñas */
  }

  .feature-item p {
    font-size: 0.8rem; /* Tamaño de fuente para el texto de características en pantallas pequeñas */
  }
}
</style>
