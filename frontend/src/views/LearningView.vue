<script setup lang="ts">
import { ref, onMounted } from "vue";
import WordDetailCard from "../components/TheWordDetailCard.vue"
import { useUserStore } from '@/stores/user';
import { getLearningWords } from "@/helpers/courses-helpers";

const learningWords = ref<string[]>([])
const userStore = useUserStore();

onMounted(() => {
  learningWords.value = getLearningWords(userStore.id, 'grd01').data
})

</script>

<template>
  <main>
    <div class="wrapper">
      <WordDetailCard />
      <div class="buttons">
        <button class="new">It's new to me</button>
        <button class="remembered">Already in my memory</button>
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
