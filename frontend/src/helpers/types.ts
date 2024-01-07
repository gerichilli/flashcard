export type user = {
  id: string
  username: string
  password: string
}

export type course = {
  id: string
  level: string
  title: string
  description: string
  percentage?: Number
}

export type courseState = {
  userCourses: course[]
  userKanjis: string[]
}

export type kanji = {
  grade: Number
  heisig_en: string
  jlpt: Number
  kanji: string
  kun_readings: string[]
  meanings: string[]
  name_readings: string[]
  notes: string[]
  on_readings: string[]
  stroke_count: Number
  unicode: string[]
}

export type user_course = {
  user_id: string
  courses: {
    id: string
    percentage: Number
  }[]
}

export type course_kanji = {
  course_id: string
  words: string[]
}

export type user_kanji = {
  user_id: string
  words: string[]
}

export type user_kanji_status = {
  kanji: string
  isRemembered?: boolean
}
