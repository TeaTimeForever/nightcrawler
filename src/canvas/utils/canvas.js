import { Rectangle } from "../physics/rectangle";
import { Sensor } from "../physics/sensor";

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

  generateRobot(){
    var robot = new Rectangle(
      {width: 32, height: 32},
      {x: 300, y: 300},
      0
    );

    var s1 = new Sensor({
      sector: 0.3,
      maxDistance: 100,
      size: 8
    }, {
      x: 16, y: 16
    }, 0, robot);

    var s2 = new Sensor({
      sector: 0.3,
      maxDistance: 100,
      size: 8
    }, {
      x: 16, y: -16
    }, 0, robot);
    robot.color = "#0f0";
    return robot;
  }

  start(){
    var robot = this.generateRobot();
    const animate = () => {
      this.ctx.clearRect(0,0,this.configs.canvasWidth, this.configs.canvasHeight);
      this.initWalls();
      this.obstacles.forEach(obstacle => {
        obstacle.drawOn(this.ctx);
        // uncomment if sad
        // obstacle.rotate(0.01);
        // obstacle.makeStep(1);
      });
      robot.drawOn(this.ctx);
      requestAnimationFrame(animate);
    };
    animate();
  }

  initWalls(){
    this.ctx.strokeRect(0, 0, this.configs.canvasWidth, this.configs.canvasHeight);
  }
}

function randomInRange(min, max) {
  return Math.random() * (max - min) + min;
}