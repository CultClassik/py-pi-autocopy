#!/bin/sh

envsubst < usb-auto-copy.service | sponge /lib/systemd/system/usb-auto-copy.service