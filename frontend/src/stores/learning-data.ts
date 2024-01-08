import { defineStore } from 'pinia'
import type { CourseState, APIData } from '@/helpers/types'
import API_ENDPOINTS from '@/helpers/constants'

export const useLearningDataStore = defineStore('learning-data', {
  state: (): CourseState => ({
    allCourses: [],
    userCourses: [],
    currentCourse: undefined
  }),

  actions: {
    async updateAllCourse() {
      try {
        const res = await fetch(API_ENDPOINTS.courses)
        const data: APIData = await res.json()

        if (data.status === 'success') {
          this.allCourses = data.data
        }
      } catch (error) {
        this.allCourses = []
        console.error('Fetch error: ', error)
      }
    },
    async updateUserCourse(user_id: number) {
      try {
        const res = await fetch(`${API_ENDPOINTS.user_courses}${user_id}`)
        const data: APIData = await res.json()

        if (data.status === 'success') {
          this.userCourses = data.data
        }
      } catch (error) {
        this.userCourses = []
        console.error('Fetch error: ', error)
      }
    },
    setCurrentCourse(course_id: number | undefined) {
      this.currentCourse = course_id
    },
    clearData() {
      this.allCourses = []
      this.userCourses = []
      this.currentCourse = undefined
    }
  }
})
