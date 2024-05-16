<template>
    <div>
      <div v-if="isLoggedIn">
        <router-link to="/home">Home</router-link>
        <router-link to="/dashboard">Dashboard</router-link>
      </div>
  
      <div class="content">
        <router-view></router-view>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    setup() {
      // Isto é apenas um exemplo, substitua por sua lógica de estado de autenticação
      const isLoggedIn = ref(false); // Você deve substituir isso pela sua lógica de autenticação
  
      return { isLoggedIn };
    }
  }
  </script>
  
  <style>
  .content {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  </style>
  