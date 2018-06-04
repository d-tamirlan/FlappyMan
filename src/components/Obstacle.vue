<template>
  <div>
    <div id="statistic">
      <div><span id="pointsText">Current: </span><span id="points">{{points}}</span></div>
      <div><span id="recordText">Best record: </span><span id="record">{{record}}</span></div>
    </div>
    <div v-for="item in items" class="obstacles_couple_wrapper"
         v-bind:style="{left: item.obstacle_top.left + 'px'}"
    >
      <img :src="obstacle_top_src"
           alt="obstacle_top"
           class="obstacle_top"
           :width="width"
           :height="item.obstacle_top.height"
           v-bind:style="{left: item.obstacle_top.left + 'px', top: item.obstacle_top.height + 'px'}"
      >
      <img :src="obstacle_bottom_src"
           alt="obstacle_bottom"
           class="obstacle_bottom"
           :width="width"
           :height="item.obstacle_bottom.height"
           v-bind:style="{left: item.obstacle_bottom.left + 'px', top: item.obstacle_bottom.height + 'px'}"
      >
    </div>
    </div>
</template>

<script>
export default {
  data() {
    return {
      width: 50,
      obstacle_top_src: '/dist/obstacle_top.png',
      obstacle_bottom_src: '/dist/obstacle_bottom.png',
      // moving step of obstacles couple
      step: 3,
      // space between obstacles couple
      space_between: 400,
      move_timeout: 20,
      min_height: 80,
      // user points
      points: 0,
      // user best record
      record: this.$cookie.get('record') || 0,
      // space between top obstacle and bottom obstacle
      slot: Math.round(window.innerHeight / 3),
      // array of obstacles couples
      items: [],
    }
  },
  created(){
    this.items = this.initObstacles();
    this.moveObstacles();
    this.$parent.raiseDifficultyLevel();
  },
  methods: {
    calculateHeight(obstacles_couple){

      let
        min_height = this.min_height,
        max_height = window.innerHeight - this.min_height - this.slot,
        // random height from range
        obstacle_top_height = Math.floor(Math.random() * (max_height - min_height) + min_height),
        obstacle_bottom_height = Math.round(window.innerHeight - (obstacle_top_height + this.slot));

      obstacles_couple.obstacle_top.height = obstacle_top_height;
      obstacles_couple.obstacle_bottom.height = obstacle_bottom_height;

      return obstacles_couple
    },
    initObstacles(){

      let
        max_obstacles_qty = Math.round(window.innerWidth / this.space_between) + 1,
        // from middle of screen to right bound
        obstacles_position = Math.round(window.innerWidth / 2),
        items = [];

      for (let i=0; i < max_obstacles_qty; i++){
        let
          obstacle_top = {
            'left': obstacles_position,
            'right_bound': obstacles_position+this.width
          },
          obstacle_bottom = {
            'left': obstacles_position,
            'right_bound': obstacles_position+this.width
          },
          obstacles_couple = {'obstacle_top': obstacle_top, 'obstacle_bottom': obstacle_bottom};

        items.push(this.calculateHeight(obstacles_couple));
        obstacles_position += (this.space_between + this.width);
      }
      return items

    },
    clashCheck(){
        this.items.forEach(function (obstacles_couple, index, array) {
          let
            obstacle_top = obstacles_couple.obstacle_top,
            character = this.$parent.$children[0],

            obstacle_bottom_top_px = obstacle_top.height + this.slot,

            character_right_bound = character.left_px + character.width,
            character_bottom_bound = character.top_px+character.height,

            left_bound_intersection = obstacle_top.left > character.left_px && obstacle_top.left < character_right_bound,
            right_bound_intersection = obstacle_top.right_bound < character_right_bound && obstacle_top.right_bound > character.left_px,

            top_obstacle_clash = character.top_px <= obstacle_top.height && (left_bound_intersection || right_bound_intersection),

            bottom_obstacle_clash = character_bottom_bound >= obstacle_bottom_top_px && (left_bound_intersection || right_bound_intersection);

          if (top_obstacle_clash || bottom_obstacle_clash){
            this.$parent.pause = true;

            if (this.points > this.record) {
              this.$cookie.set('record', this.points, 7);
              this.record = this.points;
            }

            let telegram_share = document.querySelector('#telegram_share');

            // dynamic description form telegram sharing
            telegram_share.href = `https://t.me/share/url?url=${window.location.hostname}&text=My best record is ${this.record}! Try yourself!`;

            let social_sharing = document.querySelector('#social_sharing').innerHTML;

            this.$swal({
              title: 'Game Over',
              type: 'error',
              html: 'Share us on social media:<br> ' + social_sharing,
              confirmButtonText: '<span style="color: #35495e">Try again!</span>',
              confirmButtonColor: '#41b883',
            }).then(() => {
              this.$parent.restartGame();
            });
          }
        }, this);
    },
    moveObstacles(){
      if (this.$parent.pause) return null;
      this.items.forEach(function (obstacles_couple, index, array) {
        let
          obstacle_top = obstacles_couple.obstacle_top,
          obstacle_bottom = obstacles_couple.obstacle_bottom,
          last_obstacle = array[array.length-1].obstacle_top;

        if (obstacle_top.right_bound < 0) {
          this.calculateHeight(obstacles_couple);
          this.points += 1;
          obstacle_top.left = last_obstacle.right_bound + this.space_between;
          obstacle_bottom.left = obstacle_top.left;

          let changed_obstacle_couple = {'obstacle_top': obstacle_top, 'obstacle_bottom': obstacle_bottom};

          array.splice(index, 1);
          array.splice(array.length, 0, changed_obstacle_couple)

        } else {
          obstacle_top.left -= this.step;
          obstacle_bottom.left -= this.step;
        }
        obstacle_top.right_bound = obstacle_top.left + this.width;
        obstacle_bottom.right_bound -= obstacle_bottom.left + this.width;
      }, this);

      this.clashCheck();
      setTimeout(this.moveObstacles, this.move_timeout);
    }
  }
}
</script>

<style lang="scss">
  .obstacles_couple_wrapper{
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
  }
  #statistic{
    position: absolute;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    left: 10px;
    font-size: 30px;
    z-index: 1;

    #points, #record{
      font-family: 'Algerian';
      color: #01b889;
    }
    #pointsText, #recordText{
      font-family: 'Consolas';
      color: #35495e;
    }
  }

</style>
