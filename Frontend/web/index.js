

eel.expose(say_hello_js);               // Expose this function to Python
function say_hello_js(x) {
    console.log("Hello from " + x);
}

function hello_python(){
    eel.say_hello_py("Javascript World!");  // Call a Python function
}