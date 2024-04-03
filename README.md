# PaperPerspective
Utilized OpenCV and pyvirtualcam to implement Perspective Transformation in real-time, eliminating the need for camera or whiteboard setups.

Initially i thought of making it an IoT based project utilizing ESP32 CAm or Rpi but then
didnt get enough of any valuable reasons to do so because i can get the work done this way from my own system so whats the need of setting up a client-server system. Maybe I'll work upon this in coming time but for now this is it. The name is cool.

## **Setup:**

1. **Install Python**: Make sure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).
2. **Install Required Libraries**: Use pip to install the required libraries:
3. pip install opencv-python pyvirtualcam


## Usage

1. **Clone the Repository**: Clone the Paper Perspective repository to your local machine:
2. git clone https://github.com/ritikonboard/PaperPerspective.git

2. **Navigate to the Directory**: Go to the Paper Perspective directory: cd PaperPerspective
4.  **Run the Python Script**: python PaperPerspective.py



## streaming the corrected video stream to google meet
if you want to use the perspective corrected video to be shared as your main camera video on Google Meet or any other video platform, then pyvirtualcam comes to rescue as it creates a virtual video for you. 
Make sure you have OBS installed for this to have this virtual cam feature on your system.
**Install OBS Virtual Camera (Optional)**: If you want to use Paper Perspective with OBS Virtual Camera, download and install OBS Studio from [obsproject.com](https://obsproject.com/). 

Now after inatalling and setting up thr obs for normal usage as you need(recording), move fprward with the following..

Run the script, corrected video frame window will appear along with original frame. 
Open Google Meet in new tab on chrome or any browser. choose the Camera source and change it from iintegrated cam to virtual cam(obs cam). you can then see the corrected video that will be shared as your primary camera video. You might need to change the color settings in obs to match the opencv color theme. 

I will make a video tutorial for this and will add pictures for reference in some time.


 
## Contributing

Contributions are welcome! I just started with OpenCV and this is just a simple application i could think of. I'm interested in diving more into Computer Vision, IoT, Embedded.
If you have any suggestions, please open an issue or submit a pull request.



