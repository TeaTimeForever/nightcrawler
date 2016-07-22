export const plus = (a, b) => {
  return {
    x: a.x + b.x,
    y: a.y + b.y
  }
};

export const minus = (a, b) => {
  return {
    x: a.x - b.x,
    y: a.y - b.y
  }
};

/** multiply
 (a.x + i * a.y) * (b.x + i * b.y)
 = a.x * b.x -
 a.y * b.y +
 i * a.y * b.x +
 i * a.x  * b.y
*/
export const mul = (a, b) => {
  return {
    x: a.x * b.x - a.y * b.y,
    y: a.y * b.x + a.x * b.y
  }
};

/**
 * abs^2
 */
export const abs2 = (p) => {
  return p.x * p.x + p.y * p.y;
};

/**
 * abs
 */
export const abs = (p) => {
  return Math.sqrt(abs2(p));
};

/**
 * invert
 * 1 / p
 * should be: p * inv(p) =  {x: 1, y: 0}
 */
export const inv = (p) => {
  let r2 = abs2(p);
  return {
    x: p.x / r2,
    y: -p.y / r2
  }
};

/**
 * division
 */
export const div = (a, b) => {
  return mul(a, inv(b));
};

export const sin = (p) => {
  return p.y / abs(p);
};

export const cos = (p) => {
  return p.x / abs(p);
};

/**
 * complex number with r = 1 and given angle
 */
export const rotor = (angle) => {
  return {
    x: Math.cos(angle),
    y: Math.sin(angle)
  }
};