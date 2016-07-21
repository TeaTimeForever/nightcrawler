/**
 * Created by eq on 22/07/16.
 */
var canvas = document.getElementById("canvas"),
  ctx = canvas.getContext('2d');

const CANVAS_WIDTH = 600,
  CANVAS_LENGTH = 600,
  MIN_OBSTACLE_SIZE = 10,
  MAX_OBSTACLE_SIZE = 30,
  OBSTACLES_COUNT = 10;

canvas.width  = CANVAS_WIDTH;
canvas.height = CANVAS_LENGTH;

generatObstacles(OBSTACLES_COUNT);

function generatObstacles(count){
  initWalls();
  for(let i=0; i < count; i++) {
    ctx.fillRect(
      randomInRange(0, CANVAS_WIDTH-MAX_OBSTACLE_SIZE),
      randomInRange(0, CANVAS_LENGTH-MAX_OBSTACLE_SIZE),
      randomInRange(MIN_OBSTACLE_SIZE, MAX_OBSTACLE_SIZE),
      randomInRange(MIN_OBSTACLE_SIZE, MAX_OBSTACLE_SIZE));
  }
};

function initWalls(){
  ctx.strokeRect(0, 0, CANVAS_WIDTH, CANVAS_LENGTH);
}

function randomInRange(min, max) {
  return Math.random() * (max - min) + min;
}