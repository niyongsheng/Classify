/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/predict'
    },
    {
	  path: '/predict',
	  name: 'predict',
	  component: require('@/components/predict').default
    },
    {
	  path: '/result',
	  name: 'result',
	  component: require('@/components/result').default
    }
  ]
})
