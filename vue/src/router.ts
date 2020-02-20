import Vue from 'vue'
import Router from 'vue-router'
import Index from './views/Index.vue'
import Members from './views/Members.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: Index
    },
    {
      path: '/members',
      name: 'members',
      component: Members
    }
  ]
})
