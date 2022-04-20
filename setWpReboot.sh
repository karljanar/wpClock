#!/bin/bash
PID=$(pgrep gnome-session | tail -n1)
export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-)

BASEDIR=$(pwd)
IMG="/img/out.png"

PIC=$BASEDIR$IMG
gsettings set org.gnome.desktop.background picture-uri "file://$PIC"