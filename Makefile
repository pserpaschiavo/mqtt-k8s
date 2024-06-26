cluster-up:
	@kind create cluster --config kubernetes/cluster-config/config.yaml
	
cluster-delete:
	@kind delete cluster

setup-cert-manager:
	@helm repo add jetstack https://charts.jetstack.io
	@helm repo update
	@helm upgrade --install cert-manager jetstack/cert-manager \
  		--namespace cert-manager \
  		--create-namespace \
  		--set installCRDs=true

setup-prometheus:
	@helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
	@helm repo update
	@helm install prometheus-stack prometheus-community/kube-prometheus-stack --version 60.0.0 \
  		--namespace monitoring \
  		--create-namespace \

setup-v1-emqx:
	@helm repo add emqx https://repos.emqx.io/charts
	@helm repo update
	@helm upgrade --install emqx-operator emqx/emqx-operator \
  		--namespace emqx-operator-system \
  		--create-namespace
	@kubectl wait --for=condition=Ready pods -l "control-plane=controller-manager" -n emqx-operator-system
	

setup-v2-emqx:
	@kubectl create -f kubernetes/emqx-manifests-v2/emqx-dep.yaml
	@kubectl create -f kubernetes/emqx-manifests-v2/emqx-service.yaml
	@kubectl create -f kubernetes/emqx-manifests-v2/emqx-configmap.yaml
	@kubectl create -f kubernetes/emqx-manifests-v2/emqx-rbac.yaml

clients-up:
	@kubectl create -f python/subscriber/subscriber.yaml
	@kubectl create -f python/publisher/publisher.yaml

clients-down:
	@kubectl delete deployments.apps k8s-mqtt-subscriber 
	@kubectl delete deployments.apps k8s-mqtt-publisher
