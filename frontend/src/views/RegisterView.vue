<template>
  <form @submit.prevent="cadastrar">
    <div class="login-container">
      <div class="login-card">
        <router-link to="/" class="voltar-btn">Voltar</router-link>
        <h1 class="h1">Cadastro</h1>
        <input type="text" placeholder="Email" />
        <input type="text" placeholder="Usuario" />
        <input type="password" placeholder="Password" />
        <button type="submit" class="cadastrar-btn">Cadastrar</button>
      </div>
    </div>
  </form>
  </template>
  
  <script>
  export default {
    name: "LoginView"
  }
  </script>
  
  <style scoped>
  .h1 {
    font-family: 'Times New Roman', Times, serif;
    font-size: 40px;
  }
  
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .login-card {
    background: linear-gradient(145deg, #6a85b6, #bac8e0);
    padding: 80px;
    width: 550px;
    border-radius: 15px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  input {
    font-family: 'Times New Roman', Times, serif;
    width: 100%;
    padding: 12px;
    margin: 15px 0;
    border-radius: 9px;
    border: none;
  }

  .voltar-btn {
    font-family: 'Times New Roman', Times, serif;
    font-size: 15px;
    display: block;
    color: #ffffff;
    text-decoration: none;
    left: 10px; /* Ajuste a posição esquerda */
  }

  button.cadastrar-btn {
    width: 100%;
    padding: 12px;
    background-color: #4a69bd;
    color: white;
    border: none;
    border-radius: 9px;
    cursor: pointer;
    font-family: 'Times New Roman', Times, serif;
    margin-top: 20px;
    font-size: 17px;
  }
  
  </style>
  