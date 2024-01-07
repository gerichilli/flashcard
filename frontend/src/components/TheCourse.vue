<script setup lang="ts">
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router'
// import $ from 'jquery'

defineProps({
  id: String,
  level: String,
  title: String,
  description: String,
  percentage: Number,
  isDisplayPercentage: Boolean
})

onMounted(() => {
  // $(".percentage-circle").css("stroke-dasharray", "75, 100")
})
</script>

<template>
  <RouterLink class="card" :to="'course/' + id">
    <div class="card-info">
      <div class="level">
        <span class="level-mark">{{ level }}</span>
        <h3>{{ title }}</h3>
      </div>
      <p class="description">{{ description }}</p>
    </div>
    <div class="process" v-if="isDisplayPercentage">
      <svg viewBox="0 0 36 36">
        <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none" stroke="#ddd"
          stroke-width="2" />
        <path d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831" fill="none"
          stroke="#e97777" stroke-width="2" class="percentage-circle" />
        <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" class="percentage">{{ percentage || 0
        }}</text>
      </svg>
    </div>
  </RouterLink>
</template>

<style scoped>
.card {
  background-color: var(--color-background);
  border: 2px solid var(--color-border);
  padding: 1.25rem;
  border-radius: 0.375rem;
  text-decoration: none;
  cursor: pointer;
  transition: 0.4s;
  color: var(--color-text);
  display: flex;
  gap: 1rem;
}

.level {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.level-mark {
  width: 36px;
  height: 36px;
  color: #ffffff;
  background: var(--color-gradient);
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 2px;
}

h3 {
  font-weight: 700;
  font-size: 1rem;
  transition: 0.4s;
}

.description {
  font-size: 0.875rem;
}

.process {
  width: 60px;
  height: 60px;
  right: 1.5rem;
  flex-shrink: 0;
}

.percentage {
  font-size: 12px;
}

.percentage-circle {
  stroke-dasharray: 0 100;
  animation: progress 0.7s linear forwards;
}

@keyframes progress {
  from {
    stroke-dasharray: 0 100;
  }

  to {
    stroke-dasharray: v-bind('percentage') 100;
  }
}

@media (hover: hover) {
  .card:hover {
    text-decoration: none;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  }

  .card:hover h3 {
    background: var(--color-gradient);
    background-clip: text;
    -webkit-text-fill-color: transparent;
  }
}
</style>