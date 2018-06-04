import Vue from 'vue'
import App from './App.vue'
import VueSweetalert2 from 'vue-sweetalert2'
import VueCookie  from 'vue-cookie'


Vue.use(VueSweetalert2);
Vue.use(VueCookie);

new Vue({
  el: '#app',
  render: h => h(App)
});
