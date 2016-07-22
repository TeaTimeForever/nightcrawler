import { Rectangle } from "../physics/rectangle";

export class Canvas {

  constructor(id) {
    this.canvas = document.getElementById(id);
    this.ctx    = canvas.getContext('2d');
    this.configs = {
      canvasWidth: 600,
      canvasHeight: 600,
      minObstacleSize: 10,
      maxObstacleSize: 40
    };

    this.canvas.width  = this.configs.canvasWidth;
    this.canvas.height = this.configs.canvasHeight;

    this.obstacles = [];
  };

  generateObstacles(count) {
    for(let i=0; i < count; i++) {
      this.obstacles.push(new Rectangle({
        width: randomInRange(this.configs.minObstacleSize, this.configs.maxObstacleSize),
        height: randomInRange(this.configs.minObstacleSize, this.configs.maxObstacleSize)
      }, {
        x: randomInRange(0 + this.configs.maxObstacleSize, this.configs.canvasWidth - this.configs.maxObstacleSize),
        y: randomInRange(0 + this.configs.maxObstacleSize, this.configs.canvasHeight - this.configs.maxObstacleSize),
      }, randomInRange(0, Math.PI*2)));
    }
  }

  start(){
    const animate = () => {
      this.ctx.clearRect(0,0,this.configs.canvasWidth, this.configs.canvasHeight);
      this.initWalls();
      this.obstacles.forEach(obstacle => {
        obstacle.drawOn(this.ctx);
        // uncomment if sad
        // obstacle.rotate(0.01);
        // obstacle.makeStep(1);
      });
      requestAnimationFrame(animate);
    }
    animate();
  }

  initWalls(){
    this.ctx.strokeRect(0, 0, this.configs.canvasWidth, this.configs.canvasHeight);
  }
}

function randomInRange(min, max) {
  return Math.random() * (max - min) + min;
}