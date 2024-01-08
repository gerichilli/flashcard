export type APIData = {
  status: 'success' | 'failed'
  message?: string
  data?: any
}

export type User = {
  id: Number
  username: string
}

export type Kanji = {
  jlpt?: Number
  kanji: string
  kun_reading: string
  meanings: string
  on_reading: string
  stroke_count: Number
  is_remembered?: boolean
}

export type Course = {
  id: Number
  level: string
  title: string
  description: string
  percentage?: Number
  kanjis: Kanji[]
}

export type CourseState = {
  allCourses: Course[]
  userCourses: {
    id: Number
    level: string
    title: string
    description: string
    percentage?: Number
    kanjis: {
      [key: string]: boolean
    }
  }[]
  currentCourse: number | undefined
}
