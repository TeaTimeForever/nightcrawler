/**
 * Created by eq on 22/07/16.
 */
import { Canvas } from "./utils/canvas"
import { IdealSensor } from "./physics/ideal.sensor";
import { Point } from "./physics/point";

var canvas = new Canvas("canvas");
canvas.initWalls();
canvas.generateObstacles(20);
canvas.start();




//tests:
var sensor = new IdealSensor();
var p1 = new Point(5, -1),
    p2 = new Point(5, 1);

console.log("sensor test: (expect: distance 5, cos 1)", sensor.doesSee(p1,p2));
sensor.rotate(0.01);
console.log("sensor test: (expect: distance ~5, cos ~1)", sensor.doesSee(p1,p2));
sensor.rotate(0.3);
console.log("sensor test: (should not see )", sensor.doesSee(p1,p2));
