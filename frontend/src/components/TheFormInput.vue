<script setup lang="ts">
import { ref } from 'vue';

defineProps({
  name: String,
  label: String,
  type: String,
  required: Boolean,
})

const input = ref(HTMLInputElement)

</script>

<template>
  <div class="form-control">
    <label :for="name">{{ label }} <span class="required" v-if="required">*</span></label>
    <input :type="type" :name="name" ref="input" @change="$emit('updateValue', input)" />
  </div>
</template>

<style scoped>
.form-control {
  display: flex;
  flex-direction: column;
  margin-bottom: 0.875rem;
}

.form-control label {
  font-weight: 500;
  margin-bottom: 0.25rem;
  font-size: 0.875rem;
}

.form-control input {
  border: 2px solid var(--color-border);
  font-family: inherit;
  padding: 0.75rem 0.875rem;
  border-radius: 0.25em;
  outline: none;
}

.form-control input:focus {
  border-color: var(--color-primary);
}

.required {
  color: red;
}
</style>