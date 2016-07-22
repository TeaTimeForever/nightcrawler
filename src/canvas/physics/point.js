import { Body } from "./body";

export class Point extends Body {
  constructor(x, y, base){
    super({x,y}, 0, base);
  }
}
