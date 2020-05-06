#Make a service from the application

```
touch /etc/systemd/system/NAME.service
```
```
[Unit]
Description=My Cool service
After=syslog.target network.target
 
[Service]
Type=forking
ExecStart=/opt/tomcat-8.0.32/bin/startup.sh
ExecStop=/opt/tomcat-8.0.32/bin/shutdown.sh
Restart=always
User=root
Group=root
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=liferay
  
[Install]
WantedBy=multi-user.target
```

```
sudo service NAME stop/start/status
```
