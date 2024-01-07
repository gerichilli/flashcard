import { v4 as uuidv4 } from 'uuid'
import { users } from './data'
import { isEmpty } from './utils'

export const loginHelper = (username: string, password: string) => {
  const user = users.filter((user) => user.username === username && user.password === password)[0]

  if (!user || isEmpty(user)) {
    return {
      data: null,
      isSuccess: false
    }
  }

  return {
    data: user,
    isSuccess: true
  }
}

export const registerHelper = (username: string, password: string) => {
  let user = users.filter((user) => user.username === username && user.password === password)[0]

  if (user && !isEmpty(user)) {
    return {
      data: user,
      isSuccess: true
    }
  }

  user = {
    id: uuidv4(),
    username,
    password
  }

  users.push(user)

  return {
    data: user,
    isSuccess: true
  }
}
