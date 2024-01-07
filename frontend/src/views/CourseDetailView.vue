<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { getCourseById, getWordsByCourseId } from '@/helpers/courses-helpers';
import { useUserStore } from '@/stores/user';
import { useLearningDataStore } from '@/stores/learning-data';
import type { course, user_kanji_status } from '@/helpers/types';
import Card from "../components/TheWordCard.vue"

const route = useRoute()
const courseData = ref<course>({
  id: '',
  level: '',
  title: '',
  description: '',
  percentage: 0,
})
const wordData = ref<user_kanji_status[]>([])
const userStore = useUserStore();
const learningDataStore = useLearningDataStore();

onMounted(() => {
  const id = route.params.id as string
  const courseRes = getCourseById(id)
  const wordsRes = getWordsByCourseId(id)
  const userCourses = learningDataStore.userCourses
  const percentage = userCourses.filter(c => c.id === id)[0] ? userCourses.filter(c => c.id === id)[0].percentage : 0

  learningDataStore.setUserKanji(userStore.id)

  if (courseRes.isSuccess && courseRes.data) {
    courseData.value = {
      ...courseRes.data,
      percentage
    }
  }

  if (wordsRes.isSuccess && wordsRes.data) {

    wordData.value = wordsRes.data.map(d => {
      const isRemembered = learningDataStore.userKanjis.filter(k => k === d).length > 0
      return {
        kanji: d,
        isRemembered
      }
    })
  }
})

</script>

<template>
  <main>
    <div class="wrapper">
      <div class="card">
        <div class="card-info">
          <div class="level">
            <span class="level-mark">{{ courseData.level }}</span>
            <h1>{{ courseData.title }}</h1>
          </div>
          <p class="description">
            {{ courseData.description }}
          </p>
        </div>
        <div class="process">
          <svg viewBox="0 0 36 36">
            <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none"
              stroke="#e97777" stroke-width="2" />
            <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none"
              stroke="#fff" stroke-width="2" class="percentage-circle" />
            <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="percentage">{{
              courseData.percentage }}</text>
          </svg>
        </div>
      </div>
      <div class="course-header">
        <h2 class="course-heading">
          Details
        </h2>
        <div class="course-btn">
          <RouterLink class="resume" to="/learning">Learn</RouterLink>
          <button class="reset">Reset</button>
          <button class="delete">Delete</button>
        </div>
      </div>
      <div class="list">
        <Card v-for="kanji in wordData" :key="kanji.kanji" :text="kanji.kanji" :isRemembered="kanji.isRemembered" />
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

.card {
  background: var(--color-gradient);
  padding: 3rem 2rem;
  border-radius: 0.375rem;
  text-decoration: none;
  transition: 0.4s;
  color: var(--color-text);
  display: flex;
  gap: 2rem;
  margin-bottom: 48px;
  color: #ffffff;
  box-shadow: 0 1px 3px 0 rgb(0, 0, 0, 0.1), 0 1px 2px -1px rgb(0, 0, 0, 0.1);
}

.level {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.5rem;
}

.level-mark {
  width: 48px;
  height: 48px;
  background: #ffffff;
  color: var(--color-heading);
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 2px;
  font-size: 1.25rem;
}

h1 {
  font-weight: 700;
  font-size: 1.5rem;
}

.description {
  font-size: 1.125rem;
}

.process {
  width: 100px;
  height: 100px;
  right: 1.5rem;
  flex-shrink: 0;
}

.percentage {
  font-size: 12px;
  fill: #ffffff;
}

.percentage-circle {
  stroke-dasharray: 0 100;
  animation: progress 1s linear forwards;
}


@keyframes progress {
  from {
    stroke-dasharray: 0 100;
  }

  to {
    stroke-dasharray: v-bind('courseData.percentage') 100;
  }
}

.list {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 1.25rem;
}

.course-header {
  display: flex;
  align-items: center;
  margin-bottom: 24px;
}

.course-heading {
  font-weight: 500;
  font-size: 1.5rem;
  margin-right: auto;
}

.course-btn {
  display: flex;
  gap: 1rem;
}

.course-btn>* {
  border: none;
  outline: none;
  cursor: pointer;
  font: inherit;
  font-weight: 500;
  padding: 0.5em 1em;
  border-radius: 0.25em;
  transition: 0.4s;
}

.resume {
  background: var(--color-primary);
  color: #ffffff;
}

.delete {
  color: red
}

@media (hover: hover) {
  .resume:hover {
    background: var(--color-gradient);
    text-decoration: none;
  }

  .reset:hover,
  .delete:hover {
    background-color: #333;
    color: #ffffff;
  }
}
</style>
