#!/bin/sh
MYDIR="$(dirname "$(which "$0")")"
ANSWER="$($MYDIR/alerter -title 'VMware IT Update' -subtitle '1.0' -message 'New VMware Update, click here for more' -closeLabel "Read Now" -actions "Dismiss","Read Later")"
case $ANSWER in
"@TIMEOUT") echo "Timeout man, sorry" ;;
"@CLOSED") echo "You clicked on the default alert close button" ;;
"@CONTENTCLICKED") echo "You clicked the alert content !" ;;
"@ACTIONCLICKED") echo "You clicked the alert default action button" ;;
"Read Later") echo "Action LATER" ;;
"Dismiss") echo "Action DISMISS" ;;
"Read Now") echo "Action MORE" ;;
**) echo "? --> $ANSWER" ;;
esac
