# py-pi-autocopy
Experiment to autocopy a file to usb on a RPi when a device is inserted.

## Ensure SSH is configured on your RPi.
1. If you can't get the IP of the RPi from your router or other device, log in to it physically and type `ip addr` and note the IP.
2. Type `sudo touch /boot/firmware/ssh`
3. Type `sudo reboot`

After reboot, from your PC:
1. Use Terninal on MacOS or Powershell on Windows, type `ssh <your username>@<ip address>`
2. Enter your password when prompted


Note for below, if you see `&&\` or `\` at the end of a line, copy all of it and run it together. For example in required pacakges section below, copy the entire code block, paste it in your sssh terminal and hit enter.

## Install required packages
From your ssh session:
```bash
sudo apt update &&\
sudo apt install -y \
  moreutils \
  gettext-base \
  python3 \
  git
```

## Clone this repository
```bash
cd ~ &&\
git clone  https://github.com/CultClassik/py-pi-autocopy.git
```

## Setup and test
```bash
# set required variables
export SOURCE_FILE='/path/to/source/file.txt'
export USB_MOUNT_POINT='/media/usb'
export DESTINATION_FILE='file.txt'

# optionally test the python script, after inserting the usb device
python3 ./pi-copy.py  \
  --source $SOURCE_FILE \
  --usb $USB_MOUNT_POINT \
  --destination $DESTINATION_FILE

# if that works, do this 
rm "${USB_MOUNT_POINT}/${DESTINATION_FILE}"


# remove the usb device and then you can run this, then test by inserting the usb device to see if the file copies successfully
cd py-pi-autocopy && ./setup.sh
```


