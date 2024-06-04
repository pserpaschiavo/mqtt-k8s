cluster-up:
	@kind create cluster --config /home/phil/Projects/MQTT/k8s-mosquito/kubernetes/cluster-config/config.yaml
	@kubectl create namespace mqtt
	@kubectl create namespace cert-manager

set-mqtt:
	@kubectl config set-context --current --namespace mqtt
	@kubectl config get-contexts
	
set-default:
	@kubectl config set-context --current --namespace default
	@kubectl config get-contexts
	
install-cert-manager:
	@kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.12.0/cert-manager.crds.yaml
	@helm repo add jetstack https://charts.jetstack.io
	@helm repo update
	@helm install cert-manager --namespace cert-manager --version v1.14.5 jetstack/cert-manager

install-ingress-nginx:
	@kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
	@kubectl wait --namespace ingress-nginx \
  			--for=condition=ready pod \
  			--selector=app.kubernetes.io/component=controller \
  			--timeout=270s

delete-cluster:
	@kind delete cluster