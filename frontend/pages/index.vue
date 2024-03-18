<template>
  <div id="app">
    <header>
      <!-- Main Navbar -->
      <nav class="uk-container uk-navbar">
        <div class="uk-navbar-left">
          <ul class="uk-navbar-nav">
            <li class="uk-active">
              <a href="#">Library<strong>Management</strong></a>
            </li>
          </ul>
        </div>
        <div class="uk-navbar-right">
          <ul class="uk-navbar-nav uk-visible@s">
            <li><a class="uk-text-large" href="/dashboard">Dashboard</a></li>
            <li><a class="uk-text-large" href="/help">Help</a></li>
          </ul>
          <a href="#" class="uk-navbar-toggle uk-hidden@s" uk-navbar-toggle-icon uk-toggle="target: #sidenav"></a>
        </div>
      </nav>
    </header>

    <div id="sidenav" uk-offcanvas="flip: true" class="uk-offcanvas">
      <div class="uk-offcanvas-bar">
        <ul class="uk-nav">
          <li><a class="uk-text-large" href="/dashboard">Dashboard</a></li>
          <li><a class="uk-text-large" href="/help">About</a></li>
        </ul>
      </div>
    </div>

    <div id="student">
      <center>
        Hello Student, <span id="stname">{{ userName }}</span>
        <br>
        <br>
        <div id="booksborrowed">
          <!-- Replace with actual API data -->
          <div v-for="book in borrowedBooks" :key="book.id" class="uk-card uk-card-default uk-width-1-3">
            <div class="uk-card-header">
              <div class="uk-grid-small uk-flex-middle" uk-grid>
                <div class="uk-width-auto">
                  <img class="uk-border-circle" :src="book.avatarUrl" alt="User Avatar">
                </div>
                <div class="uk-width-auto">
                  <h4 class="uk-card-title uk-margin-remove-bottom">Title: {{ book.title }}</h4>
                  <h4 class="uk-card-title uk-margin-remove-bottom">Written By: <span class="author">{{ book.author }}</span></h4>
                  <p class="uk-text-meta uk-margin-remove-top">Date Issued: <time :datetime="book.issueDate">{{ book.issueDate }}</time></p>
                </div>
              </div>
            </div>
            <div class="uk-card-body">
              <p>{{ book.summary }}</p>
            </div>
            <div class="uk-card-footer">
              <span href="#" class="uk-button-text">Due Date: <span class="duedate">{{ book.dueDate }}</span></span>
            </div>
          </div>
        </div>
      </center>
    </div>
  </div>
</template>



<script setup>
import { ref, onMounted } from 'vue';

const isUserLoggedIn = ref(false); // Set this value based on your logic
const userName = ref(getLocalStorageItem('Name') || ''); // Fetch user name from localStorage // Fetch user type from localStorage
const userType = ref(getLocalStorageItem("accType") || "")
const borrowedBooks = ref([
  {
    id: 1,
    avatarUrl: 'https://yt3.ggpht.com/Le5_s8cNZTxGt92yNkf05zgs1nzZg8l2lHs0uHM9p2eIRQJWOg4EXzVDKk_v-PKQ9ikWbU4x=s108-c-k-c0x00ffffff-no-rj',
    title: 'Yeh Jawaani Hain Deewani',
    author: 'Someone',
    issueDate: 'April 01, 2016',
    summary: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
    dueDate: 'April 15, 2016',
  },
  // Add more book objects as needed
]);
onMounted(() => {

  isUserLoggedIn.value = Boolean(userName.value && userType.value);
  if(userType=="teacher" || userType=="Teacher"){
    navigateTo("/teacher")
  }
  if(!userName.value && !userType.value){
    navigateTo("/login")
  }
});

// Helper function to safely get an item from localStorage
function getLocalStorageItem(key) {
  try {
    return localStorage.getItem(key) || '';
  } catch (error) {
    console.error('Error accessing localStorage:', error.message);
    return '';
  }
}
</script>