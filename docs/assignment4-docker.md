# Assignment 4 – Creating a Docker image

The goal here is to take the result of your last assignment and build a Docker image for it. This is mostly about figuring out what needs to be in the Dockerfile. Once you have that, building the image should be easy: 

```bash
$> docker build -t IMAGE_NAME .
```

And when you have the image, anyone should be able to run it:

```bash
$> docker run --rm --detach --publish 5000:5000 IMAGE_NAME
```

You should get the following messages printed to your terminal. 

```
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 118-561-796
```

If your application wasn't named `app.py` the first line will be somewhat different. In any case, people can now see your entities site at [http://0.0.0.0:5000/](http://0.0.0.0:5000/).

What you need to create is a Git reporitory with

1. a readme file that describes your work
2. all code needed to run your application
3. a Dockerfile that anyone can use to build the image

Send the link to the repository to me by April 27th.

Some things are not quite obvious and could get you in a tailspin. What follows are some hints to get you on your way. Feel free to email me with any remaining problems if you get stuck.

---

Figure out what exactly your requirements are by looking at the environment in which your code runs (python version, version of installed packages, database requirements, and any linux commands) and what files are needed to run your application.

When I did this assignment using the wrong environment I got an error that took me a while to fix, but it turned out to be an incompatible version of some Python package.

---

You start from an existing image and you could try to find an image on [https://hub.docker.com/](https://hub.docker.com/) that has everything you need (Python, all packages in Python that you need, SQLite), but what you need exactly may be hard or impossible to find. My suggestion is to start your Dockerfile as follows.

```dockerfile
FROM python:3.6-slim-buster
RUN apt-get -y update && apt-get install -y sqlite3 libsqlite3-dev
```

The first line makes your point of departure an official Python Docker image, the name of that image is `python` and the version we use is `3.6-slim-buster`. With this we will get what is the most recent version of Python 3.6, which currently (April 2021) is Python 3.6.13.  If you want to have more control over which version you want you can spell it out by using `3.6.13-slim-buster`. And of course you could use a more recent Python version if you want, but you probably should still avoid version 3.10. The `buster` part of the version refers to Debian 10.4 which is the latest stable release of Debian and in your base image Python is built on top of a fixed Linux distribution. Finally, the `slim` part indicates that we use a paired down version of the full image. This image only installs the minimal packages needed to run python. You can use `3.6-buster` at the cost of a bigger image (875MB versus 112MB).

In the second line we install SQLite, which can be a bit tricky. On Ubuntu and Debian you install applications with `apt-get` (Advanced Packaging Tool). You want to precede each install with an `apt-get update` because it downloads the list of available packages, which is not on your base image. It is also recommended to do all your installs in a signle line.

---

Sometimes it is useful to experiment inside of your container and see what is there. If you built an image you can spin up a container, connect to it and run a bash shell.

```bash
$> docker run --rm -it IMAGE_NAME bash
```

You will get a container promt that looks like `root@6196823c68d8:/# ` and then you can look around and try what you wanted to try in the Dockerfile. You can do this even after a build that just failed. In the latter case you will notice a recent image with no name that will be at the top of your images list.

```bash
$> docker images
<none>                           <none>            26bbd24f3787   50 seconds ago   535MB
entities                         latest            7495d3b25c62   21 hours ago     1.3GB
python                           3.8-slim-buster   b281745b6df9   3 days ago       114MB
```

And you can enter it and see what the state of the image/container is.

```bash
$> docker run --rm -it 26bbd24f3787 bash
```

You can also do this from your base image.

---

One hard to debug error is where everything looks fine, and you know it runs outside of Docker and you are convinced that you got everything perfectly installed, you even know you can run the website from inside the container and connect to it. But nothing happens when you connect to the container's website from outside the contaier. In your main application file you probably have the following two lines at the end.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

And this worked fine till now, but inside a container you want to port number.

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

When you use `0.0.0.0` you tell the your Flask server to listen to all available IP addresses on the container. Some people say this is a security risk, but both the Docker documentation at [https://docs.docker.com/compose/gettingstarted/](https://docs.docker.com/compose/gettingstarted/) and the Flask QuickStart tutorial at [https://flask.palletsprojects.com/en/1.1.x/quickstart/](https://flask.palletsprojects.com/en/1.1.x/quickstart/) use `0.0.0.0` and do not mention a security risk.

---

Further reading:

- Flask in Docker
  - [https://felipefaria.medium.com/running-a-simple-flask-application-inside-a-docker-container-b83bf3e07dd5](https://felipefaria.medium.com/running-a-simple-flask-application-inside-a-docker-container-b83bf3e07dd5)
  - [https://runnable.com/docker/python/dockerize-your-flask-application](https://runnable.com/docker/python/dockerize-your-flask-application)
  - [https://www.digitalocean.com/.../how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04](https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04)
- On Python Docker builds
  - [https://hub.docker.com/_/python](https://hub.docker.com/_/python)
  - [https://medium.com/.../alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker](https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d)
  - [https://pythonspeed.com/articles/base-image-python-docker-images/](https://pythonspeed.com/articles/base-image-python-docker-images/)
  - [https://pythonspeed.com/articles/reproducible-docker-builds-python/](https://pythonspeed.com/articles/reproducible-docker-builds-python/)

It also helps to look at the getting started tutorial at [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/) which will go much further into Docker than what you need to know for this assignment. The tutorial will ask you to run the following docker-run command.

```bash
$> docker run -d -p 80:80 docker/getting-started
```

What it does not tell you is that you then need to point your browser to [http://0.0.0.0/tutorial/](http://0.0.0.0/tutorial/).

