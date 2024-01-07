<script setup lang="ts">
import router from '@/router';
import { useUserStore } from '@/stores/user';
import FormInput from './TheFormInput.vue'

const userInfo = {
  username: '',
  password: '',
  rePassword: ''
}

const userStore = useUserStore();

function updateUserInput(key: keyof typeof userInfo, value: string) {
  userInfo[key] = value;
}


function handleSubmit() {
  if (!userInfo.password || !userInfo.username || !userInfo.rePassword) {
    alert('Please input all required fields')
  }

  userStore.register(
    userInfo.username,
    userInfo.password
  )

  if (userStore.isLogin) {
    router.push("/")
  }
}
</script>

<template>
  <form @submit.prevent="handleSubmit">
    <h2>Register</h2>
    <FormInput name="username" label="Username" type="text" required
      @update-value="(input) => updateUserInput('username', input.value)" />
    <FormInput name="password" label="Password" type="password" required
      @update-value="(input) => updateUserInput('password', input.value)" />
    <FormInput name="re-password" label="Confirm password" type="password" required
      @update-value="(input) => updateUserInput('rePassword', input.value)" />
    <button type="submit" class="submit">Submit</button>
  </form>
</template>
<style scoped>
form {
  max-width: 300px;
  margin: 50px auto;
}

h2 {
  font-size: 2rem;
  text-align: center;
  color: var(--color-heading);
  margin-bottom: 1rem;
}

.submit {
  border: none;
  background: var(--color-gradient);
  color: #ffffff;
  padding: 0.875rem 0.875rem;
  cursor: pointer;
  width: 100%;
  font: inherit;
  font-size: 0.875rem;
  font-weight: 700;
  border-radius: 0.25em;
  margin-top: 1rem;
}

.required {
  color: red;
}
</style>