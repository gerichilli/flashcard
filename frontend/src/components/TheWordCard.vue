<script setup lang="ts">
defineProps({
  text: String,
  isRemembered: Boolean
})
</script>

<template>
  <RouterLink :to="'/kanji/' + text" class="word-card">
    {{ text }}
  </RouterLink>
</template>
<style scoped>
.word-card {
  aspect-ratio: 1;
  border: 2px solid var(--color-border);
  padding: 1rem;
  font-size: 3rem;
  font-weight: 500;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 1rem;
  color: var(--color-text);
  opacity: v-bind("isRemembered ? '0.25' : '1'");

  /* background: var(--color-gradient);
  background-clip: text;
  -webkit-text-fill-color: transparent; */
}

@media (hover: hover) {
  .word-card:hover {
    text-decoration: none;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
    background: var(--color-gradient);
    color: #fff;
  }
}
</style>