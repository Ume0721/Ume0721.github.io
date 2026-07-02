import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/layouts/MainLayout.vue'),
    children: [
      { path: '', name: 'Dashboard', component: () => import('@/views/Dashboard.vue') },
      { path: 'explorer', name: 'Explorer', component: () => import('@/views/DataExplorer.vue') },
      { path: 'analysis', name: 'Analysis', component: () => import('@/views/Analysis.vue') },
    ],
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
