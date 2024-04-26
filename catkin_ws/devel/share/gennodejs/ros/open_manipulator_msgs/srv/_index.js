
"use strict";

let SetJointPosition = require('./SetJointPosition.js')
let SetDrawingTrajectory = require('./SetDrawingTrajectory.js')
let GetJointPosition = require('./GetJointPosition.js')
let SetActuatorState = require('./SetActuatorState.js')
let GetKinematicsPose = require('./GetKinematicsPose.js')
let SetKinematicsPose = require('./SetKinematicsPose.js')

module.exports = {
  SetJointPosition: SetJointPosition,
  SetDrawingTrajectory: SetDrawingTrajectory,
  GetJointPosition: GetJointPosition,
  SetActuatorState: SetActuatorState,
  GetKinematicsPose: GetKinematicsPose,
  SetKinematicsPose: SetKinematicsPose,
};
