import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('./pages/Home.vue')
  },
  {
    path: '/pokemons',
    name: 'Pokemons',
    component: () => import('./pages/Pokemons.vue')
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('./pages/About.vue')
  },
  {
    path: "/battle",
    name: "Battle",
    component: () => import('./pages/Battle.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;