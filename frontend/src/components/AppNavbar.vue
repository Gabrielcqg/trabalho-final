<template>
  <nav class="app-navbar">
    <div class="navbar-left">
      <div class="logo">CLINICA M </div>
    </div>
    <div class="navbar-center">
      <router-link to="/home">Home</router-link>
      <router-link to="/Pacientes">Pacientes</router-link>
      <router-link to="/Medicos">Medicos</router-link>
      <router-link to="/informacoes">Informacoes</router-link>
      <router-link to="/contact">Contact</router-link>
    </div>
    <div class="navbar-right">
      <img src="@/assets/user-icon.png" alt="User Icon" class="user-icon">
      <div class="usuario"><h1>usuario x</h1></div>
    </div>
  </nav>
</template>


<script>
export default {
  name: 'AppNavbar',
  data() {
    return {
      userName: 'Usuário', // O nome deve ser dinâmico conforme o login
    };
  }
}
</script>

<style>
#app {
  max-width: 100%; 
  margin: 0 auto;
  padding: 0; 
}

body {
  display: block; 
}

.app-navbar {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f8f9fa;
  padding: 10px 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  position: absolute;
  top: 0;
  left: 0;
}

.logo{
  font-size: 27px;
  margin-left: 16px;
}
.navbar-left, .navbar-center, .navbar-right {
  display: flex;
  align-items: center;
}

.navbar-center {
  gap: 95px;
}

.user-icon {
  width: 40px;
  margin-right: 15px;
}
.usuario{
  margin-right: 16px  
}

.router-link-active, .navbar-center a {
  text-decoration: none;
  color: #2c3e50; /* Cor escura similar à imagem */
  font-weight: 500;
}

.navbar-center a:hover {
  color: #007bff; /* Cor azul para hover */
}

</style>
