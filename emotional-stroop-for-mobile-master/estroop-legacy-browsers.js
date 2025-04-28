/**************** 
 * Estroop *
 ****************/


// store info about the experiment session:
let expName = 'estroop';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '',
    'id': '',
    'group': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(startRoutineBegin());
flowScheduler.add(startRoutineEachFrame());
flowScheduler.add(startRoutineEnd());
const outer_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(outer_loopLoopBegin(outer_loopLoopScheduler));
flowScheduler.add(outer_loopLoopScheduler);
flowScheduler.add(outer_loopLoopEnd);







flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'estroop.xlsx', 'path': 'estroop.xlsx'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'cross_white.png', 'path': 'cross_white.png'},
    {'name': 'tick_white.png', 'path': 'tick_white.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var startClock;
var mouse;
var colours;
var buttonSize;
var buttonGap;
var buttonOffset;
var touchscreen;
var nBlocks;
var ivLevels;
var block_selection;
var weblink;
var thisIndex;
var block_results;
var showFeedback;
var instructions;
var rec;
var start_button;
var preBlockClock;
var stroopClock;
var fixation;
var stroop_text;
var Response;
var button1;
var button2;
var button3;
var button4;
var feedbackClock;
var image;
var button1_2;
var button2_2;
var button3_2;
var button4_2;
var postBlockClock;
var text_3;
var text_4;
var key_resp;
var rec_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "start"
  startClock = new util.Clock();
  mouse = new core.Mouse({
    win: psychoJS.window,
  });
  mouse.mouseClock = new util.Clock();
  // Run 'Begin Experiment' code from code
  colours = [["red", "d"], ["blue", "f"], ["yellow", "j"], ["green", "k"]];
  util.shuffle(colours);
  buttonSize = 0.2;
  buttonGap = 0.2;
  buttonOffset = 0.3;
  touchscreen = 0;
  nBlocks = 3;
  if ((expInfo["group"] === "1")) {
      ivLevels = ["Practice", "Neutral", "Negative", "Positive"];
      block_selection = [["45:75", "Positive", 2], ["75:105", "Negative", 3]];
  } else {
      ivLevels = ["Practice", "Neutral", "Positive", "Negative"];
      block_selection = [["75:105", "Negative", 3], ["45:75", "Positive", 2]];
  }
  block_selection.push(["15:45", "Neutral", 1]);
  block_selection.push(["0:15", "Practice", 0]);
  weblink = "https://brookeshls.co1.qualtrics.com/jfe/preview/SV_4GFvF9AAzBNbO5M?Q_CHL=preview&Q_SurveyVersionID=current&";
  nBlocks = 4;
  thisIndex = 0;
  block_results = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]];
  showFeedback = 1;
  weblink += ((((("participant=" + expInfo["participant"]) + "&id=") + expInfo["id"]) + "&researcher=") + expInfo["researcher"]);
  
  instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.04,  wrapWidth: 4, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  rec = new visual.Rect ({
    win: psychoJS.window, name: 'rec', 
    width: [0.5, 0.09][0], height: [0.5, 0.09][1],
    ori: 0, 
    pos: [0, (- 0.2)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([0.2, 0.2, 0.2]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -3, 
    interpolate: true, 
  });
  
  start_button = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_button',
    text: 'Start',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], draggable: false, height: 0.08,  wrapWidth: 2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "preBlock"
  preBlockClock = new util.Clock();
  // Initialize components for Routine "stroop"
  stroopClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.15,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  stroop_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'stroop_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.15,  wrapWidth: 2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  Response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  button1 = new visual.Polygon ({
    win: psychoJS.window, name: 'button1', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [((- buttonGap) + 0.1), (((- buttonOffset) + buttonGap) + 0.1)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color(colours[0][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -4, 
    interpolate: true, 
  });
  
  button2 = new visual.Polygon ({
    win: psychoJS.window, name: 'button2', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [buttonGap, ((- buttonOffset) + buttonGap)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color(colours[1][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -5, 
    interpolate: true, 
  });
  
  button3 = new visual.Polygon ({
    win: psychoJS.window, name: 'button3', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [(- buttonGap), ((- buttonOffset) - buttonGap)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color(colours[2][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -6, 
    interpolate: true, 
  });
  
  button4 = new visual.Polygon ({
    win: psychoJS.window, name: 'button4', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [buttonGap, ((- buttonOffset) - buttonGap)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color(colours[3][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -7, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  button1_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'button1_2', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [(- buttonGap), ((- buttonOffset) + buttonGap)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color(colours[0][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -1, 
    interpolate: true, 
  });
  
  button2_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'button2_2', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [buttonGap, ((- buttonOffset) + buttonGap)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color(colours[1][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -2, 
    interpolate: true, 
  });
  
  button3_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'button3_2', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [(- buttonGap), ((- buttonOffset) - buttonGap)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color(colours[2][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -3, 
    interpolate: true, 
  });
  
  button4_2 = new visual.Polygon ({
    win: psychoJS.window, name: 'button4_2', 
    edges: 72, size:buttonSize,
    ori: 0, 
    pos: [buttonGap, ((- buttonOffset) - buttonGap)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color(colours[3][0]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -4, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "postBlock"
  postBlockClock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: ' ',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.45)], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  rec_2 = new visual.Rect ({
    win: psychoJS.window, name: 'rec_2', 
    width: [0.5, 0.09][0], height: [0.5, 0.09][1],
    ori: 0, 
    pos: [0, (- 0.45)], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 5, 
    lineColor: new util.Color([1, 1, 1]), 
    fillColor: new util.Color([0.2, 0.2, 0.2]), 
    colorSpace: 'rgb', 
    opacity: 1, 
    depth: -4, 
    interpolate: true, 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var startMaxDurationReached;
var gotValidClick;
var mouserec;
var startMaxDuration;
var startComponents;
function startRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    startClock.reset();
    routineTimer.reset();
    startMaxDurationReached = false;
    // update component parameters for each repeat
    // setup some python lists for storing info about the mouse
    gotValidClick = false; // until a click is received
    // Run 'Begin Routine' code from code
    mouserec = mouse.getPos();
    instructions.text = "This experiment consists of a Stroop task.\n\nIn this task you will be presented with a series of words.\nEach screen will show a single word, these words will appear in different colours (green, yellow, blue and red).\nYour job is to indicate the colour that the word is printed in as quickly and as accurately as possible. \nClick the button on the screen that corresponds to that colour. \n\nTouch Start if you  understand the instructions and are ready to begin.";
    
    psychoJS.experiment.addData('start.started', globalClock.getTime());
    startMaxDuration = null
    // keep track of which components have finished
    startComponents = [];
    startComponents.push(mouse);
    startComponents.push(instructions);
    startComponents.push(rec);
    startComponents.push(start_button);
    
    startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var mouseloc;
function startRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start' ---
    // get current time
    t = startClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code
    mouseloc = mouse.getPos();
    if (((mouseloc[0] === mouserec[0]) && (mouseloc[1] === mouserec[1]))) {
    } else {
        if (rec.contains(mouse)) {
            touchscreen = 1;
            fixation.setPos([0, 0.3]);
            stroop_text.setPos([0, 0.3]);
            image.setPos([0, 0.3]);
            continueRoutine = false;
        }
    }
    
    
    // *instructions* updates
    if (t >= 0.0 && instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions.tStart = t;  // (not accounting for frame time here)
      instructions.frameNStart = frameN;  // exact frame index
      
      instructions.setAutoDraw(true);
    }
    
    
    // *rec* updates
    if (t >= 0.0 && rec.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec.tStart = t;  // (not accounting for frame time here)
      rec.frameNStart = frameN;  // exact frame index
      
      rec.setAutoDraw(true);
    }
    
    
    // *start_button* updates
    if (t >= 0.0 && start_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_button.tStart = t;  // (not accounting for frame time here)
      start_button.frameNStart = frameN;  // exact frame index
      
      start_button.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    startComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var _mouseButtons;
function startRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start' ---
    startComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('start.stopped', globalClock.getTime());
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = mouse.getPos();
    _mouseButtons = mouse.getPressed();
    psychoJS.experiment.addData('mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('mouse.rightButton', _mouseButtons[2]);
    // Run 'End Routine' code from code
    if ((touchscreen === 0)) {
        button1.setOpacity(0);
        button2.setOpacity(0);
        button3.setOpacity(0);
        button4.setOpacity(0);
        button1_2.setOpacity(0);
        button2_2.setOpacity(0);
        button3_2.setOpacity(0);
        button4_2.setOpacity(0);
        rec_2.setOpacity(0);
    }
    
    // the Routine "start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var outer_loop;
function outer_loopLoopBegin(outer_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    outer_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nBlocks, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'outer_loop'
    });
    psychoJS.experiment.addLoop(outer_loop); // add the loop to the experiment
    currentLoop = outer_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    outer_loop.forEach(function() {
      snapshot = outer_loop.getSnapshot();
    
      outer_loopLoopScheduler.add(importConditions(snapshot));
      outer_loopLoopScheduler.add(preBlockRoutineBegin(snapshot));
      outer_loopLoopScheduler.add(preBlockRoutineEachFrame());
      outer_loopLoopScheduler.add(preBlockRoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      outer_loopLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      outer_loopLoopScheduler.add(trialsLoopScheduler);
      outer_loopLoopScheduler.add(trialsLoopEnd);
      outer_loopLoopScheduler.add(postBlockRoutineBegin(snapshot));
      outer_loopLoopScheduler.add(postBlockRoutineEachFrame());
      outer_loopLoopScheduler.add(postBlockRoutineEnd(snapshot));
      outer_loopLoopScheduler.add(outer_loopLoopEndIteration(outer_loopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'estroop.xlsx', useRows),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(stroopRoutineBegin(snapshot));
      trialsLoopScheduler.add(stroopRoutineEachFrame());
      trialsLoopScheduler.add(stroopRoutineEnd(snapshot));
      trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(feedbackRoutineEachFrame());
      trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function outer_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(outer_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function outer_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var preBlockMaxDurationReached;
var thisBlock;
var useRows;
var rtList;
var useColours;
var preBlockMaxDuration;
var preBlockComponents;
function preBlockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'preBlock' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    preBlockClock.reset();
    routineTimer.reset();
    preBlockMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    thisBlock = block_selection.pop();
    useRows = thisBlock[0].toString();
    rtList = [];
    
    // Run 'Begin Routine' code from code_both2
    useColours =Array(10).fill([0,1,2,3]).flat();
    util.shuffle(useColours);
    
    psychoJS.experiment.addData('preBlock.started', globalClock.getTime());
    preBlockMaxDuration = null
    // keep track of which components have finished
    preBlockComponents = [];
    
    preBlockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function preBlockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'preBlock' ---
    // get current time
    t = preBlockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    preBlockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function preBlockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'preBlock' ---
    preBlockComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('preBlock.stopped', globalClock.getTime());
    // the Routine "preBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stroopMaxDurationReached;
var thisColour;
var response;
var Score;
var butcol1;
var butcol2;
var butcol3;
var butcol4;
var _Response_allKeys;
var stroopMaxDuration;
var stroopComponents;
function stroopRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stroop' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    stroopClock.reset();
    routineTimer.reset();
    stroopMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from stroop_code
    thisColour = useColours.pop();
    psychoJS.experiment.addData("Colour", colours[thisColour][0]);
    psychoJS.experiment.addData("Answer", colours[thisColour][1]);
    response = 99;
    Score = 0;
    butcol1 = "white";
    butcol2 = "white";
    butcol3 = "white";
    butcol4 = "white";
    
    stroop_text.setColor(new util.Color(colours[thisColour][0]));
    stroop_text.setText(Word);
    Response.keys = undefined;
    Response.rt = undefined;
    _Response_allKeys = [];
    psychoJS.experiment.addData('stroop.started', globalClock.getTime());
    stroopMaxDuration = null
    // keep track of which components have finished
    stroopComponents = [];
    stroopComponents.push(fixation);
    stroopComponents.push(stroop_text);
    stroopComponents.push(Response);
    stroopComponents.push(button1);
    stroopComponents.push(button2);
    stroopComponents.push(button3);
    stroopComponents.push(button4);
    
    stroopComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function stroopRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stroop' ---
    // get current time
    t = stroopClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }
    
    frameRemains = 0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from stroop_code
    if ((t < 0.5)) {
        mouserec = mouse.getPos();
    } else {
        mouseloc = mouse.getPos();
        if (((mouseloc[0] === mouserec[0]) && (mouseloc[1] === mouserec[1]))) {
        } else {
            if (button1.contains(mouse)) {
                response = 0;
                butcol1 = "yellow";
            } else {
                if (button2.contains(mouse)) {
                    response = 1;
                    butcol2 = "yellow";
                } else {
                    if (button3.contains(mouse)) {
                        response = 2;
                        butcol3 = "yellow";
                    } else {
                        if (button4.contains(mouse)) {
                            response = 3;
                            butcol4 = "yellow";
                        }
                    }
                }
            }
        }
        if ((response < 99)) {
            if ((response === thisColour)) {
                Score = 1;
            }
            continueRoutine = false;
        }
    }
    
    
    // *stroop_text* updates
    if (t >= 0.5 && stroop_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stroop_text.tStart = t;  // (not accounting for frame time here)
      stroop_text.frameNStart = frameN;  // exact frame index
      
      stroop_text.setAutoDraw(true);
    }
    
    
    // *Response* updates
    if (t >= 0.5 && Response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Response.tStart = t;  // (not accounting for frame time here)
      Response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Response.clearEvents(); });
    }
    
    if (Response.status === PsychoJS.Status.STARTED) {
      let theseKeys = Response.getKeys({keyList: ['d', 'f', 'j', 'k'], waitRelease: false});
      _Response_allKeys = _Response_allKeys.concat(theseKeys);
      if (_Response_allKeys.length > 0) {
        Response.keys = _Response_allKeys[_Response_allKeys.length - 1].name;  // just the last key pressed
        Response.rt = _Response_allKeys[_Response_allKeys.length - 1].rt;
        Response.duration = _Response_allKeys[_Response_allKeys.length - 1].duration;
        // was this correct?
        if (Response.keys == colours[0][1]) {
            Response.corr = 1;
        } else {
            Response.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *button1* updates
    if (t >= 0.0 && button1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button1.tStart = t;  // (not accounting for frame time here)
      button1.frameNStart = frameN;  // exact frame index
      
      button1.setAutoDraw(true);
    }
    
    
    // *button2* updates
    if (t >= 0.0 && button2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button2.tStart = t;  // (not accounting for frame time here)
      button2.frameNStart = frameN;  // exact frame index
      
      button2.setAutoDraw(true);
    }
    
    
    // *button3* updates
    if (t >= 0.0 && button3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button3.tStart = t;  // (not accounting for frame time here)
      button3.frameNStart = frameN;  // exact frame index
      
      button3.setAutoDraw(true);
    }
    
    
    // *button4* updates
    if (t >= 0.0 && button4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button4.tStart = t;  // (not accounting for frame time here)
      button4.frameNStart = frameN;  // exact frame index
      
      button4.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stroopComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var feedbackImage;
function stroopRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stroop' ---
    stroopComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('stroop.stopped', globalClock.getTime());
    // Run 'End Routine' code from stroop_code
    block_results[thisBlock[2]][0] += 1;
    if (((Response.corr === 1) || (Score === 1))) {
        block_results[thisBlock[2]][1] += 1;
        rtList.push((Math.round((t * 1000)) - 500));
        feedbackImage = "tick_white.png";
    } else {
        feedbackImage = "cross_white.png";
    }
    if ((thisBlock[2] > 0)) {
        showFeedback = 0;
    }
    
    // was no response the correct answer?!
    if (Response.keys === undefined) {
      if (['None','none',undefined].includes(colours[0][1])) {
         Response.corr = 1;  // correct non-response
      } else {
         Response.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Response.corr, level);
    }
    psychoJS.experiment.addData('Response.keys', Response.keys);
    psychoJS.experiment.addData('Response.corr', Response.corr);
    if (typeof Response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Response.rt', Response.rt);
        psychoJS.experiment.addData('Response.duration', Response.duration);
        routineTimer.reset();
        }
    
    Response.stop();
    // the Routine "stroop" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedbackMaxDurationReached;
var feedbackMaxDuration;
var feedbackComponents;
function feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedbackClock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    image.setOpacity(showFeedback);
    image.setImage(feedbackImage);
    button1_2.setLineColor(new util.Color(butcol1));
    button2_2.setLineColor(new util.Color(butcol2));
    button3_2.setLineColor(new util.Color(butcol3));
    button4_2.setLineColor(new util.Color(butcol4));
    psychoJS.experiment.addData('feedback.started', globalClock.getTime());
    feedbackMaxDuration = null
    // keep track of which components have finished
    feedbackComponents = [];
    feedbackComponents.push(image);
    feedbackComponents.push(button1_2);
    feedbackComponents.push(button2_2);
    feedbackComponents.push(button3_2);
    feedbackComponents.push(button4_2);
    
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback' ---
    // get current time
    t = feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    
    // *button1_2* updates
    if (t >= 0.0 && button1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button1_2.tStart = t;  // (not accounting for frame time here)
      button1_2.frameNStart = frameN;  // exact frame index
      
      button1_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (button1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button1_2.setAutoDraw(false);
    }
    
    
    // *button2_2* updates
    if (t >= 0.0 && button2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button2_2.tStart = t;  // (not accounting for frame time here)
      button2_2.frameNStart = frameN;  // exact frame index
      
      button2_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (button2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button2_2.setAutoDraw(false);
    }
    
    
    // *button3_2* updates
    if (t >= 0.0 && button3_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button3_2.tStart = t;  // (not accounting for frame time here)
      button3_2.frameNStart = frameN;  // exact frame index
      
      button3_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (button3_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button3_2.setAutoDraw(false);
    }
    
    
    // *button4_2* updates
    if (t >= 0.0 && button4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      button4_2.tStart = t;  // (not accounting for frame time here)
      button4_2.frameNStart = frameN;  // exact frame index
      
      button4_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (button4_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      button4_2.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback' ---
    feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
    if (feedbackMaxDurationReached) {
        feedbackClock.add(feedbackMaxDuration);
    } else {
        feedbackClock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var postBlockMaxDurationReached;
var rtMid;
var waitTime;
var pressSpace;
var _key_resp_allKeys;
var postBlockMaxDuration;
var postBlockComponents;
function postBlockRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'postBlock' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    postBlockClock.reset();
    routineTimer.reset();
    postBlockMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_3
    util.sort(rtList);
    rtMid = ((rtList.length + 1) / 2);
    if ((rtMid === Math.round(rtMid))) {
        block_results[thisBlock[2]][2] = rtList[Number.parseInt(rtMid)];
    } else {
        block_results[thisBlock[2]][2] = ((rtList[Number.parseInt((rtMid - 0.5))] + rtList[Number.parseInt((rtMid + 0.5))]) / 2);
    }
    if ((thisBlock[2] === 0)) {
        text_3.text = ((("That was the end of the practice trials.\n\nYou scored " + block_results[thisBlock[2]][1].toString()) + " out of ") + block_results[thisBlock[2]][0].toString());
        text_4.text = "Please wait for 10 seconds before starting the first block";
        waitTime = 10;
    } else {
        if ((thisBlock[2] === 1)) {
            text_3.text = "That was the end of the first block.";
            text_4.text = "Please wait for 30 seconds before starting the second block";
            waitTime = 30;
        } else {
            if (((thisBlock[2] === 2) && (nBlocks === 4))) {
                text_3.text = "That was the end of the second block.";
                text_4.text = "Please wait for 30 seconds before starting the third block";
                waitTime = 30;
            } else {
                text_3.text = "Thank you for taking part.";
                text_4.text = "Please submit your data and then wait for the green \"Thank you for your patience\" message.";
                waitTime = 2;
            }
        }
    }
    pressSpace = 0;
    
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('postBlock.started', globalClock.getTime());
    postBlockMaxDuration = null
    // keep track of which components have finished
    postBlockComponents = [];
    postBlockComponents.push(text_3);
    postBlockComponents.push(text_4);
    postBlockComponents.push(key_resp);
    postBlockComponents.push(rec_2);
    
    postBlockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function postBlockRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'postBlock' ---
    // get current time
    t = postBlockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_3
    if (((t > waitTime) && (pressSpace === 0))) {
        if ((touchscreen === 1)) {
            text_4.text = "Continue";
            mouserec = mouse.getPos();
        } else {
            text_4.text = "Press space to continue";
        }
        pressSpace = 1;
    } else {
        if (((pressSpace === 1) && (touchscreen === 1))) {
            mouseloc = mouse.getPos();
            if (((mouseloc[0] === mouserec[0]) && (mouseloc[1] === mouserec[1]))) {
            } else {
                if (rec_2.contains(mouse)) {
                    continueRoutine = false;
                }
            }
        }
    }
    
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= waitTime && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *rec_2* updates
    if (t >= waitTime && rec_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rec_2.tStart = t;  // (not accounting for frame time here)
      rec_2.frameNStart = frameN;  // exact frame index
      
      rec_2.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    postBlockComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function postBlockRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'postBlock' ---
    postBlockComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('postBlock.stopped', globalClock.getTime());
    key_resp.stop();
    // the Routine "postBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
