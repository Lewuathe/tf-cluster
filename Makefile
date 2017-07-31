all: build

build:
	docker build -t lewuathe/tf-cluster .

run:
	docker-compose up -d

down:
	docker-compose down
	docker-compose rm

push: build
	docker push lewuathe/tf-cluster
