<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { useUserStore } from '../stores/user'

const user = useUserStore();
</script>

<template>
  <header>
    <div class="wrapper">
      <RouterLink to="/" class="logo">
        <span>K</span>
        <span>A</span>
        <span>N</span>
        <span>J</span>
        <span>I</span>
      </RouterLink>
      <nav>
        <RouterLink to="/courses">Courses</RouterLink>
        <RouterLink to="/login" v-if="!user.isLogin">Login</RouterLink>
        <RouterLink to="/register" v-if="!user.isLogin">Register</RouterLink>
        <p v-if="user.isLogin">Hello {{ user.username }} 💜</p>
      </nav>
    </div>
  </header>
</template>

<style scoped>
header {
  padding: 1.25rem 2rem;
  border-bottom: 2px solid var(--color-border);
}

.wrapper {
  display: flex;
  align-items: center;
  max-width: 1280px;
  margin: auto;
}

.logo {
  margin-right: auto;
  display: flex;
  gap: 4px;
}

.logo span {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  font-weight: 700;
  font-size: 0.875rem;
  color: #fff;
  background: var(--color-gradient);
  border-radius: 50%;
}

nav {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

nav>a {
  font-weight: 500;
  color: var(--color-primary);
}

@media (hover: hover) {
  .logo:hover {
    text-decoration: none;
  }
}
</style>