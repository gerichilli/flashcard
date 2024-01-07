<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import type { kanji } from '../helpers/types'

const kanjiData = ref<kanji>({
  grade: 0,
  heisig_en: '',
  jlpt: 0,
  kanji: '',
  kun_readings: [],
  meanings: [],
  name_readings: [],
  notes: [],
  on_readings: [],
  stroke_count: 0,
  unicode: []
})
const route = useRoute()

const fetchData = async (kanji: string) => {
  const res = await fetch(`https://kanjiapi.dev/v1/kanji/${kanji}`)
  const data = await res.json()
  kanjiData.value = data
}

onMounted(() => {
  fetchData(route.params.kanji[0])
})
</script>

<template>
  <div class="card">
    <h2 class="kanji">{{ kanjiData.kanji }}</h2>
    <div class="info">
      <div class="line">
        <p class="label">Meanings: </p>
        <p class="content">{{ kanjiData.meanings.join(', ') }}</p>
      </div>
      <div class="line">
        <p class="label">On Readings: </p>
        <p class="content">{{ kanjiData.on_readings.join(', ') }}</p>
      </div>
      <div class="line">
        <p class="label">Kun Readings: </p>
        <p class="content">{{ kanjiData.kun_readings.join(', ') }}</p>
      </div>
      <div class="line">
        <p class="label">Stroke Count: </p>
        <p class="content">{{ kanjiData.stroke_count }}</p>
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
}
</style>
