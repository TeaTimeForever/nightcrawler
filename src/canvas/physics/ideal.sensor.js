import { Body } from "./body";
import { cos, minus, sin } from "../utils/complex";

export class IdealSensor extends Body {

  doesSee(p1, p2){

    var relativeP1 = this.relative(p1),
        relativeP2 = this.relative(p2);

    if(relativeP1.y * relativeP2.y > 0) {
      return null;
    } else {
      let diff = minus(relativeP1, relativeP2);
      if(diff.y == 0) {
        return null;
      }
      let x = relativeP2.x - (diff.x/diff.y * relativeP2.y);
      if (x < 0 ) {
        return null; // object is behind sensor
      } else {
        return {
          distance: x,
          // looks crazy but..
          // just dont touch
          // pic.1
          cos: Math.abs(sin(diff))
        }
      }
    }
  }
}