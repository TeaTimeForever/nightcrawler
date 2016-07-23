import { Body } from "./body";
import { Point } from "./point";

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
    ctx.fillStyle = this.color || "#000";
    ctx.beginPath();
    this.corners.forEach((p, index) => {
      let pencil = (index == 0)? ctx.moveTo : ctx.lineTo;
      let absolutePos = p.absolutePosition;
      pencil.call(ctx, absolutePos.x, absolutePos.y);
    });
    ctx.closePath();
    ctx.fill();
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