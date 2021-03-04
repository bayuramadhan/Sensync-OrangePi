1. Tutorial Menginstall OrangePi:
sudo apt-get update
sudo apt-get upgrade

2. Install Pyhton2 dan pip
sudo apt-get install python
curl https://bootstrap.pypa.io/2.7/get-pip.py | sudo python

3. Install FTP
sudo apt-get install vsftpd
sudo nano /etc/vsftpd.conf
    --> uncomment write_enable=YES

4. Install Web server
sudo apt-get install apache2
sudo apt-get install mysql-server
sudo apt-get install php libapache2-mod-php php-mysql php-cgi php-curl php-json
sudo apt-get install phpmyadmin
sudo mysql_secure_installation
    --> yes
    --> password strong 0
    --> input password 'makanminggu12'
    --> yes terus sampai beres

5. Add mysql account
sudo mysql -u root -p
    --> input password 'makanminggu12'
SET GLOBAL validate_password.policy=LOW
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'makanminggu12';
GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';
FLUSH PRIVILEGES;
exit;
sudo /etc/init.d/mysql restart

6. set timezone
sudo timedatectl set-timezone Asia/Jakarta

7. install i2c dan uart
sudo nano /boot/armbianEnv.txt
    --> tambahkan uart1 uart2 i2c0 i2c1 i2c2 ke baris overlays=usbhost2 usbhost3
sudo nano /etc/modules
    --> tambahkan i2c-dev
sudo apt-get install python-dev i2c-tools.
sudo pip install requests smbus pyserial
