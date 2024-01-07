<script setup lang="ts">
import router from '../router/index'
import WordDetailCard from "../components/TheWordDetailCard.vue"


</script>

<template>
  <main>
    <div class="wrapper">
      <div class="top">
        <a @click="router.back()" class="back">
          Back
        </a>
      </div>
      <WordDetailCard />
    </div>
  </main>
</template>

<style scoped>
.wrapper {
  max-width: 1280px;
  margin: auto;
  padding-top: 50px;
  padding-bottom: 50px;
}

.top {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  margin-bottom: 0.5rem;
}

.back {
  cursor: pointer;
  color: var(--color-primary)
}
</style>
