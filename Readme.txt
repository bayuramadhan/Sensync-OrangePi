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
1. sudo apt-get install apache2
2. sudo apt-get install mysql-server
3. sudo apt-get install php libapache2-mod-php php-mysql php-cgi php-curl php-json
4. sudo apt-get install phpmyadmin
5. sudo mysql_secure_installation
    --> yes
    --> password strong 0
    --> input password 'makanminggu12'
    --> yes terus sampai beres

Add mysql account
1. sudo mysql -u root -p
    --> input password 'makanminggu12'
2. SET GLOBAL validate_password.policy=LOW
3. CREATE USER 'admin'@'localhost' IDENTIFIED BY 'makanminggu12';
4. GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';
5. FLUSH PRIVILEGES;
exit;
sudo /etc/init.d/mysql restart

