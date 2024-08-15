from flask import Flask, render_template
from flask import  request, jsonify
from flask_socketio import SocketIO, emit
import random
##
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
project_name=""
DUT_Name=""
Cycle_Name=""
speed = 0
torque = 0
status = 'Stopped'
sendData={}

# Route to get current data
@app.route('/get_data', methods=['GET'])
def get_data():
    global speed, torque, status,project_name,DUT_Name,Cycle_Name,sendData
    #return jsonify({'Project_Name': project_name, 'DUT_Name': DUT_Name, 'Cycle_Name': Cycle_Name,'speed': speed, 'torque': torque, 'status': status})
    return jsonify(sendData)


# Simulate sensor data
def generate_sensor_data():
    temperature = round(random.uniform(20, 30), 2)
    humidity = round(random.uniform(40, 60), 2)
    light_intensity = random.randint(0, 100)
    return {'temperature': temperature, 'humidity': humidity, 'light_intensity': light_intensity}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_data', methods=['POST'])
def set_data():
    global speed, torque, status,project_name,DUT_Name,Cycle_Name,sendData
    data = request.json
    print('Received data:', data)
    sendData = data
    
    project_name = data['Project_Name']
    DUT_Name = data['DUT_Name']
    Cycle_Name=data['Cycle_Name']
    
    speed = data['speed']
    torque = data['torque']
    status = data['status']
    #emit('update_sensor_data',data)
    # Process the data here
    #return jsonify({'message': 'Data received successfully'})
    
    if status == "Fault":
        print("fault")
    
        send_email('Fault in Transmission TestRig ', 'Fault Alert Testing', 'navaneeth.ats@gmail.com')

    return jsonify(data)

def send_email(subject, message, to_email):
    # Email configuration
    sender_email = 'navaneethan@ats-india.com'
    sender_password = '$Nv@202ats$'
    smtp_server = 'smtp3.netcore.co.in'
    smtp_port = 587  # For TLS

    # Create a MIMEText object for the email content
    email_body = MIMEText(message, 'plain')

    # Create a MIMEMultipart object and attach the email content
    email = MIMEMultipart()
    email['From'] = 'navaneethan@ats-india.com'
    email['To'] = to_email
    email['Subject'] = subject
    email.attach(email_body)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, email.as_string())





    
   

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    # Send initial sensor data when client connects
    #emit('update_sensor_data', generate_sensor_data())

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=4000)
