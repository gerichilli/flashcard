<script setup lang="ts">
import { RouterLink } from 'vue-router'
import IconWelcome from './icons/IconWelcome.vue'
</script>

<template>
  <div class="wrapper">
    <h1>Our mission is to help you learn a new language in a fun and engaging way. Whether you are a beginner or an
      advanced learner, we have courses that cater to your needs.</h1>
    <div class="image">
      <IconWelcome />
    </div>
    <RouterLink to="/courses" class="button">Explore courses</RouterLink>
  </div>
</template>

<style scoped>
.wrapper {
  max-width: 640px;
  margin: auto;
  padding-top: 50px;
  padding-bottom: 50px;
}

h1 {
  font-size: 1.25rem;
  text-align: center;
}

.image {
  max-width: 500px;
  margin: auto;
}

.button {
  width: 100%;
  max-width: 200px;
  display: block;
  background: var(--color-gradient);
  color: #ffffff;
  padding: 0.875rem 1.25rem;
  font-size: 0.875rem;
  font-weight: 700;
  border-radius: 0.25em;
  margin-top: 1rem;
  margin: 0 auto;
  text-align: center;
}

@media (hover: hover) {
  .button:hover {
    text-decoration: none;
  }
}
</style>