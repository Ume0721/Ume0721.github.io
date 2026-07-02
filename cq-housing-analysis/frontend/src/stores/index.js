import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAppStore = defineStore('app', () => {
  const currentDistrict = ref(null)
  const setDistrict = (value) => {
    currentDistrict.value = value
  }

  return {
    currentDistrict,
    setDistrict,
  }
})
