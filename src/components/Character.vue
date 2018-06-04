<template>
  <img :src="img_src"
       alt="character"
       id="character"
       :width="width"
       :height="height"
       v-bind:style="{left: left_px + 'px', top: top_px + 'px'}"
  >
</template>

<script>
  import Obstacle from './Obstacle.vue'

export default {
  data() {
    return {
      width: 106,
      height: 60,
      img_src: '/dist/character.png',
      step: 30,
      left_px: 10,
      top_px: Math.round(window.innerHeight/2)
    }
  },
  components: {
    Obstacle
  },
  created() {
    window.addEventListener('keydown', event => {
      if (this.$parent.pause) return null;

      if (event.keyCode === 38){
        this.moveUp()
      } else if (event.keyCode === 40){
        this.moveDown()
      } else if (event.keyCode === 39){
        this.moveRight()
      } else if (event.keyCode === 37){
        this.moveLeft()
      }
    })
  },
  methods:{
    moveUp(){
      let new_top_px = this.top_px - this.step;
      this.top_px = (new_top_px < 0) ? 0 : new_top_px;
      //  условие ? значение1 : значение2
    },
    moveDown(){
      let
        new_top_px = this.top_px + this.step,
        bottom_bound = new_top_px + this.height,
        window_height = window.innerHeight;
      this.top_px = (bottom_bound > window_height) ? (window_height - this.height) : new_top_px;

      //  условие ? значение1 : значение2
    },
    moveRight(){
      let
        new_left_px = this.left_px + this.step,
        right_bound = new_left_px + this.width,
        window_width = window.innerWidth;
      this.left_px = (right_bound >= window_width) ? (window_width - this.width) : new_left_px;
      //  условие ? значение1 : значение2
    },
    moveLeft(){
      let
        new_left_px = this.left_px - this.step;
      this.left_px = (new_left_px < 0) ? 0 : new_left_px;

      //  условие ? значение1 : значение2
    }
  }
}
</script>

<style lang="scss">
  #character{
    position: absolute;
  }
</style>
