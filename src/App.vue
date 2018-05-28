<template>
  <div id="app">
    <img id="logo" src="./assets/logo.png">
    <character></character>
    <obstacle></obstacle>
  </div>
</template>

<script>
  import Character from './components/Character.vue'
  import Obstacle from './components/Obstacle.vue'

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    'character': Character,
    'obstacle': Obstacle,
  }
}
</script>

<style lang="scss">

  html, body{
    margin: 0;
    width: 100%;
    height: 100%;
  }
  #app {
    width: 100%;
    height: 100%;
    background-image: url("./assets/background.png");
    background-size: contain;
  }
  #logo {
    position: absolute;
    right: 0;
    width: 50px;
  }
</style>
