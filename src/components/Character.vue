<template>
  <img :src="img_src"
       alt="character"
       id="character"
       v-bind:style="{left: left_px + 'px', top: top_px + 'px'}"
  >
</template>

<script>
export default {
  data() {
    return {
      img_src: 'src/assets/character.png',
      step: 10,
      left_px: 0,
      top_px: 0
    }
  },
  created() {
    window.addEventListener('keyup', e => {
      alert('asd');
      this.top_px = 10
    })
  },
  methods:{
    moveUp(event){
      alert('asda');
      this.top_px -= this.step;
    }
  }
}
</script>

<style lang="scss">

</style>
