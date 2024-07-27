# Camera Mirror

## Install

**Note**: This is intended to run on a Raspberry Pi 4B

If it's your first time using a particular Pi, add your ssh key to GitHub, then:
- `ssh pi@faces.local`
- `git clone git@github.com:camoverride/camera_mirror.git`
- `cd camera_mirror`
- `python -m venv --system-site-packages .venv`
- `source .venv/bin/activate`

Install Python packages:
<!-- - `pip install numpy --upgrade --prefer-binary` -->
- `pip install numpy PyYAML opencv-python`

<!-- - `pip install --upgrade numpy` -->
- `pip install --force-reinstall simplejpeg --default-timeout=1000`

The following are required for the `face_recognition` package:

Install [cmake](https://lindevs.com/install-cmake-on-raspberry-pi/):
- `sudo apt update`
- `sudo apt install -y cmake`

Install [dlib](https://pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/):
- `cd ..`
- `git clone https://github.com/davisking/dlib.git`
- `cd dlib`
- `python setup.py install` (takes a long time)

Install `face_recognition`. Note: OpenCV's haarcascade might be preferable if using a Raspberry Pi
- `pip install face_recognition`

Probably downgrade numpy so it's compatible with `face_recognition`...
- `python -m pip install numpy==1.4`


## Setup Display

Hide the cursor:

- `sudo mv /usr/share/icons/PiXflat/cursors/left_ptr /usr/share/icons/PiXflat/cursors/left_ptr.bak`

Rotate and enable the display:

- `WAYLAND_DISPLAY=wayland-1 wlr-randr --output HDMI-A-1 --transform 90`
- `export DISPLAY=:0`

Restore the cursor (if you wish):

- `sudo mv /usr/share/icons/PiXflat/cursors/left_ptr.bak /usr/share/icons/PiXflat/cursors/left_ptr`


## Run

Required after ssh-ing in:

- `cd ~/Desktop/camera_mirror`
- `source camera_mirror_2/bin/activate`

Test run:
- `python test_picam_stream.py`

Run in production:

Start a service with *systemd*. This will start the program when the computer starts and revive it when it dies. Copy the contents of `recordingloop.service` to `/etc/systemd/system/recordingloop.service` (via `sudo vim /etc/systemd/system/recordingloop.service`).

Start the service using the commands below.

- `sudo systemctl daemon-reload`
- Start it on boot: `sudo systemctl enable recordingloop.service` 
- Start it right now: `sudo systemctl start recordingloop.service`
- Stop it right now: `sudo systemctl stop recordingloop.service`
- Get logs: `sudo journalctl -u recordingloop | tail`

Helpful:

- `git update-index --skip-worktrees`


## To Do's

- read from RTSP stream
- correct recordingloop startup thing
- run screen setup at startup
- add basecamp, hotspot, eason wifi wpaconfig 
- add to tailscale
- add filter, analysis, etc
