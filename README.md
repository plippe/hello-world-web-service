# Hello World web service

Docker offers a simple way to verify it is installed properly with the
[`hello-world`](https://hub.docker.com/_/hello-world/) image. This image has no real purpose, but to display
`Hello from Docker!`.

Similarly, this project's only goal is to start a web service, and return healthy responses. This can be useful to
validate connectivity between multiple remote services.


### Getting started

A sample image is available on [Docker Hub](https://hub.docker.com/r/plippe/hello-world-web-service/).

```
docker run --rm -itp 5000:5000 plippe/hello-world-web-service
```

By default, the web service will run on the port `5000`. It can be published to a different one, but also configured
during the build phase.

```
docker build --build-arg PORT=8080 -t my-image https://github.com/plippe/hello-world-web-service.git
docker run --rm -itp 8080:8080 my-image
```
