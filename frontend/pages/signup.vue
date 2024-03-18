<template>
    <div class="uk-section uk-section-muted uk-flex uk-flex-middle uk-animation-fade" uk-height-viewport>
      <div class="uk-width-1-1">
        <div class="uk-container">
          <div class="uk-grid-margin uk-grid uk-grid-stack" uk-grid>
            <div class="uk-width-1-1@m">
              <div class="uk-margin uk-width-large uk-margin-auto uk-card uk-card-default uk-card-body uk-box-shadow-large">
                <h3 class="uk-card-title uk-text-center">Sign up today. It's free!</h3>
                <form @submit.prevent="signup">
                  <div class="uk-margin">
                    <div class="uk-inline uk-width-1-1">
                      <span class="uk-form-icon" uk-icon="icon: user"></span>
                      <input v-model="name" class="uk-input uk-form-large" type="text" placeholder="First and last name">
                    </div>
                  </div>
                  <div class="uk-margin">
                    <div class="uk-inline uk-width-1-1">
                      <span class="uk-form-icon" uk-icon="icon: user"></span>
                      <input v-model="username" class="uk-input uk-form-large" type="text" placeholder="Username">
                    </div>
                  </div>
                  <div class="uk-margin">
                    <div class="uk-inline uk-width-1-1">
                      <span class="uk-form-icon" uk-icon="icon: mail"></span>
                      <input v-model="email" class="uk-input uk-form-large" type="text" placeholder="Email address">
                    </div>
                  </div>
                  <div class="uk-margin">
                    <div class="uk-inline uk-width-1-1">
                      <span class="uk-form-icon" uk-icon="icon: lock"></span>
                      <input v-model="password" class="uk-input uk-form-large" type="password" placeholder="Set a password">	
                    </div>
                  </div>
                  <div class="uk-margin uk-grid-small uk-child-width-auto uk-grid">
                    <label><input v-model="agreeTerms" class="uk-checkbox" type="checkbox"> I agree the Terms and Conditions.</label>
                  </div>
                  <div class="uk-margin">
                    <button class="uk-button uk-button-primary uk-button-large uk-width-1-1">Sign Up</button>
                  </div>
                  <div class="uk-text-small uk-text-center">
                    Already have an account? <a href="./login" uk-switcher-item="1">Log in</a>
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
  const signup = () => {
    // Handle signup logic
    console.log("Sign up button clicked");
  };
  
  let name = '';
  let username = '';
  let email = '';
  let password = '';
  let agreeTerms = false;
  </script>
  
  <style scoped>
  /* Add scoped styles here */
  </style>
  