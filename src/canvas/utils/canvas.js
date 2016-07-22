/**
 * Created by eq on 22/07/16.
 */

export class Canvas {

  constructor(id) {
    this.canvas = document.getElementById(id);
    this.ctx    = canvas.getContext('2d');
    this.configs = {
      canvasWidth: 600,
      canvasLength: 600,
      minObstacleSize: 10,
      maxObstacleSize: 40
    };

    this.canvas.width  = this.configs.canvasWidth;
    this.canvas.height = this.configs.canvasLength;
  };

  generateObstacles(count) {
    for(let i=0; i < count; i++) {
      this.ctx.fillRect(
        randomInRange(0, this.configs.canvasWidth-this.configs.maxObstacleSize),
        randomInRange(0, this.configs.canvasLength-this.configs.maxObstacleSize),
        randomInRange(this.configs.minObstacleSize, this.configs.maxObstacleSize),
        randomInRange(this.configs.minObstacleSize, this.configs.maxObstacleSize));
    }
  }

  initWalls(){
    this.ctx.strokeRect(0, 0, this.configs.canvasWidth, this.configs.canvasLength);
  }
}


function randomInRange(min, max) {
  return Math.random() * (max - min) + min;
}