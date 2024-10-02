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
            const { rol: userRol, mensaje } = response.data;

            Swal.fire({
                icon: 'success',
                title: mensaje,
                text: 'Bienvenido a tu cuenta',
            });

            if (userRol === "cliente") {
                router.push('/cliente');
            } else if (userRol === "empleado") {
                router.push('/empleado');
            } else {
                menError.value = 'Rol no encontrado';
            }
        } catch (error) {
            console.error("Error de inicio de sesión", error);
            menError.value = error.response.data.detail || "Error de inicio de sesión";
            Swal.fire({
                icon: 'error',
                title: 'Error de inicio de sesión',
                text: menError.value,
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
                title: response.data.mensaje,
                text: 'Usuario registrado con éxito',
            });
            cambioForm(); // Switch to login form after registration
        } catch (error) {
            console.error("Error al registrar usuario: ", error);
            menError.value = error.response.data.detail || "Error al registrar usuario";
            Swal.fire({
                icon: 'error',
                title: 'Error en el registro',
                text: menError.value,
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
.aut-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.frminput {
  margin-bottom: 15px;
}

.frminput label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.frminput input,
.frminput select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
  margin: 10px 0;
  width: 100%;
}

button:hover {
  background-color: #0056b3;
}

.error-message {
  color: #dc3545;
  margin-top: 10px;
}
</style>
