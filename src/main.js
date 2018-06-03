import Vue from 'vue'
import App from './App.vue'
import VueSweetalert2 from 'vue-sweetalert2'
import VueCookie  from 'vue-cookie'
import SocialSharing from 'vue-social-sharing'

Vue.use(VueSweetalert2);
Vue.use(VueCookie);
Vue.use(SocialSharing);

new Vue({
  el: '#app',
  render: h => h(App)
});
