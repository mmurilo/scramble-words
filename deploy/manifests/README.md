# K8s Deployment files

This directory containes the Kubernetes manifests needed to deploy Jumble-api.

These 'static deployment manifests' are generated automatically from the [helm chart](../charts/jumble-api/Chart.yaml).

When a new release is created, these manifests will beautomatically generated and published

## Installing

### Prerequisites

- [kubectl](Prerequisites)
- A supported version of kuberentes

### Deploying

All resources are included in a single YAML manifest file.

Create a namesapce

```bash
kubectl apply -f namespace.yaml
```

Install all jumble-api components:

```bash
kubectl -n jumble-api apply -f jumble-api.yaml
```

By default, jumble-api will be installed into the jumble-api namespace. It is possible to run it in a different namespace, although you'll need to make modifications to the deployment manifests.

### Uninstalling

To uninstall jumble-api you can run:

```bash
kubectl -n jumble-api delete -f jumble-api.yaml
```

## How can I generate my own manifests?

If you want to build a copy of your own manifests for testing purposes, you
can do so `helm template`.

To build the manifests, run:

```bash
helm template -n jumble-api jumble charts/jumble-api --skip-tests > jumble-api.yaml
```

These manifest are generated based on `defaults` helm values, If you want to customize your manifests, edit your own values.yaml file and run:

```bash
helm template -n jumble-api jumble charts/jumble-api -f <your_helm_values>.yaml --skip-tests > jumble-api.yaml
```
