# Jumble-api

A Helm chart for deploying an API server built in Python that takes a word and re-arranges the characters randomly

## Prerequisites

- Kubernetes 1.20+
- Helm 3+

## Installing the Chart

To install the chart with the release name `my-release`:

```console
## clone the helm repository
$ git clone git@github.com:mmurilo/scramble-words.git

## Install the Jumble-apir helm chart
$ helm install my-release --namespace jumble-api scramble-words/deploy/charts/jumble-api
```

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `my-release` deployment:

```console
$ helm delete my-release
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Configuration

The following table lists the configurable parameters of the Jumble-api chart and their default values.

| Parameter                                    | Description                                                                                                                   | Default                                                                                             |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `image.repository`                           | Image Repository                                                                                                              | `"mmurilo/scramble-words"`                                                                          |
| `image.pullPolicy`                           | Image Pull Policy                                                                                                             | `"IfNotPresent"`                                                                                    |
| `image.tag`                                  | Overrides the image tag whose default is the chart appVersion.                                                                | `""`                                                                                                |
| `imagePullSecrets`                           | Image Pull Secrets                                                                                                            | `[]`                                                                                                |
| `serviceAccount.create`                      | If `true`, create a new service account                                                                                       | `true`                                                                                              |
| `serviceAccount.annotations`                 | Annotations to add to the service account                                                                                     | `{}`                                                                                                |
| `serviceAccount.name`                        | Service account to be used. If not set and `serviceAccount.create` is `true`, a name is generated using the fullname template | `""`                                                                                                |
| `podAnnotations`                             | Annotations to add to the cert-manager pod                                                                                    | `{}`                                                                                                |
| `podSecurityContext`                         | Pod Security context                                                                                                          | `{}`                                                                                                |
| `securityContext.runAsUser`                  | User to run containers                                                                                                        | `1000`                                                                                              |
| `securityContext.capabilities.drop`          | Container cappabilities to be dropped                                                                                         | `["all"]`                                                                                           |
| `securityContext.capabilities.add`           | Container cappabilities to be granted                                                                                         | `["NET_BIND_SERVICE"]`                                                                              |
| `service.type`                               | Service type                                                                                                                  | `"ClusterIP"`                                                                                       |
| `service.port`                               | Service port                                                                                                                  | `80`                                                                                                |
| `ingress.enabled`                            | If `true` a resource type ingress will be created                                                                             | `false`                                                                                             |
| `ingress.className`                          | Ingress Class name                                                                                                            | `""`                                                                                                |
| `ingress.annotations`                        | Annotation to be addd to ingress                                                                                              | `{}`                                                                                                |
| `ingress.hosts`                              | Hostname                                                                                                                      | `[{"host": "chart-example.local", "paths": [{"path": "/", "pathType": "ImplementationSpecific"}]}]` |
| `ingress.tls`                                | Ingress TLS configuration                                                                                                     | `[]`                                                                                                |
| `resources.limits.cpu`                       | CPU/memory resource requests/limits                                                                                           | `"500m"`                                                                                            |
| `resources.limits.memory`                    | CPU/memory resource requests/limits                                                                                           | `"512Mi"`                                                                                           |
| `resources.requests.cpu`                     | CPU/memory resource requests/limits                                                                                           | `"100m"`                                                                                            |
| `resources.requests.memory`                  | CPU/memory resource requests/limits                                                                                           | `"128Mi"`                                                                                           |
| `autoscaling.enabled`                        | If `true` will create a HPA resources                                                                                         | `false`                                                                                             |
| `autoscaling.minReplicas`                    | HPA configuration                                                                                                             | `1`                                                                                                 |
| `autoscaling.maxReplicas`                    | HPA configuration                                                                                                             | `100`                                                                                               |
| `autoscaling.targetCPUUtilizationPercentage` | HPA configuration                                                                                                             | `80`                                                                                                |
| `nodeSelector`                               | Node labels for pod assignment                                                                                                | `{}`                                                                                                |
| `tolerations`                                | Node tolerations for pod assignment                                                                                           | `[]`                                                                                                |
| `affinity`                                   | Node affinity for pod assignment                                                                                              | `{}`                                                                                                |
| `env.max_calls`                              | Maximun number of call to be stored in the app's database                                                                     | `1000`                                                                                              |
| `env.return_limit`                           | number off calls to be returned by `audit` endpoint                                                                           | `10`                                                                                                |
| `auth_token`                                 | Authentication token for endpoints                                                                                            | `[]`                                                                                                |
| `persistence.enabled`                        | If `true` data persistence using PV and PVC                                                                                   | `true`                                                                                              |
| `persistence.storageClassName`               | storaga class name for persistence storage                                                                                    | `"standard"`                                                                                        |
| `persistence.accessMode`                     | access mode for PV and PVC                                                                                                    | `"ReadWriteOnce"`                                                                                   |
| `persistence.size`                           | Persistence storage size                                                                                                      | `"1Gi"`                                                                                             |
| `persistence.existingClaim`                  | name of existinng PVC                                                                                                         | `""`                                                                                                |
| `persistence.hostPath`                       | host path for persistent storage                                                                                              | `"/tmp/db-data"`                                                                                    |

### Default Security Contexts

The default pod-level and container-level security contexts, below, adhere to the [restricted](https://kubernetes.io/docs/concepts/security/pod-security-standards/#restricted) Pod Security Standards policies.

Default pod-level securityContext:

```yaml
runAsNonRoot: true
runAsUser: 1000
```

Default containerSecurityContext:

```yaml
allowPrivilegeEscalation: false
capabilities:
  drop:
    - all
  add:
    - NET_BIND_SERVICE
```

### Assigning Values

Specify each parameter using the `--set key=value[,key=value]` argument to `helm install`.

Alternatively, a YAML file that specifies the values for the above parameters can be provided while installing the chart. For example,

```console
$ helm install my-release -f values.yaml .
```

> **Tip**: You can use the default [values.yaml](values.yaml)
