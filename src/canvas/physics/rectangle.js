import { Body } from "./body";
import { Point } from "./point";
import { drawPolygon } from "../utils/graphics";

export class Rectangle extends Body {

  constructor(size, position, angle, base) {
    super(position, angle, base);

    var xOffset = size.width/2,
        yOffset = size.height/2;

    this.corners = [
      new Point(-xOffset, -yOffset, this),
      new Point(xOffset, -yOffset, this),
      new Point(xOffset, yOffset, this),
      new Point(-xOffset, yOffset, this)
    ];
  }

  drawOn(ctx) {
    drawPolygon(ctx, this.corners, this.color);
    super.drawOn(ctx);
  }

  getEdges(){
    return [[
      this.corners[0], this.corners[1]
    ],[
      this.corners[1], this.corners[2]
    ],[
      this.corners[2], this.corners[3]
    ],[
      this.corners[3], this.corners[0]
    ]];
  }
}