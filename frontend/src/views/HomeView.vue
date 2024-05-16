<template>
  <div>
    <app-navbar></app-navbar>
    <div class="outer-content-container">
      <div class="card">
        <div class="icon-section">
          <img src="@/assets/calendar_check_icon_136844.png" alt="Check Icon">
        </div>
        <div class="text-section">
          <div class="number">{{ totalConsultations }}</div>
          <div class="text">Total de consultas realizadas pela clínica (No mês)</div>
        </div>
      </div>
      <div class="card2">
        <div class="icon-section">
          <img src="@/assets/calendar_check_icon_136844.png" alt="Check Icon">
        </div>
        <div class="text-section">
          <div class="number">{{ totalConsultations }}</div>
          <div class="text">Total de pacientes únicos que ja estao marcados</div>
        </div>
      </div>
      <div class="button-group">
        <button @click="showNewDoctorForm">Cadastrar novo médico</button>
        <button @click="showNewPatientForm">Cadastrar novo paciente</button>
        <button @click="showScheduleAppointmentForm">Agendar consulta</button>
      </div>
      <div v-if="showAppointmentForm">
        <h2>Agendar consulta</h2>
        <form @submit.prevent="scheduleAppointment">
          <label for="patient">Paciente:</label>
          <select id="patient" v-model="selectedPatient">
            <option v-for="patient in patients" :key="patient.id" :value="patient.id">
              {{ patient.name }}
            </option>
          </select>
         
          <label for="doctor">Médico:</label>
          <select id="doctor" v-model="selectedDoctor">
            <option v-for="doctor in doctors" :key="doctor.id" :value="doctor.id">
              {{ doctor.name }}
            </option>
          </select>
 
 
          <label for="date">Data da consulta:</label>
          <input type="date" id="date" v-model="appointmentDate">
 
 
          <label for="time">Hora da consulta:</label>
          <input type="time" id="time" v-model="appointmentTime">
 
 
          <button type="submit">Agendar</button>
        </form>
      </div>
      <div v-if="showDoctorForm">
        <h2>Cadastrar novo médico</h2>
        <form @submit.prevent="registerDoctor">
          <label for="doctorName">Nome do médico:</label>
          <input id="doctorName" v-model="newDoctor.name" type="text" required>
 
 
          <label for="crm">CRM:</label>
          <input id="crm" v-model="newDoctor.crm" type="text" required>
 
 
          <label for="crmUf">CRM-UF:</label>
          <select id="crmUf" v-model="newDoctor.crmUf" required>
            <option value="SP">SP</option>
            <option value="MG">MG</option>
            <option value="RJ">RJ</option>
          </select>
 
 
          <button type="submit">Cadastrar</button>
        </form>
      </div>
      <div v-if="showPatientForm">
        <h2>Cadastrar novo paciente</h2>
        <form @submit.prevent="registerPatient">
          <label for="patientName">Nome:</label>
          <input id="patientName" v-model="newPatient.name" type="text" required>
 
 
          <label for="patientCPF">CPF:</label>
          <input id="patientCPF" v-model="newPatient.cpf" type="text" required>
 
 
          <label for="patientDOB">Data de Nascimento:</label>
          <input id="patientDOB" v-model="newPatient.dob" type="date" required>
 
 
          <button type="submit">Cadastrar</button>
        </form>
 </div>
    </div>
  </div>
 </template>
 
 
 
 
 <script>
 import AppNavbar from '@/components/AppNavbar.vue';
 
 
 export default {
  name: 'HomeView',
  components: {
    AppNavbar
  },
  data() {
    return {
      totalConsultations: 7,
      showAppointmentForm: false,
      showDoctorForm: false,
      patients: [],  // This should be fetched from your database
      doctors: [],   // This should be fetched from your database
      selectedPatient: '',
      selectedDoctor: '',
      appointmentDate: '',
      appointmentTime: '',
      showPatientForm: false,
      newDoctor: {  // Ensure this is defined to prevent undefined errors
        name: '',
        crm: '',
        crmUf: '',
      },
      newPatient: {
      name: '',
      cpf: '',
      dob: ''
    }
    };
  },
  methods: {
  showScheduleAppointmentForm() {
    this.showAppointmentForm = true;
    this.showDoctorForm = false;
    this.showPatientForm = false; // Add this line to hide the patient form
    this.fetchPatients();
    this.fetchDoctors();
  },
  showNewDoctorForm() {
    this.showDoctorForm = true;
    this.showAppointmentForm = false;
    this.showPatientForm = false; // Add this line to hide the patient form
    console.log("showNewDoctorForm method called");
  },
  showNewPatientForm() {
    this.showPatientForm = true;
    this.showDoctorForm = false;
    this.showAppointmentForm = false; // Add this line to hide the appointment form
    console.log("showNewPatientForm method called");
  },
  registerDoctor() {
    // Submit the new doctor data to your API
    console.log('Registering new doctor:', this.newDoctor);
    alert('Médico cadastrado com sucesso!');
  },
  registerPatient() {
    // Submit the new patient data to your API
    console.log('Registering new patient:', this.newPatient);
    alert('Paciente cadastrado com sucesso!');
  }
 }
 }
 </script>
 
 
 <style scoped>
 .outer-content-container {
  display: flex;
  flex-direction: row; /* Changes the flex-direction to horizontal */
  align-items: flex-start; /* Keeps children aligned at the top */
  justify-content: flex-start; /* Aligns children to the left side */
  flex-wrap: wrap; /* Allows wrapping if space is not enough */
  width: 90vw; /* Ensure it takes full width if needed */
  height: 100vh;
  background-color: rgba(255, 255, 255, 0.9);
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 60px;
  padding: 2vw; /* Adds padding inside the container */
 }
 
 
 .card, .card2 {
  display: flex;
  width: 25vw; /* Adjust width as needed or keep it auto */
  height: 12.5vw; /* Adjust height as needed */
  border-radius: 10px;
  overflow: hidden;
  border: 2px solid black;
  margin-left: 2vw;
  margin-right: 2vw; /* Space between cards */
  margin-top: 4vw;
 }
 
 
 .icon-section {
  background-color: #5C6BC0; /* Purple background */
  padding: 20px;
  width: 10vw; /* Adjust width as needed */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
 }
 
 
 .icon-section img {
  width: 8vw;
 }
 
 
 .icon-section .number {
  color: white;
  font-size: 24px;
  font-weight: bold;
  margin-top: 10px;
 }
 
 
 .text-section {
  font-size: 4vw;
  background-color: rgb(255, 255, 255); /* White background */
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding-left: 10px;
 }
 
 
 .text-section .text {
  font-size: 0.9vw; /* Adjust font size as needed */
  padding-bottom: 0.7vw;
 }
 
 
 
 
 .button-group {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  margin-top: 5.4vw;
  margin-left: 4vw;
 }
 
 
 .button-group button {
  padding: 10px 20px;
  margin-bottom: 10px;
  background-color: #4A47A3;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 20vw; /* Ajuste conforme necessário */
 }
 
 
 .button-group button:hover {
  background-color: #3734A9;
 }
 
 
 form {
  display: flex;
  flex-direction: column;
  width: 87vw;
 }
 form label, form select, form input {
  margin-bottom: 0.5em;
  height: 2.3vw;
 
 
 }
 form button {
  padding: 10px;
  background-color: #4A47A3;
  color: white;
  border-radius: 5px;
  cursor: pointer;
 }
 form button:hover {
  background-color: #3734A9;
 }
 </style>
 
 
 