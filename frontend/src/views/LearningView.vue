<script setup lang="ts">
import { ref, onMounted } from "vue";
import WordDetailCard from "../components/TheWordDetailCard.vue"
import { useUserStore } from '@/stores/user';
import router from '@/router';
import { useLearningDataStore } from '@/stores/learning-data';
import API_ENDPOINTS from "@/helpers/constants";
import type { Kanji, APIData } from "@/helpers/types";

const learningWords = ref<Kanji[]>([]);
const currentIndex = ref(0)
const rememberedKanji = ref<string[]>([]);
const userStore = useUserStore();
const learningDataStore = useLearningDataStore();

onMounted(async () => {
  if (userStore.isLogin) {
    const res = await fetch(API_ENDPOINTS.learning, {
      method: 'POST',
      cache: 'no-cache',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        course_id: learningDataStore.currentCourse,
        user_id: userStore.id
      })
    })

    const data: APIData = await res.json()

    if (data.status === 'success') {
      learningWords.value = data.data
    }
  }
})

async function updateRememberedKanji(kanji_list: string[]) {
  // Call API
  await fetch(API_ENDPOINTS.update_learning, {
    method: 'POST',
    cache: 'no-cache',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user_id: userStore.id,
      kanji_list: kanji_list
    })
  })
}

async function handleNext() {
  if (currentIndex.value >= learningWords.value.length - 1) {
    alert("Completed a learning section")

    try {
      await updateRememberedKanji(rememberedKanji.value)
      router.push(`course/${learningDataStore.currentCourse}`)
    } catch (error) {
      console.error(error)
      router.push(`/`)
    }
  } else {
    currentIndex.value++
  }
}

async function handleRemembered() {
  if (currentIndex.value >= learningWords.value.length - 1) {
    alert("Completed a learning section")
    await updateRememberedKanji(rememberedKanji.value)

    try {
      await updateRememberedKanji(rememberedKanji.value)
      router.push(`course/${learningDataStore.currentCourse}`)
    } catch (error) {
      console.error(error)
      router.push(`/`)
    }
  } else {
    rememberedKanji.value.push(learningWords.value[currentIndex.value].kanji)
    currentIndex.value++
  }
}

</script>

<template>
  <main>
    <div class="wrapper" v-if="learningWords[currentIndex]">
      <WordDetailCard :kanji="learningWords[currentIndex].kanji"
        :kun_reading="learningWords[currentIndex].kun_reading.split(',').join(', ')"
        :on_reading="learningWords[currentIndex].on_reading.split(',').join(', ')"
        :meanings="learningWords[currentIndex].meanings.split(',').join(', ')"
        :stroke_count="+learningWords[currentIndex].stroke_count" />
      <div class="buttons">
        <button class="new" @click="handleNext">It's new to me</button>
        <button class="remembered" @click="handleRemembered">Already in my memory</button>
      </div>
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

.buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

button {
  border: none;
  outline: none;
  cursor: pointer;
  font: inherit;
  font-weight: 500;
  padding: 0.5em 1em;
  border-radius: 0.25em;
  transition: 0.4s;
}


.new {
  background: var(--color-text);
  color: #ffffff;
}

.remembered {
  background: var(--color-primary);
  color: #ffffff;
}
</style>
