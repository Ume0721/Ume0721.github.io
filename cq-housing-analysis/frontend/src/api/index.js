import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 30000,
})

api.interceptors.response.use(
  (res) => res.data,
  (err) => Promise.reject(err)
)

export const getSummary = () => api.get('/houses/summary')
export const getHouseList = (params) => api.get('/houses/list', { params })
export const getDistricts = () => api.get('/houses/districts')

export const getDistrictRank = () => api.get('/viz/district-ranking')
export const getPriceTrend = (params) => api.get('/viz/price-trend', { params })
export const getLayoutDist = (params) => api.get('/viz/layout-distribution', { params })
export const getScatter = (params) => api.get('/viz/scatter', { params })

export const getPrediction = () => api.get('/stats/prediction')
export const getClustering = (params) => api.get('/stats/clustering', { params })
export const getCorrelation = () => api.get('/stats/correlation')

export const seedMockData = (count) => api.post(`/dataset/seed-mock?count=${count}`)
export const clearData = () => api.delete('/dataset/clear')

export default api
