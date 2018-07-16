.PHONY: build run release
.DEFAULT_GOAL := build

DOCKER_IMAGE := plippe/hello-world-web-service
DOCKER_PORT := 5000

build:
	docker build \
		--build-arg PORT=$(DOCKER_PORT) \
		--tag $(DOCKER_IMAGE) .

run:
	docker run \
		--rm \
		--interactive \
		--tty \
		--publish ${DOCKER_PORT}:${DOCKER_PORT} \
		$(DOCKER_IMAGE)

release:
	docker push $(DOCKER_IMAGE)
