export function drawPolygon(ctx, points, color) {
  ctx.fillStyle = color || "#000";
  ctx.beginPath();
  points.forEach((p, index) => {
    let pencil = (index == 0)? ctx.moveTo : ctx.lineTo;
    let absolutePos = p.absolutePosition;
    pencil.call(ctx, absolutePos.x, absolutePos.y);
  });
  ctx.closePath();
  ctx.fill();
}