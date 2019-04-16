#!/bin/sh
sudo launchctl unload /Library/LaunchDaemons/com.vmware.epm.notify.plist
sudo rm /Library/LaunchDaemons/com.vmware.epm.notify.plist

sudo rm -R /Library/VMware/Notify
