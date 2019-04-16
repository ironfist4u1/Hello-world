#!/bin/sh
dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

sudo unzip $dir/Notify.zip -d /Library/VMware
sudo chown -R :staff /Library/VMware/Notify/*
sudo chmod 775 /Library/VMware/Notify/*
sudo chmod 775 /Library/VMware/Notify/resources/*

dscl . list /Users | grep -v '_' | grep -v 'administrator' | grep -v 'daemon' | grep -v 'nobody' | grep -v 'root' | grep -v 'mfe' > /Library/VMware/Notify/my_text_file.txt

#my weird way of finding the user name

sudo python /Library/VMware/Notify/resources/configInstall.py
sudo rm /Library/VMware/Notify/resources/configInstall.py

sudo chmod a+x /Library/VMware/Notify/com.vmware.epm.notify.plist

sudo cp /Library/VMware/Notify/com.vmware.epm.notify.plist /Library/LaunchDaemons/

sudo chown root:wheel /Library/LaunchDaemons/com.vmware.epm.notify.plist

sudo launchctl load -w  /Library/LaunchDaemons/com.vmware.epm.notify.plist

sudo rm /Library/VMware/Notify/com.vmware.epm.notify.plist

sudo rm -R /Library/VMware/__MACOSX
