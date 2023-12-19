<script setup>
import axios from 'axios'
import { ref, computed } from 'vue'
import Modal from './components/Modal.vue'

const show = ref(false)
function addExpense() {
  console.log("added an expense")
  show.value = false
}

function close() {
  console.log("expense not added")
  show.value = false
}

</script>
<template>
  <div id="nav">
    <router-link class="nav_links" to="/">Dashboard</router-link> 
    <router-link class="nav_links" to="/calendar">Calendar</router-link>
    <router-link class="nav_links" to="/analysis">Analysis</router-link>
  </div>
  <router-view/>

  <div id="plus_button" @click="show = true">
    +
  </div>
  <div class="modal" v-if="show">
    <Modal @addExpense="addExpense" @close="close"/>
  </div>
</template>

<style>
#nav {
  display: flex;
  justify-content: space-between;
}
.nav_links {
  background: linear-gradient(to right, #ef5350, #f48fb1, #7e57c2, #2196f3, #26c6da, #43a047, #eeff41, #f9a825, #ff5722);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
#plus_button {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: white;
  color: black;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
  font-weight: bold;
  padding-bottom: 5px;
  cursor: pointer;
}
.modal {
  position: fixed;
  left: 50%;
  transform: translate(-50%, 0);
  background-color: white;
  color: black;
  width: 80%;
  height: 50%;
  top: 10%;
  text-align: center;
}
</style> 