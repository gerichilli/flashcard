import { defineStore } from 'pinia'
import { registerHelper, loginHelper } from '../helpers/user-helpers'
import type { user } from '../helpers/types'

export const useUserStore = defineStore('user', {
  state: (): user => ({
    username: '',
    password: '',
    id: ''
  }),
  getters: {
    isLogin: (state) => state.username && state.password
  },
  actions: {
    register(username: string, password: string) {
      if (username && password) {
        const res = registerHelper(username, password)

        if (res.isSuccess) {
          this.username = res.data.username
          this.password = res.data.password
          this.id = res.data.id
        }
      }
    },
    login(username: string, password: string) {
      if (username && password) {
        const res = loginHelper(username, password)

        if (res.data && res.isSuccess) {
          this.username = res.data.username
          this.password = res.data.password
          this.id = res.data.id
        }
      }
    }
  }
})
