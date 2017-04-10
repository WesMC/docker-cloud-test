#Everything that is necessary on Flask Server Instance.
## 1) Setup a repository on Github for Version Control

## 2) Code for web app

In order to have any sort of web app, we need to make the web app in the first place. In our case, it is nothing more than importing Flask, defining a home root / index, then setting the python file to run the app by using:

```
if __name__ == '__main__':
    app.runAppFunction(whateverTheNameIs)
```

## 3) Unit / Acceptance Testing

Once we've written our app, we want to make sure that what the output is, is exactly what we expect it to be. For our app, we use a bash script to run a python3 script that imports a library called `unittest`. Using that, we set it so that it expects, and searches for our content that should be there.

## 4) Dockerfile for Docker containers / images

With using docker, we are able to create virtual machine images that act as an OS with pre-installed programs and libraries that we want to use.

We also have a .yml file for our build tests for continuous integration on docker cloud. It executes the `Dockerfile` so that it builds, then it calls the `run_tests.sh` script to test if the flask server works.

## 5) AWS instance

Using a specified key, we login to our AWS instance, install docker and git software, clone the master Repo from Github, and then run the specific docker commands to build and then run the Flask Server in a detached state that continuously runs
