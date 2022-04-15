from crontab import CronTab
import os, getpass
user = getpass.getuser()
base_dir = os.path.dirname(__file__)
cron = CronTab(user=user)
job = cron.new(command='python3 ' + base_dir + '/make_wp.py')
job.minute.every(1)
job = cron.new(command='gsettings set org.gnome.desktop.background picture-uri "file:///'+base_dir+'/img/out.png"')
job.every_reboot()
cron.write()