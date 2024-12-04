var index = 0; // Tracks the current program being shown
var loopTimeout; // Stores the timeout ID for the auto-loop
var programs = []; // Array to store loaded programs


/**
 * Handles the output of the Skulpt interpreter
 * @param {string} text - Output text from the program
 */
function outf(text) {
    console.log('Output:', text); // Log the program's output to the console
}


function builtinRead(file) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][file] === undefined) {
        throw new Error("File not found: '" + file + "'");
    }
    return Sk.builtinFiles["files"][file];
}


/**
 * Runs a Skulpt program
 * @param {Object} program - Contains the program name and code
 */
function runProgram(program) {
    console.log('Running program:', program.name); // Debug: program being executed


    Sk.configure({
        output: outf, // Your output function
        read: builtinRead, // Your read function
        __future__: Sk.python3, // Use Python 3 if needed
        syspaths: ['src/lib'], // Add this line to include the path to turtle.js
    });

    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    

    if (Sk.builtinFiles.files["src/lib/turtle.js"]) {
        console.log("turtle.js is loaded.");
    } else {
        console.error("turtle.js is not loaded.");
    }
    


    
    var myPromise = Sk.misceval.asyncToPromise(function() {
        return Sk.importMainWithBody("<stdin>", false, program.code, true);
    });


    myPromise.then(function(mod) {
        console.log('Successfully ran program:', program.name); // Debug success
    }, function(err) {
        console.error('Error in program:', program.name, 'Error:', err.toString()); // Debug error
    });
}


/**
 * Clears the turtle canvas
 */
function clearCanvas() {
    console.log('Clearing canvas'); // Debug: canvas cleared
    var canvas = document.getElementById('turtleCanvas');
    var ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function resetCanvas() {
    const canvasContainer = document.getElementById('turtleCanvas');
    while (canvasContainer.firstChild) {
        canvasContainer.removeChild(canvasContainer.firstChild);
    }
}




/**
 * Displays the current program on the canvas
 */
function showProgram() {
    if (programs.length === 0) {
        console.error('No programs to display.'); // Debug: no programs
        return;
    }
    console.log('Showing program index:', index); // Debug: current program index
    clearCanvas();
    resetCanvas();
    var program = programs[index];
    document.getElementById('studentName').innerText = 'Program by: ' + program.name; // Show program author
    runProgram(program);
}


/**
 * Moves to the next program
 */
function nextProgram() {
    index = (index + 1) % programs.length;
    console.log('Next program index:', index); // Debug: next program index
    showProgram();
}


/**
 * Moves to the previous program
 */
function prevProgram() {
    index = (index - 1 + programs.length) % programs.length;
    console.log('Previous program index:', index); // Debug: previous program index
    showProgram();
}


/**
 * Automatically loops through programs
 */
function autoLoopPrograms() {
    console.log('Starting auto-loop'); // Debug: auto-loop started
    showProgram();
    loopTimeout = setTimeout(function() {
        nextProgram();
        autoLoopPrograms();
    }, 10000); // Change every 10 seconds
}

function debugCanvas(){
    const canvas = document.getElementById('turtleCanvas');
    const ctx = canvas.getContext('2d');
    ctx.fillStyle = 'blue';
    ctx.fillRect(10, 10, 50, 50); // Draw a small blue square

}


/**
 * Loads programs from 'students.json'
 */
function loadPrograms() {
    console.log('Loading programs...'); // Debug: loading programs
    fetch('students.json')
        .then(response => {
            console.log('Fetched students.json'); // Debug: file fetched
            return response.json();
        })
        .then(data => {
            let promises = data.map(student => {
                console.log('Fetching code for:', student.name); // Debug: fetching student code
                return fetch(student.codeFile)
                    .then(response => response.text())
                    .then(code => {
                        console.log('Loaded code for:', student.name); // Debug: code loaded
                        programs.push({
                            name: student.name,
                            code: code
                        });
                    });
            });
            return Promise.all(promises);
        })
        .then(() => {
            console.log('All programs loaded:', programs); // Debug: all programs loaded
            if (programs.length > 0) {
                autoLoopPrograms(); // Start auto-loop if programs are loaded
            } else {
                console.error('No programs loaded.'); // Debug: no programs
            }
        })
        .catch(err => {
            console.error('Error loading programs:', err); // Debug: error loading programs
        });
}


/**
 * Initializes the application
 */
window.onload = function() {
    console.log('Initializing application...'); // Debug: application initializing
    document.getElementById('nextBtn').addEventListener('click', function() {
        console.log('Next button clicked'); // Debug: next button clicked
        clearTimeout(loopTimeout);
        nextProgram();
    });


    document.getElementById('prevBtn').addEventListener('click', function() {
        console.log('Previous button clicked'); // Debug: previous button clicked
        clearTimeout(loopTimeout);
        prevProgram();
    });


    loadPrograms(); // Load student programs on page load
};
