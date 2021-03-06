# docker-cloud-test
Docker Cloud Example for COMP 698 in UNH Manchester

#Getting to AWS

You are using you given key to connect to your AWS EC2 Instance through SSH, command looks like

`ssh -i wcouturier-xxxxxxxxxx.key 54.215.211.220`

The last entry in the command is YOUR specific IP address. If you have an issue with it saying

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

Then you need to execute command: `chmod 0400 wcouturier-xxxxxxxxxx.key`, then re-run the ssh command, and it should work

Once on your instance run the command  

`lsb_release -a`

That should give us the information of the operating system. In this case, it should be almost like:

```
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.2 LTS
Release:	16.04
Codename:	xenial
```

Next, as long as you have either sudo or root privileges, you shoudl run the command `sudo apt-get update -y` to update your VM

Once done, install docker using either `sudo apt-get install -y docker` or for some reason mine didn't install until I used `sudo apt install -y docker.io`

```
UPDATE - docker.io is an older version of a docker installer, it's prefered we do something else to install
```

Once the programs are installed, we want to perform our build. Because at the time of this writing we have not achieved CI / CD / CD, we are going to do

```
sudo docker run -d -p 8080:5000 wmc81294/docker-cloud-test python3 unh698.py
```

it states that we want to run the container in a detached state, funnel all traffic from port 8080 of the host OS to the container's port 5000, using the image from docker cloud from a specified user's repo, use python3 to run the file unh698.py as soon as it's started, and continuously run.

# How to delete docker images and containers

<b>WARNING - this will delete all images and containers, and it will not be recoverable</b>

```
#!/bin/bash
# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi $(docker images -q)
```

# Wireshark command

```
sudo -g wireshark wireshark-gtk
```

# Other Resources

[Deployment.md](./deployment.md)
