<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { useUserStore } from '@/stores/user';
import { useLearningDataStore } from '@/stores/learning-data';
import { getAllCourseHelper } from '@/helpers/courses-helpers'
import Course from "../components/TheCourse.vue"
import type { course } from "../helpers/types"

const userStore = useUserStore();
const learningDataStore = useLearningDataStore();
const allCourses = ref<course[]>([])

onMounted(async () => {
  try {
    const response = await fetch('http://localhost:5000/courses');
    if (!response.ok) {
      allCourses.value = []
    }
    const courses = await response.json();
    allCourses.value = courses;
  } catch (error) {
    console.error('Fetch error: ', error);
  }

  if (userStore.isLogin) {
    learningDataStore.setUserCourses(userStore.id);
  }
});
</script>

<template>
  <main>
    <div class="wrapper">
      <div class="courses" v-if="userStore.isLogin">
        <h2>Your courses</h2>
        <div class="course-list">
          <Course v-for="course in learningDataStore.userCourses" :key="course.id" :id="course.id" :level="course.level"
            :title="course.title" :description="course.description" :percentage="course.percentage?.valueOf()"
            isDisplayPercentage />
        </div>
      </div>
      <div class="courses">
        <h2>All courses</h2>
        <div class="course-list">
          <Course v-for="course in allCourses" :key="course.id" :id="course.id" :level="course.level"
            :title="course.title" :description="course.description" :percentage=0 :isDisplayPercentage="false" />
        </div>
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

.courses {
  margin-bottom: 40px;
}

.course-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  column-gap: 16px;
  row-gap: 16px;
}

h2 {
  font-size: 1.25rem;
  font-weight: 500;
  margin-bottom: 1rem;
}
</style>
