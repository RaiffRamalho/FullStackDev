# Logs Analysis Project

This is the modules 3  first project of udacity course of Fullstack Developer

## Prerequisites

* Python 2.7 installed in the machine

### Set up described in the project specification

* Install VirtualBox

VirtualBox is the software that actually runs the virtual machine. [You can download it from virtualbox.org, here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) . Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

Currently (October 2017), the supported version of VirtualBox to install is version 5.1. Newer versions do not work with the current release of Vagrant.

Ubuntu users: If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center instead. Due to a reported bug, installing VirtualBox from the site may uninstall other software you need.

* Install Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. [Download it from vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

If Vagrant is successfully installed, you will be able to run vagrant --version
in your terminal to see the version number.
The shell prompt in your terminal may differ. Here, the $ sign is the shell prompt.

* Download the VM configuration

Use Github to fork and clone the [repository](https://github.com/udacity/fullstack-nanodegree-vm)
You will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

Navigating to the FSND-Virtual-Machine directory and listing the files in it.
This picture was taken on a Mac, but the commands will look the same on Git Bash on Windows.

* Start the virtual machine

From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

* Logged in!

If you are now looking at a shell prompt that starts with the word vagrant (as in the above screenshot), congratulations — you've gotten logged into your Linux VM.

Inside the VM, change directory to /vagrant and look around with ls.

The files you see here are the same as the ones in the vagrant subdirectory on your computer (where you started Vagrant from). Any file you create in one will be automatically shared to the other. This means that you can edit code in your favorite text editor, and run it inside the VM.

Files in the VM's /vagrant directory are shared with the vagrant folder on your computer. But other data inside the VM is not. For instance, the PostgreSQL database itself lives only inside the VM.

* Download the data

Next, download the [data here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.

Here's what this command does:

psql — the PostgreSQL command line program

-d news — connect to the database named news which has been set up for you

-f newsdata.sql — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

## How to run

Open the virtual machine.
Run
```
vagrant up
vagrant ssh
```
After go to vagrant directory

```
cd /vagrant/
```

The file logProj.py need to be inside the vagrant folder. Execute the comand

```
python logProj.py
```
