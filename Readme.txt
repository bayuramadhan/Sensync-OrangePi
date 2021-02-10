Tutorial Menginstall OrangePi:
1. sudo apt-get update
2. sudo apt-get upgrade

Install Pyhton2 dan pip
3. sudo apt-get install python
4. curl https://bootstrap.pypa.io/2.7/get-pip.py | sudo python

Install FTP
5. sudo apt-get install vsftpd
6. sudo nano /etc/vsftpd.conf, uncomment write_enable=YES

Install Web server
7. sudo apt-get install apache2
8. sudo apt-get install php
9. sudo apt-get install php-mysql
10. sudo apt-get install mysql-server
11. sudo apt-get install libapache2-mod-php
12. sudo apt-get install phpmyadmin
13. sudo chown admin /var/www/html
14. ln -s /usr/share/phpmyadmin phpmyadmin
15. sudo systemctl restart apache2

Add mysql account






1. chmod +x /home/admin/run.sh
