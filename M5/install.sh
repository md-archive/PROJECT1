#!/bin/bash
touch "installation_log_$(date +%F).log"
echo "Performing System Update..." >> installation_log_$(date +%F).log
sleep .9
echo "Upgrading packages..." >> installation_log_$(date +%F).log
{
sudo apt update -y && sudo apt upgrade -y
} > /dev/null > installation_log_$(date +%F).log 
echo "Installing Dependencies..." >> installation_log_$(date +%F).log
sleep 3
{
sudo apt install apache2 -y 
sudo apt install php8.1  -y 
} > /dev/null > installation_log_$(date +%F).log

{
MAIN="#listen_addresses = 'localhost'        # what IP address(es) to listen on;"
MODIFIED="listen_addresses = '*'        # what IP address(es) to listen on;"
apt install postgresql postgresql-contrib -y
echo "DONE..."
sleep 2
cd /etc/postgresql/14/main/
echo "Starting Services. . ."
pg_ctlcluster 14 main start
echo "Enabling Connectivity..."
sed -i "s/$MAIN/$MODIFIED/g" /etc/postgresql/14/main/postgresql.conf
touch pg_hba.conf
echo "# TYPE DATABASE USER CIDR-ADDRESS  METHOD" >> pg_hba.conf
echo "host    all             all             0.0.0.0/0               md5" >> pg_hba.conf
echo "YOU ARE GOING TO BE ASKED TO SET YOUR DATABASE PASSWORD!"
sleep 5
sudo -u postgres psql --command '\password postgres'
systemctl restart postgresql
service postgresql restart

echo "Loading the Server Main IP address..."
hostname -I | cut -f1 -d' '
sleep .5
echo "To access the database please use the shown IP address and an available port on :5432"
echo "Loading Users..."
sleep .5
echo "===================================================="
sleep .2
echo "========= User: postgres                    ========"
sleep .3
echo "========  Password: set_user_password        ======="
echo "===================================================="
} > /dev/null > installation_log_$(date +%F).log

echo "Done"
exit 0

