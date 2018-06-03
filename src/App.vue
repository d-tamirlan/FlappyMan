<template>
  <div id="app">
    <!--<section id="social_sharing">-->
      <!--<script> document.write(VK.Share.button()); </script>-->
      <!--<social-sharing url="https://vuejs.org/"-->
                        <!--title="The Progressive JavaScript Framework"-->
                        <!--description="Intuitive, Fast and Composable MVVM for building interactive interfaces."-->
                        <!--quote="Vue is a progressive framework for building user interfaces."-->
                        <!--hashtags="vuejs,javascript,framework"-->
                        <!--twitter-user="vuejs"-->
                        <!--inline-template>-->
        <!--<network network="vk">-->
          <!--<i class="fa fa-vk"></i> VKontakte-->
        <!--</network>-->
      <!--</social-sharing>-->
    <!--</section>-->
    <div class="control"
         :class="pause ? 'play' : 'pause'"
         v-on:click="playGame"
    >
      <span class="left"></span><span class="right"></span>
    </div>
    <!--<img id="pause" src="./assets/pause.png" alt="pause">-->
    <!--<img id="play" src="./assets/play.png" alt="play">-->
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
      pause: true,
      raise_level_timeout: 1000
    }
  },
  created() {
    // Show alert before start the game
    this.$swal({
      title: 'Welcome',
      type: 'info',
      confirmButtonColor: '#41b883',
      confirmButtonText: '<span style="color: #35495e">Start the game!</span>'
    }).then(() => {
      this.playGame()
    });

    // Pause and play the game on "space" button
    window.addEventListener('keyup', event => {
      if (event.keyCode === 32){
        this.playGame()
      }
    });
  },
  methods: {
    playGame(){
      this.pause = !this.pause;

      if (!this.pause){
        let obstacles = this.$children[1];
        obstacles.moveObstacles();
        this.raiseDifficultyLevel()
      }
    },
    restartGame(){
      let
        character = this.$children[0],
        obstacles = this.$children[1];

      character.left_px = 10;
      character.top_px = Math.round(window.innerHeight/2);

      obstacles.items = obstacles.initObstacles();
      obstacles.points = 0;
      obstacles.move_timeout = 30;
      obstacles.record = this.$cookie.get('record') || 0;
      this.pause = false;
      obstacles.moveObstacles();
      this.raiseDifficultyLevel()
    },
    raiseDifficultyLevel(){
      let
        obstacles = this.$children[1];

      if (this.pause === true || obstacles.move_timeout === 0) return null;

      obstacles.move_timeout -= obstacles.move_timeout > 10 ? 1: 0.5;
      console.log(obstacles.move_timeout);
      setTimeout(this.raiseDifficultyLevel, this.raise_level_timeout);
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
    overflow: hidden;
  }
  #app {
    width: 100%;
    height: 100%;
    background: url("./assets/background.png") no-repeat;
    background-size: 100% 100%;
    overflow: hidden;
  }
  #logo {
    position: absolute;
    right: 0;
    width: 50px;
    z-index: 1;
  }
  #pause, #play{
    position: absolute;
    cursor: pointer;
    width: 60px;
    z-index: 1;
  }
  #pause{
    right: 120px;
  }
  #play{
    right: 50px;
  }
  .control {
  $circular_color: #35495e;
  $color: #41b883;
  $highlight: darken($color, 10%);
  $duration: 0.4s;
  $sin:  0.866;
  $size: 28px;

  border: $size*0.1 solid $circular_color;
  border-radius: 50%;
  margin: 2px;
  padding: $size*0.25;
  width: $size;
  height: $size;
  font-size: 0;
  white-space: nowrap;
  text-align: center;
  cursor: pointer;
  position: absolute;
  right: 60px;
  z-index: 1;

  &, .left, .right, &:before {
    display: inline-block;
    vertical-align: middle;
    transition: border $duration, width $duration, height $duration, margin $duration;
    transition-tiomig-function: cubic-bezier(1, 0, 0, 1);
  }

  &:before {
    content: "";
    height: $size;
  }

  &.pause {
    .left, .right {
      margin: 0;
      border-left: $size*0.33 solid $color;
      border-top: 0 solid transparent;
      border-bottom: 0 solid transparent;
      height: $size*$sin;
    }

    .left {
      border-right: $size*0.2 solid transparent;
    }
  }

  &.play {
    $border: $size/4;

    .left {
      margin-left: $size/6;
      border-left: $size*$sin/2 solid $color;
      border-top: $border solid transparent;
      border-bottom: $border solid transparent;
      border-right: 0px solid transparent;
      height: $size - 2*$border;
    }

    .right {
      margin: 0;
      border-left: $size*$sin/2 solid $color;
      border-top: $border solid transparent;
      border-bottom: $border solid transparent;
      height: 0px;
    }
  }

  &:hover {
    border-color: $highlight;

    .left, .right {
      border-left-color: $highlight;
    }
  }
}
</style>
