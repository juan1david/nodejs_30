<template>
    <div class="aut-container">
        <form @submit.prevent="loginUsuario">
            <div class="frminput" v-if="!frmlogin">
                <label for="documento">Documento</label>
                <select v-model="documento" id="documento">
                    <option value="">Seleccionar documento</option>
                    <option v-for="doc in documentos" :key="doc" :value="doc">
                        {{ doc }}
                    </option>
                </select>
            </div>

            <div class="frminput">
                <label for="nombreUsuario">Nombre Usuario</label>
                <input type="text" id="nombreUsuario" v-model="nombreUsuario" required />
            </div>

            <div class="frminput">
                <label for="Password">Password</label>
                <input type="password" id="Password" v-model="password" required />
            </div>

            <div class="frminput" v-if="!frmlogin">
                <label for="rol">Rol</label>
                <input type="text" id="rol" v-model="rol" required />
            </div>

            <button type="submit">{{ frmlogin ? 'Iniciar Sesión' : 'Registrarse' }}</button>
            <div v-if="menError" class="error-message">{{ menError }}</div>
            <button type="button" @click="cambioForm">{{ frmlogin ? 'Crear Cuenta' : 'Iniciar Sesión' }}</button>
        </form>
    </div>
</template>

<script setup>
import Swal from 'sweetalert2';
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const nombreUsuario = ref('');
const password = ref('');
const rol = ref('');
const documento = ref('');
const documentos = ref([]);
const frmlogin = ref(true);
const menError = ref('');
const router = useRouter();

const cambioForm = async () => {
    frmlogin.value = !frmlogin.value;
    if (!frmlogin.value) {
        try {
            const response = await axios.get('http://127.0.0.1:8000/clientes/documento/');
            documentos.value = response.data;
        } catch (error) {
            console.error("Error en la consulta de documentos: ", error);
            menError.value = "Error al consultar documentos";
        }
    }
};

const loginUsuario = async () => {
    if (frmlogin.value) {
        try {
            const response = await axios.post('http://127.0.0.1:8000/login', {
                nombre_usuario: nombreUsuario.value,
                password: password.value,
            });
            const { rol: userRol } = response.data;

            if (userRol === "cliente") {
                router.push('/cliente');
            } else if (userRol === "empleado") {
                router.push('/empleado');
            } else {
                menError.value = 'Rol no encontrado';
            }

            Swal.fire({
                icon: 'success',
                title: 'Inicio de sesión exitoso',
                text: 'Bienvenido a tu cuenta',
            });
        } catch (error) {
            console.error("Error de inicio de sesión", error);
            menError.value = "Error de inicio de sesión";
            Swal.fire({
                icon: 'error',
                title: 'Error de inicio de sesión',
                text: 'Error al iniciar sesión',
            });
        }
    } else {
        try {
            const response = await axios.post('http://127.0.0.1:8000/registrousuario', {
                nombre_usuario: nombreUsuario.value,
                password: password.value,
                rol: rol.value,
                documento: documento.value,
            });
            Swal.fire({
                icon: 'success',
                title: 'Usuario Registrado',
                text: 'Usuario registrado con éxito',
            });
        } catch (error) {
            console.error("Error al registrar usuario: ", error);
            menError.value = "Error al registrar usuario";
            Swal.fire({
                icon: 'error',
                title: 'Error en el registro',
                text: 'Hubo un problema al registrar el usuario',
            });
        }
    }
};

onMounted(async () => {
    if (!frmlogin.value) {
        try {
            const response = await axios.get('http://127.0.0.1:8000/clientes/documento/');
            documentos.value = response.data;
        } catch (error) {
            console.error("Error en la consulta de documentos: ", error);
            menError.value = "Error al consultar documentos";
        }
    }
});
</script>

<style scoped>
/* Contenedor principal del formulario de autenticación y registro */
.aut-container {
  max-width: 600px; /* Ancho máximo del contenedor en pantallas grandes */
  margin: 0 auto; /* Centra el contenedor horizontalmente */
  padding: 20px; /* Espaciado interno */
  font-family: Arial, sans-serif; /* Fuente de texto */
  background-color: #fff; /* Color de fondo */
  border-radius: 8px; /* Bordes redondeados */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Sombra del contenedor */
}

/* Estilo para los inputs del formulario */
.frminput {
  margin-bottom: 15px; /* Espacio entre los inputs */
}

/* Estilo para las etiquetas de los inputs */
.frminput label {
  display: block; /* Muestra las etiquetas en bloque */
  margin-bottom: 5px; /* Espacio debajo de la etiqueta */
  font-weight: bold; /* Fuente en negrita */
}

/* Estilo para los campos de entrada del formulario */
.frminput input,
.frminput select {
  width: 100%; /* Ancho completo del contenedor */
  padding: 10px; /* Espaciado interno */
  border: 1px solid #ddd; /* Borde de la caja */
  border-radius: 4px; /* Bordes redondeados */
  box-sizing: border-box; /* Incluye el padding y el borde en el ancho total */
}

/* Estilo para el botón del formulario */
button {
  background-color: #007bff; /* Color de fondo del botón */
  color: #fff; /* Color del texto */
  border: none; /* Sin borde */
  padding: 10px 15px; /* Espaciado interno */
  border-radius: 4px; /* Bordes redondeados */
  cursor: pointer; /* Cursor en forma de mano */
  font-size: 16px; /* Tamaño del texto */
  transition: background-color 0.3s; /* Transición suave para el cambio de color */
  margin: 10px 0; /* Margen alrededor del botón */
  width: 100%; /* Ancho completo del contenedor */
}

/* Estilo para el botón en estado hover */
button:hover {
  background-color: #0056b3; /* Color de fondo en hover */
}

/* Estilo para el mensaje de error */
.error-message {
  color: #dc3545; /* Color de texto de error */
  margin-top: 10px; /* Espacio encima del mensaje */
}

/* Estilo para el mensaje de éxito */
.message-success {
  color: #28a745; /* Color de texto de éxito */
  margin-top: 10px; /* Espacio encima del mensaje */
}

/* Estilo para el mensaje de advertencia */
.message-warning {
  color: #ffc107; /* Color de texto de advertencia */
  margin-top: 10px; /* Espacio encima del mensaje */
}

/* Estilo para el mensaje de error general */
.message-error {
  color: #dc3545; /* Color de texto de error */
  margin-top: 10px; /* Espacio encima del mensaje */
}

/* Media queries para pantallas pequeñas */
@media (max-width: 600px) {
  .aut-container {
    padding: 15px; /* Reducir espaciado interno en pantallas pequeñas */
  }

  button {
    padding: 10px; /* Ajustar espaciado interno del botón */
    font-size: 14px; /* Tamaño del texto en el botón */
  }
}
</style>
