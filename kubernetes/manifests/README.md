# K8s manifest

helm template -n jumble-api jumble charts/jumble-api --skip-tests > manifests/jumble-api.yaml
