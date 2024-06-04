cluster-up:
	@kind create cluster --config kubernetes/cluster-config/config.yaml
	@kubectl create namespace mqtt
	@kubectl create namespace cert-manager

cluster-delete:
	@kind delete cluster

setup-cert-manager:
	@helm repo add jetstack https://charts.jetstack.io
	@helm repo update
	@helm upgrade --install cert-manager jetstack/cert-manager \
  		--namespace cert-manager \
  		--create-namespace \
  		--set installCRDs=true

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