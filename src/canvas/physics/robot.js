import { Body } from "./body";
import { Sensor } from "./sensor";
import { Rectangle } from "./rectangle";

export class Robot extends Body {

  constructor(position, angle, base){
    super(position, angle, base);
    this.shape = new Rectangle(
      {width: 32, height: 32},
      {x: 0, y: 0},
      0, this
    );

    this.leftEye = new Sensor({
      sector: 0.3,
      maxDistance: 200,
      size: 8
    }, {
      x: 16, y: 16
    }, 0, this.shape);

    this.rightEye = new Sensor({
      sector: 0.3,
      maxDistance: 200,
      size: 8
    }, {
      x: 16, y: -16
    }, 0, this.shape);

    this.shape.color = "#0f0";
  }

  step(obstacles){
    var rightEyeObstacles = this.rightEye.evaluate(obstacles);
    var leftEyeObstacles  = this.leftEye.evaluate(obstacles);

    this.rightEye.color = `rgba(0, 0, 255, ${1-(rightEyeObstacles / this.rightEye.options.maxDistance)})`;
    this.leftEye.color = `rgba(0, 0, 255, ${1-(leftEyeObstacles / this.leftEye.options.maxDistance)})`;

    var commands = this.run(leftEyeObstacles, rightEyeObstacles);
    commands.forEach(c => {
      this.execute(c);
    });
  }

  execute(command) {
    switch (command) {
      case "turn left": this.rotate(-0.01); break;
      case "turn right": this.rotate(0.01); break;
      case "move forward": this.makeStep(0.5); break;
    }
  }

  run(leftSonarOutput, rightSonarOutput) {
    return ["move forward", "turn right"];
  }

}
