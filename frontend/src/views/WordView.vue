<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import router from '../router/index'
import WordDetailCard from "../components/TheWordDetailCard.vue"
import type { Kanji, APIData } from '@/helpers/types'
import API_ENDPOINTS from '@/helpers/constants';

const route = useRoute()
const character = route.params.kanji[0]

const kanjiData = ref<Kanji>({
  kanji: '',
  kun_reading: '',
  meanings: '',
  on_reading: '',
  stroke_count: 0,
})

onMounted(async () => {
  const res = await fetch(`${API_ENDPOINTS.kanji}${character}`)
  const data: APIData = await res.json()
  if (data.status === 'success') {
    kanjiData.value = data.data
  }
})
</script>

<template>
  <main>
    <div class="wrapper">
      <div class="top">
        <a @click="router.back()" class="back">
          Back
        </a>
      </div>
      <WordDetailCard :kanji="kanjiData.kanji" :kun_reading="kanjiData.kun_reading.split(',').join(', ')"
        :on_reading="kanjiData.on_reading.split(',').join(', ')" :meanings="kanjiData.meanings.split(',').join(', ')"
        :stroke_count="+kanjiData.stroke_count" />
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
