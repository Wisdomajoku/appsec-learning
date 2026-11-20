#!/usr/bin/env node
/**
 * Day 7 Lab: JavaScript Runtime Mechanics & Security Quirks
 * Demonstrating type coercion, loose vs strict equality,
 * truthiness evaluation, prototype inheritance, and async error shielding.
 */

function runTypeJugglingExperiments() {
    console.log("=" .repeat(65));
    console.log("EXPERIMENT 1: LOOSE EQUALITY (==) VS STRICT EQUALITY (===)");
    console.log("=" .repeat(65));

    // Case A: Loose equality coerces types automatically
    const comparison1 = (0 == "");         // true! (Empty string converts to 0)
    const comparison2 = (0 == "0");        // true! (String "0" converts to number 0)
    const comparison3 = (false == "0");    // true! (Boolean false converts to 0)
    const comparison4 = (null == undefined);// true!

    console.log(`0 == ""          evaluates to: ${comparison1}`);
    console.log(`0 == "0"         evaluates to: ${comparison2}`);
    console.log(`false == "0"     evaluates to: ${comparison3}`);
    console.log(`null == undefined evaluates to: ${comparison4}`);

    // The Authentication Flaw Scenario:
    // Imagine an API secret check using loose equality:
    const storedSecretToken = "0"; // Stored in config
    const attackerInput = 0;       // Attacker submits raw JSON number 0

    if (attackerInput == storedSecretToken) {
        console.log("\n[!] SECURITY BYPASS: attackerInput (0) == storedSecretToken ('0') is TRUE!");
    }

    // The Fix: Strict Equality (===) checks BOTH type and value
    const strictCheck = (attackerInput === storedSecretToken);
    console.log(`[+] Strict Check: attackerInput === storedSecretToken is: ${strictCheck} (Blocked!)`);
}

function runTruthinessExperiments() {
    console.log("\n" + "=" .repeat(65));
    console.log("EXPERIMENT 2: JAVASCRIPT TRUTHINESS (VS PYTHON DAY 1)");
    console.log("=" .repeat(65));

    // Notice the critical differences from Python:
    const emptyString = "";
    const emptyArray = [];
    const emptyObject = {};
    const stringFalse = "false";

    console.log(`Boolean("")      (Empty string): ${Boolean(emptyString)}`);
    console.log(`Boolean("false") (String 'false'): ${Boolean(stringFalse)}`);
    
    // CRITICAL PYTHON VS JS DIFFERENCE:
    // In Python: bool([]) is False.
    // In JavaScript: Boolean([]) is TRUE!
    console.log(`Boolean([])      (Empty array) : ${Boolean(emptyArray)}  <-- (In Python this was FALSE!)`);
    console.log(`Boolean({})      (Empty object): ${Boolean(emptyObject)} <-- (In Python this was FALSE!)`);

    // The Flaw:
    // If a developer writes `if (req.body.items)` assuming it checks for contents:
    const userPayload = [];
    if (userPayload) {
        console.log("[!] TRUTHINESS TRAP: An empty array [] evaluates to TRUE in JavaScript!");
    }
}

function runPrototypeInspection() {
    console.log("\n" + "=" .repeat(65));
    console.log("EXPERIMENT 3: THE PROTOTYPE CHAIN (INSPECTION)");
    console.log("=" .repeat(65));

    // Create a plain object with no custom properties
    const blankObject = {};

    console.log("Keys on blankObject:", Object.keys(blankObject)); // []
    console.log("Does toString exist on blankObject?", typeof blankObject.toString); // function!
    console.log("Where did toString come from?");
    console.log("--> Object.getPrototypeOf(blankObject) === Object.prototype:", 
        Object.getPrototypeOf(blankObject) === Object.prototype);

    console.log("\nAppSec Lesson: In JavaScript, objects are linked to prototypes.");
    console.log("Polluting Object.prototype affects every object in the application.");
}

async function runAsyncSafetyDemo() {
    console.log("\n" + "=" .repeat(65));
    console.log("EXPERIMENT 4: ASYNC EXECUTION & ERROR SHIELDING");
    console.log("=" .repeat(65));

    // Simulated async database query that fails
    const mockFailingDatabaseQuery = () => {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                reject(new Error("Database connection dropped"));
            }, 100);
        });
    };

    // Safe pattern: Wrapping await in try/catch to shield the single thread
    try {
        console.log("[*] Dispatching asynchronous database query...");
        await mockFailingDatabaseQuery();
    } catch (err) {
        console.log(`[+] CAUGHT EXCEPTION DEFENSIVELY: ${err.message}`);
        console.log("[+] The Node.js event loop remains healthy and running.");
    }
}

// Main execution controller
async function main() {
    runTypeJugglingExperiments();
    runTruthinessExperiments();
    runPrototypeInspection();
    await runAsyncSafetyDemo();
    console.log("\n" + "=" .repeat(65));
    console.log("ALL EXPERIMENTS COMPLETED SUCCESSFULLY");
    console.log("=" .repeat(65));
}

main();
