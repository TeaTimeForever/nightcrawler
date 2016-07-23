import { Body } from "./body";
import { IdealSensor } from "./ideal.sensor";
import { Point } from "./point";
import { drawPolygon } from "../utils/graphics";

export class Sensor extends Body {
  /**
   * @param options:
   *          sector - angle range which scanner is able to observe
   *          maxDistance - max distance which is possible to recognize
   *          size - physical radius
   */
  constructor(options, position, angle, base){
    super(position, angle, base);
    this.options = options;

    // detectors -- we approximate real sensor with ideal sensors with different angles
    this.detectors = [
      new IdealSensor({x:0, y:0}, -this.options.sector/2, this),
      new IdealSensor({x:0, y:0}, 0, this),
      new IdealSensor({x:0, y:0}, this.options.sector/2, this)
    ];

    // visibilityPoints -- border points which scanner is able to detect
    this.visibilityPoints = [
      new Point(0,0, this),
      new Point(this.options.maxDistance, 0, this.detectors[0]),
      new Point(this.options.maxDistance, 0, this.detectors[1]),
      new Point(this.options.maxDistance, 0, this.detectors[2]),
    ]
  }

  evaluate(obstacles) {
    var results = this.detectors.map(d => {
      var seen = d.evaluate(obstacles);
      if(seen == null) {
        return this.options.maxDistance;
      } else {
        return Math.min(seen.distance, this.options.maxDistance);
      }
    });

    return results.reduce((a,b) => a+b, 0) / results.length;
  }

  drawOn(ctx) {
    let absolutePos = this.absolutePosition;
    ctx.fillStyle = this.color || "rgb(0,0,255)";
    ctx.beginPath();
    ctx.arc(
      absolutePos.x,
      absolutePos.y,
      this.options.size,
      0,
      Math.PI*2,
      true);
    ctx.closePath();
    ctx.fill();
    drawPolygon(ctx, this.visibilityPoints, "rgba(255,0,0,0.5)");
    super.drawOn(ctx);
  }
}
