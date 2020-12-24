# weatherballoon2pocsag

This is a simple script to notify you of a weatherballoon close to you via POCSAG.

## installed software

You need python3 and crontab installed on your machine. Further install the needed python modules.

## setup variables

### import.py

In this script on line 23 you have to setup your APRS call and the pincode.

### pocsag_sender.py

In this script on line 9 to 13 you have to setup your POCSAG call, password, posittion, maximal distance and tx group.

## crontab

Start your contab setup with `crontag -e` and add this lines (take care of the correct path):

```
*/10 * * * * cd /home/pi/weatherballoon2pocsag && ./pocsag_sender.py >> cron.log
2 4,16 * * * cd /home/pi/weatherballoon2pocsag && ./start_import.sh >> import.log
```
