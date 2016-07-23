import {rotor, mul, plus } from "../utils/complex";

const space = {
  absoluteRotor: rotor(0),
  absolutePosition: {x: 0, y: 0}
};

export class Body {

  /**
   * position -- object coordinates in base coordinate system (relative to base object)
   * angle    -- relative angle (to base)
   * base     -- base object
   */
  constructor(position, angle, base) {
    this.rotor = rotor(angle || 0);
    this.position = position || {x: 0, y: 0};
    this.base = base || space;
  };

  get absoluteRotor() {
    return mul(this.base.absoluteRotor, this.rotor);
  }

  get absolutePosition() {
    return plus(this.base.absolutePosition, mul(this.position, this.base.absoluteRotor));
  }

  rotate(angle){
    this.rotor = mul(this.rotor, rotor(angle));
  }

  makeStep(distance){
    this.position = plus(this.position, mul(this.rotor, {x: distance, y: 0}));
  }

  relative(body){
    return div(minus(body.absolutePosition, this.absolutePosition), this.absoluteRotor);
  }
};