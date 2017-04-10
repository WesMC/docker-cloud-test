# docker-cloud-test
Docker Cloud Example for COMP 698 in UNH Manchester

#Getting to AWS

You are using you given key to connect to your AWS EC2 Instance through SSH, command looks like

`ssh -i wcouturier-1491234697.key 54.153.127.23`

The last entry in the command is YOUR specific IP address. If you have an issue with it saying

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
```

Then you need to execute command: `chmod 0400 wcouturier-1491234697.key`, then re-run the ssh command, and it should work

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

# How to delete docker images and containers

<b>WARNING - this will delete all images and containers, and it will not be recoverable</b>

```
#!/bin/bash
# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi $(docker images -q)
```

# Other Resources

[Deployment.md](./deployment.md)
