import { courses, course_words, user_courses, user_kanjis } from './data'
import type { course } from './types'

export const getAllCourseHelper = () => {
  return {
    data: courses,
    isSuccess: true
  }
}

export const getCourseById = (id: string) => {
  const course = courses.filter((course) => course.id === id)[0]

  if (course) {
    return {
      data: course,
      isSuccess: true
    }
  }

  return {
    data: null,
    isSuccess: false
  }
}

export const getWordsByCourseId = (id: string) => {
  const collection = course_words.filter((collection) => collection.course_id === id)[0]

  if (collection) {
    return {
      data: collection.words,
      isSuccess: true
    }
  }

  return {
    data: null,
    isSuccess: false
  }
}

export const getUserCourses = (user_id: string) => {
  const userCourses = user_courses.filter((user) => user.user_id === user_id)[0]

  if (userCourses) {
    const data: course[] = []

    userCourses.courses.forEach((course) => {
      const courseData = getCourseById(course.id).data

      if (courseData) {
        data.push({
          ...courseData,
          percentage: course.percentage
        })
      }
    })

    return {
      data: data,
      isSuccess: true
    }
  }

  return {
    data: null,
    isSuccess: false
  }
}

export const getUserWords = (user_id: string) => {
  const userData = user_kanjis.filter((data) => data.user_id === user_id)[0]

  if (userData) {
    return {
      data: userData.words,
      isSuccess: true
    }
  }

  return {
    data: null,
    isSuccess: false
  }
}

export const getLearningWords = (user_id: string, course_id: string) => {
  const words: string[] = []
  const learnedWords = user_kanjis.filter((k) => k.user_id === user_id)[0].words

  course_words.forEach((course) => {
    if (course.course_id === course_id) {
      words.push(course.words.filter((w) => learnedWords.find((word) => w === word))[0])
    }
  })

  return {
    data: words,
    isSuccess: true
  }
}
