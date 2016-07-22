import { rotor } from '../utils/complex';

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
};