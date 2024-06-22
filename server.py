from flask import Flask, request, jsonify, render_template
import exec_rpi_command
import os
import datetime
import config
import cloudutils
import rpiInterface
import validator

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/forms')
def forms():
    return render_template('forms-elements.html')

# Endpoint to create a new guide
@app.route('/start-session', methods=["POST"])
def start_data_collection_sesssion():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    session_name = request.json['session_name'] 

    session_folder_path = config.PI_IMAGES_DIR + "/" + config.CURRENT_TERM + "/" + current_date
    print(session_folder_path)
    exec_rpi_command.ssh_execute("mkdir " + session_folder_path)

    session_folder_path += "/" + session_name
    print(session_folder_path)
    exec_rpi_command.ssh_execute("mkdir " + session_folder_path)

    return jsonify({'message': 'Post created successfully'}), 201

@app.route('/end-session', methods=["POST"])
def end_session():
    print("ending session")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    session_name = request.json['session_name']
    rpi_session_folder_path = rpiInterface.get_rpi_local_image_dir_with_date() + "/" + session_name

    local_session_folder_path = config.LOCAL_IMAGES_DIR + "/" + config.CURRENT_TERM 
    if not os.path.exists(local_session_folder_path):
        os.mkdir(local_session_folder_path)

    
    local_session_folder_path +=  "/" + current_date 
    if not os.path.exists(local_session_folder_path):
        os.mkdir(local_session_folder_path)

    local_session_folder_path += "/" + session_name
    if not os.path.exists(local_session_folder_path):
        os.mkdir(local_session_folder_path)

    os.system("scp -r " + config.RPI_USER + "@" + config.RPI_IP + ":" + rpi_session_folder_path + " " + local_session_folder_path)
    return jsonify({'message': 'Post created successfully'}), 201

# Endpoint to create a new guide
@app.route('/validate-session', methods=["POST"])
def validate_session():
    session_name = request.json['session_name']
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    local_session_folder_path = config.LOCAL_IMAGES_DIR + "/" + config.CURRENT_TERM + "/" + current_date + "/" + session_name
    metadata_url = request.json["metadata_url"]
    local_metadata_download_path = config.LOCAL_METADATA_DIR + "/" + session_name + ".xlsx"
    # cloudutils.download_files_from_folder(metadata_url, local_metadata_download_path)

    # count number of samples
    # compare count
    return jsonify({'message': 'Post created successfully'}), 201

# Endpoint to create a new guide
@app.route('/submit-ticket', methods=["POST"])
def submit_ticket():
    session_name = request.json['session_name']
    metadata_url = request.json["metadata_url"]
    local_session_folder_path = LOCAL_IMAGES_DIR + "/" + CURRENT_TERM + "/" + DATE + "/" + session_name
    # Make Jira ticket
    return jsonify({'message': 'Post created successfully'}), 201
