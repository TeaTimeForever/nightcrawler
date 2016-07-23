import { Body } from "./body";
import { IdealSensor } from "./ideal.sensor";

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
      new IdealSensor({x:0, y:0}, -angle/2, this),
      new IdealSensor({x:0, y:0}, 0, this),
      new IdealSensor({x:0, y:0}, angle/2, this)
    ];
  }
}
