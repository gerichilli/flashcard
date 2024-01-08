<script setup lang="ts">
defineProps({
  kanji: String,
  kun_reading: String,
  meanings: String,
  on_reading: String,
  stroke_count: Number,
})
</script>

<template>
  <div class="card">
    <h2 class="kanji">{{ kanji }}</h2>
    <div class="info">
      <div class="line">
        <p class="label">Meanings: </p>
        <p class="content">{{ meanings }}</p>
      </div>
      <div class="line">
        <p class="label">On Readings: </p>
        <p class="content">{{ on_reading }}</p>
      </div>
      <div class="line">
        <p class="label">Kun Readings: </p>
        <p class="content">{{ kun_reading }}</p>
      </div>
      <div class="line">
        <p class="label">Stroke Count: </p>
        <p class="content">{{ stroke_count }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  padding: 3rem 2rem;
  border-radius: 0.375rem;
  color: var(--color-text);
  display: flex;
  gap: 2rem;
  margin-bottom: 48px;
  box-shadow: 0 1px 3px 0 rgb(0, 0, 0, 0.1), 0 1px 2px -1px rgb(0, 0, 0, 0.1);
  display: flex;
  grid-auto-flow: 40px;
}

.kanji {
  font-size: 4rem;
  border: 2px solid var(--color-border);
  width: 140px;
  aspect-ratio: 1;
  border-radius: 0.1em;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.info {
  flex-grow: 1;
}

.line {
  display: flex;
  margin-bottom: 0.75rem;
}

.label {
  width: 200px;
  font-weight: 700;
  flex-shrink: 0;
}
</style>
