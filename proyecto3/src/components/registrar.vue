<template>
  <div class="container">
    <h1 class="title">Registrar Cliente</h1>
    <form @submit.prevent="insertarCliente" class="form">
      <div class="form-group">
        <label for="documento">Documento</label>
        <input v-model="cliente.documento" id="documento" type="text" required class="form-control" />
      </div>
      <div class="form-group">
        <label for="nombre">Nombre</label>
        <input v-model="cliente.nombre" id="nombre" type="text" required class="form-control" />
      </div>
      <div class="form-group">
        <label for="apellido">Apellido</label>
        <input v-model="cliente.apellido" id="apellido" type="text" required class="form-control" />
      </div>
      <div class="form-group">
        <label for="correo">Correo</label>
        <input v-model="cliente.correo" id="correo" type="email" required class="form-control" />
      </div>
      <div class="form-group">
        <label for="celular">Celular</label>
        <input v-model="cliente.celular" id="celular" type="text" required class="form-control" />
      </div>
      <button type="submit" class="submit-button">Registrar</button>
    </form>
    <div v-if="message" :class="messageClass">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';

export default {
  setup() {
    const cliente = ref({
      documento: "",
      nombre: "",
      apellido: "",
      correo: "",
      celular: ""
    });

    const message = ref('');
    const messageClass = ref('');

    const insertarCliente = async () => {
      try {
        const respuesta = await axios.post('http://127.0.0.1:8000/insertar', cliente.value);

        if (respuesta.status === 200) {
          message.value = 'Registrado exitosamente';
          messageClass.value = 'message-success';
          cliente.value = { documento: "", nombre: "", apellido: "", correo: "", celular: "" };
        } else {
          message.value = 'No se pudo registrar';
          messageClass.value = 'message-error';
        }
      } catch (error) {
        message.value = 'Error al registrar datos';
        messageClass.value = 'message-error';
      }
    };

    return { cliente, insertarCliente, message, messageClass };
  }
};
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  width: 149%;
  padding: 20px;
  font-family: Arial, sans-serif;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Responsive styles */
@media (max-width: 768px) {
  .container {
    padding: 10px;
    width: 90%;
  }

  .title {
    font-size: 24px;
  }
}

.title {
  text-align: center;
  margin-bottom: 20px;
  color: #333;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.submit-button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px 15px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.submit-button:hover {
  background-color: #0056b3;
}

.message-success,
.message-warning,
.message-error {
  margin-top: 10px;
}

.message-success {
  color: #28a745;
}

.message-warning {
  color: #ffc107;
}

.message-error {
  color: #dc3545;
}
</style>
