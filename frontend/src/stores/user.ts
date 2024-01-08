import { defineStore } from 'pinia'
import type { User, APIData } from '@/helpers/types'
import API_ENDPOINTS from '@/helpers/constants'

export const useUserStore = defineStore('user', {
  state: (): User => ({
    id: 0,
    username: ''
  }),
  getters: {
    isLogin: (state) => (state.username && state.id ? true : false)
  },
  actions: {
    async register(username: string, password: string) {
      if (username && password) {
        const res = await fetch(API_ENDPOINTS.register, {
          method: 'POST',
          cache: 'no-cache',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ username, password })
        })

        const data: APIData = await res.json()

        if (data.status === 'success') {
          this.id = data.data.id
          this.username = data.data.username
        } else {
          alert(data.message)
        }
      }
    },
    async login(username: string, password: string) {
      if (username && password) {
        const res = await fetch(API_ENDPOINTS.login, {
          method: 'POST',
          cache: 'no-cache',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ username, password })
        })

        const data: APIData = await res.json()

        if (data.status === 'success') {
          this.id = data.data.id
          this.username = data.data.username
        } else {
          alert(data.message)
        }
      }
    },
    logout() {
      this.id = 0
      this.username = ''
    }
  }
})
