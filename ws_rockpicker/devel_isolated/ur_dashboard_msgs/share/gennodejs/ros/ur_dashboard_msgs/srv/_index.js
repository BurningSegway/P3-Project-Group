
"use strict";

let GetProgramState = require('./GetProgramState.js')
let GetRobotMode = require('./GetRobotMode.js')
let AddToLog = require('./AddToLog.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')
let RawRequest = require('./RawRequest.js')
let Load = require('./Load.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let Popup = require('./Popup.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let IsProgramRunning = require('./IsProgramRunning.js')

module.exports = {
  GetProgramState: GetProgramState,
  GetRobotMode: GetRobotMode,
  AddToLog: AddToLog,
  IsInRemoteControl: IsInRemoteControl,
  RawRequest: RawRequest,
  Load: Load,
  IsProgramSaved: IsProgramSaved,
  Popup: Popup,
  GetSafetyMode: GetSafetyMode,
  GetLoadedProgram: GetLoadedProgram,
  IsProgramRunning: IsProgramRunning,
};
