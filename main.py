import eel

# Set web files folder
eel.init("./Frontend/web")


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print("Hello from %s" % x)


eel.say_hello_js("Python World!")  # Call a Javascript function

eel.start("index.html")  # Start
