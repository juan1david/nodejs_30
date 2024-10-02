<template>
  <div class="consulta-container">
    <h1>Consulta de Clientes</h1>
    <div v-if="data.length > 0" class="table-container">
      <table>
        <thead>
          <tr>
            <th>Documento</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Correo</th>
            <th>Celular</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(cliente, index) in data" :key="index">
            <td>{{ cliente.documento }}</td>
            <td>{{ cliente.nombre }}</td>
            <td>{{ cliente.apellido }}</td>
            <td>{{ cliente.correo }}</td>
            <td>{{ cliente.celular }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else class="no-data">
      <p>No se encontraron datos.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref, onMounted } from 'vue';

export default {
  setup() {
    const data = ref([]);

    const consultaDatosClientes = async () => {
      try {
        const respuesta = await axios.get('http://127.0.0.1:8000/consultaclientes');
        if (Array.isArray(respuesta.data)) {
          data.value = respuesta.data;
        } else {
          console.error('No se cargaron los datos', respuesta.data);
        }
      } catch (error) {
        console.error("Error no hay respuesta", error);
      }
    };

    onMounted(consultaDatosClientes);

    return { data };
  }
}
</script>

<style scoped>
/* Estilo general del contenedor de consulta */
.consulta-container {
  display: flex; /* Usar Flexbox */
  flex-direction: column; /* Organiza los elementos verticalmente */
  align-items: center; /* Centra los elementos horizontalmente */
  justify-content: center; /* Centra los elementos verticalmente */
  height: 100vh; /* Altura completa del viewport */
  max-width: 100%; /* Ajusta el ancho máximo */
  margin: 0 auto; /* Centra el contenedor horizontalmente */
  padding: 20px; /* Ajusta el padding */
  font-family: Arial, sans-serif; /* Fuente de texto */
  text-align: center; /* Centra el texto del contenedor */
}

/* Estilo para el encabezado */
h1 {
  color: #333; /* Color del texto */
  margin-bottom: 20px; /* Espacio debajo del encabezado */
}

/* Estilo para el contenedor de la tabla */
.table-container {
  overflow-x: auto; /* Permite desplazamiento horizontal en pantallas pequeñas */
}

/* Estilo para la tabla */
table {
  width: 100%; /* Ancho completo del contenedor */
  border-collapse: collapse; /* Colapsa bordes de las celdas */
  margin: 0 auto; /* Centra la tabla */
}

/* Estilo para los encabezados de la tabla */
th {
  background-color: #f4f4f4; /* Color de fondo */
  padding: 10px; /* Espaciado interno */
  text-align: left; /* Alineación del texto */
  border-bottom: 1px solid #ddd; /* Línea inferior de la celda */
}

/* Estilo para las celdas de la tabla */
td {
  padding: 10px; /* Espaciado interno */
  border-bottom: 1px solid #ddd; /* Línea inferior de la celda */
}

/* Estilo para el mensaje de sin datos */
.no-data {
  color: #999; /* Color del texto */
  font-size: 18px; /* Tamaño del texto */
}

/* Media Queries para pantallas pequeñas */
@media (max-width: 768px) {
  h1 {
    font-size: 1.5rem; /* Tamaño del texto para pantallas más pequeñas */
  }

  .table-container {
    padding: 0; /* Ajusta el padding para pantallas pequeñas */
  }

  table {
    font-size: 0.9rem; /* Ajusta el tamaño de la fuente de la tabla */
  }

  th, td {
    padding: 8px; /* Ajusta el padding para pantallas pequeñas */
  }

  .no-data {
    font-size: 16px; /* Ajusta el tamaño del texto para pantallas pequeñas */
  }
}

@media (max-width: 480px) {
  h1 {
    font-size: 1.2rem; /* Tamaño del texto para pantallas muy pequeñas */
  }

  .table-container {
    padding: 0; /* Ajusta el padding para pantallas muy pequeñas */
  }

  table {
    font-size: 0.8rem; /* Ajusta el tamaño de la fuente de la tabla */
  }

  th, td {
    padding: 6px; /* Ajusta el padding para pantallas muy pequeñas */
  }

  .no-data {
    font-size: 14px; /* Ajusta el tamaño del texto para pantallas muy pequeñas */
  }
}
</style>
