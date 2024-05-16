<template>
  <form @submit.prevent="login">
    <div class="login-container">
      <div class="login-card">
        <h1 class="h1">Login</h1>
        <input type="text" placeholder="Seu Email" />
        <input type="password" placeholder="Password" />
        <button type="submit" class="login-btn">Login</button>
        <router-link to="/register" class="register-btn">Não tem uma conta? Cadastre-se</router-link>
      </div>
    </div>
  </form>
  </template>
   <script setup>
 
 
 function login() {
  console.log('login')
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
    border-radius: 25px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
   input {
    font-family: 'Times New Roman', Times, serif;
    width: 100%;
    padding: 12px;
    margin: 15px 0;
    border-radius: 14px;
    border: none;
  }
   button.login-btn {
    width: 100%;
    padding: 12px;
    background-color: #4a69bd;
    color: white;
    border: none;
    border-radius: 14px;
    cursor: pointer;
    font-family: 'Times New Roman', Times, serif;
    margin-top: 20px;
    font-size: 17px;
  }
   .register-btn {
    font-family: 'Times New Roman', Times, serif;
    font-size: 20px;
    display: block;
    margin-top: 20px;
    text-decoration: none;
    border: none;
    border-radius: 14px;
    color: rgb(255, 255, 255);
    transition: 0.4s;
    padding: 3px;
  }
   @media (hover: hover) {
    a:hover {
      background-color: hsl(237, 87%, 65%);
    }
  }
  </style>