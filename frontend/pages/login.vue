<template>
  <div class="uk-section uk-section-muted uk-flex uk-flex-middle uk-animation-fade" uk-height-viewport>
    <div class="uk-width-1-1">
      <div class="uk-container">
        <div class="uk-grid-margin uk-grid uk-grid-stack" uk-grid>
          <div class="uk-width-1-1@m">
            <div class="uk-margin uk-width-large uk-margin-auto uk-card uk-card-default uk-card-body uk-box-shadow-large">
              <h3 class="uk-card-title uk-text-center">Welcome back!</h3>
              <form @submit.prevent="login">
                <div class="uk-margin">
                  <div class="uk-inline uk-width-1-1">
                    <span class="uk-form-icon" uk-icon="icon: mail"></span>
                    <input v-model="email" class="uk-input uk-form-large" type="text" placeholder="Email">
                  </div>
                  <div v-if="!isEmailValid" class="uk-alert-danger uk-margin-small" uk-alert>
                    <p>Please enter a valid email address.</p>
                  </div>
                </div>
                <div class="uk-margin">
                  <div class="uk-inline uk-width-1-1">
                    <span class="uk-form-icon" uk-icon="icon: lock"></span>
                    <input v-model="password" class="uk-input uk-form-large" type="password" placeholder="Password">
                  </div>
                  <div v-if="!isPasswordValid" class="uk-alert-danger uk-margin-small" uk-alert>
                    <p>Password must be 8-16 characters long.</p>
                  </div>
                </div>
                <div class="uk-margin">
                  <button class="uk-button uk-button-primary uk-button-large uk-width-1-1" type="submit">Login</button>
                </div>
                <div class="uk-text-small uk-text-center">
                  Not registered? <a href="/signup">Create an account</a>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const { VITE_LOGIN_API_URL } = useRuntimeConfig();

const email = ref('');
const password = ref('');
const isEmailValid = ref(true);
const isPasswordValid = ref(true);

const login = async () => {
  isEmailValid.value = validateEmail(email.value);
  isPasswordValid.value = validatePassword(password.value);

  if (!isEmailValid.value || !isPasswordValid.value) return;

  // You can now perform your API call using $fetch
  try {
    const response = await fetch(VITE_LOGIN_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email.value,
        password: password.value,
      }),
    });

    if (response.ok) {
      // Handle successful login
      console.log('Login successful');
    } else {
      // Handle login failure
      console.error('Login failed');
    }
  } catch (error) {
    console.error('Error occurred while logging in:', error);
  }
};

const validateEmail = (email) => {
  // Regular expression for email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const validatePassword = (password) => {
  // Check if password length is between 8 and 16 characters
  return password.length >= 8 && password.length <= 16;
};
</script>

<style>
/* Add any custom styles here */
</style>
