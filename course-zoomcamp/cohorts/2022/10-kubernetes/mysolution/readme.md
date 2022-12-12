Install kubectl:
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/#install-kubectl-binary-with-curl-on-linux
1) Download the latest release with the command:
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
2) Validate the binary (optional)
curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
Validate the kubectl binary against the checksum file:
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check

Install Kind:
https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-release-binaries
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.17.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

Create cluster:
kind create cluster

get list of services:
kubectl get services 

To be able to use the docker image we previously created (zoomcamp-model:v001), we need to register it with kind. Command to do so:
kind load docker-image



apply a deployment.yaml file:
kubectl apply -f deployment.yaml
to see deployments:
kubectl get deployments

then apply service.yaml:
kubectl apply -f  service.yaml
to see services:
kubectl get services


kubectl port-forward service/credit-card-service 9696:80
