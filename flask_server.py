import os
import signal
import subprocess
import image_utils
from flask import Flask, jsonify, request, redirect, render_template

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

state = {
    "process": None
}

def save_and_show_image(file): # test
    img = image_utils.load_image_file(file)
    image_utils.resize_and_crop_and_save(img, 'test.ppm', (32, 32))
    if state["process"]:
        os.killpg(os.getpgid(state["process"].pid), signal.SIGTERM)  # Send the signal to all the process groups
    state["process"] = subprocess.Popen(["sudo", "./rpi-rgb-led-matrix/examples-api-use/demo", "-D", "1", "-m", "1000", "test.ppm"], stdout=subprocess.PIPE, 
                       shell=False, preexec_fn=os.setsid)
    return "Showing the img!"

@app.route('/img', methods=['GET', 'POST'])
def upload_image():
    # Check if a valid image file was uploaded
    print(request.content_type)
    print(request.files)
    print(request.content_length)
    print(request.form)

    if request.method == 'POST':
        if 'file' not in request.files and 'file' not in request.form:
            return redirect(request.url)

        if 'file' in request.files:
            print(f"The file is {request.files['file'].filename}")

            file = request.files['file']
        else:
            file = request.form['file']

        if file.filename == '':
            print("Empty file")
            return redirect(request.url)

        if file and allowed_file(file.filename):
            # The image file seems valid! Detect faces and return the result.
            return save_and_show_image(file)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/irRemote')
def ir_mode():
    # subprocess.Popen(["rm","-r","some.file"])
    state["process"] = subprocess.Popen(["python", "IR-Remote-Receiver-Python-Module/IR_Mode.py"], stdout=subprocess.PIPE, 
                       shell=False, preexec_fn=os.setsid)
    return "irRemote"

@app.route('/photoSensor')
def photoSensor_mode():
    state["process"] = subprocess.Popen(["python", "light-sensor.py"], stdout=subprocess.PIPE, 
                       shell=False, preexec_fn=os.setsid)
    return "Yes, turn it on!"

@app.route('/demoScroll', methods=['GET', 'POST'])
def play_demo():
    if state["process"]:
        os.killpg(os.getpgid(state["process"].pid), signal.SIGTERM)  # Send the signal to all the process groups
    demoNumber = request.args.get('demoNumber')
    state["process"] = subprocess.Popen(["sudo", "./rpi-rgb-led-matrix/examples-api-use/demo", "-D", demoNumber], stdout=subprocess.PIPE, 
                       shell=False, preexec_fn=os.setsid)
    return demoNumber

@app.route('/')
def turn_on():
    state["process"] = subprocess.Popen(["sudo", "./rpi-rgb-led-matrix/examples-api-use/demo", "-D", "6"], stdout=subprocess.PIPE, 
                       shell=False, preexec_fn=os.setsid)
    return "Yes, turn it on!"

@app.route('/kill')
def turn_off():
    if state["process"]:
        os.killpg(os.getpgid(state["process"].pid), signal.SIGTERM)  # Send the signal to all the process groups
    return "Killed it!"

@app.route('/killAll')
def kill_everything():
    os.system("sudo killall demo")

@app.route('/webApp')
def webApp():
    return render_template("webApp.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')