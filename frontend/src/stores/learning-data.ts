import { defineStore } from 'pinia'
import { getUserCourses, getUserWords } from '@/helpers/courses-helpers'
import type { courseState } from '../helpers/types'

export const useLearningDataStore = defineStore('learning-data', {
  state: (): courseState => ({
    userCourses: [],
    userKanjis: []
  }),

  actions: {
    setUserCourses(user_id: string) {
      const res = getUserCourses(user_id)

      if (res.isSuccess && res.data) {
        this.userCourses = res.data
      }
    },
    setUserKanji(user_id: string) {
      const res = getUserWords(user_id)

      if (res.isSuccess && res.data) {
        this.userKanjis = res.data
      }
    }
  }
})
