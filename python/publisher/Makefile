build-image:
	@docker build -t pserpaschiavo/k8s-mqtt-publisher:1.0 .

push-image:
	@docker push pserpaschiavo/k8s-mqtt-publisher:1.0

new-repository:
	@docker tag pserpaschiavo/k8s-mqtt-publisher:1.0 k8s-mqtt-publisher:1.0

k8s-up:
	@kubectl create -f publisher.yaml

k8s-down:
	@kubectl delete deployments.apps k8s-mqtt-publisher