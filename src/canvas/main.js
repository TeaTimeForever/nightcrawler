/**
 * Created by eq on 22/07/16.
 */
import { Canvas } from "./utils/canvas"

var canvas = new Canvas("canvas");
canvas.initWalls();
canvas.generateObstacles(20);
canvas.start();
