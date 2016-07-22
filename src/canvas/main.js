/**
 * Created by eq on 22/07/16.
 */
import { Canvas } from "./lib/canvas"

var canvas = new Canvas("canvas");
canvas.initWalls();
canvas.generatObstacles(20);
