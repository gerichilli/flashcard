<script setup lang="ts">
import { onMounted } from 'vue';
import { useUserStore } from '@/stores/user';
import { useLearningDataStore } from '@/stores/learning-data';
import CourseComponent from "../components/TheCourse.vue"

const userStore = useUserStore();
const learningDataStore = useLearningDataStore();

onMounted(async () => {
  learningDataStore.updateAllCourse()
  learningDataStore.updateUserCourse(+userStore.id)
});
</script>

<template>
  <main>
    <div class="wrapper">
      <div class="courses" v-if="userStore.isLogin">
        <h2>Your courses</h2>
        <div class="course-list">
          <CourseComponent v-for="course in learningDataStore.userCourses" :key="course.id.toString()"
            :id="course.id.toString()" :level="course.level" :title="course.title" :description="course.description"
            :percentage="course.percentage?.valueOf()" isDisplayPercentage />
        </div>
      </div>
      <div class="courses">
        <h2>All courses</h2>
        <div class="course-list">
          <CourseComponent v-for="course in learningDataStore.allCourses" :key="course.id.toString()"
            :id="course.id.toString()" :level="course.level" :title="course.title" :description="course.description"
            :percentage=0 :isDisplayPercentage="false" />
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
