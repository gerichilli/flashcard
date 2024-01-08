<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user';
import { useLearningDataStore } from '@/stores/learning-data';
import router from '@/router';
import type { Kanji, Course, APIData } from '@/helpers/types';
import API_ENDPOINTS from '@/helpers/constants';
import Card from "../components/TheWordCard.vue"

const userStore = useUserStore();
const learningDataStore = useLearningDataStore();

const route = useRoute()
const courseData = ref<Course>({
  id: 0,
  level: '',
  title: '',
  description: '',
  percentage: 0,
  kanjis: []
})

const courseId = route.params.id as string;

async function handleLearning() {
  if (userStore.isLogin) {
    learningDataStore.setCurrentCourse(+courseId)

    await fetch(API_ENDPOINTS.update_course, {
      method: 'POST',
      cache: 'no-cache',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ user_id: userStore.id, course_id: +courseId })
    })

    router.push('/learning')
  } else {
    router.push('/register')
  }

}

onMounted(async () => {
  const res = await fetch(`${API_ENDPOINTS.course_kanji}${courseId}`);
  const data: APIData = await res.json();

  if (data.status !== "success") return;

  const course = learningDataStore.userCourses.filter(c => c.id === data.data.id)[0];

  if (userStore.isLogin && course) {
    courseData.value = {
      ...data.data,
      percentage: course.percentage || data.data.percentage,
      kanjis: data.data.kanjis.map((kanji: Kanji) => {
        return {
          ...kanji,
          is_remembered: course.kanjis[kanji.kanji as keyof typeof course.kanjis] || false
        }
      })
    }
  } else {
    courseData.value = data.data
  }

  console.log(courseData.value)
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
          <button class="resume" @click="handleLearning">Learn</button>
          <!-- <button class="reset">Reset</button>
          <button class="delete">Delete</button> -->
        </div>
      </div>
      <div class="list">
        <Card v-for="kanji in courseData.kanjis" :key="kanji.kanji" :text="kanji.kanji"
          :isRemembered="kanji.is_remembered" />
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
