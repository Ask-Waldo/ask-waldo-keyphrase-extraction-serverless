# Extract keywords API

_Note for Robin: https://www.magalix.com/blog/implementing-faas-in-kubernetes-using-kubeless_
## Install Kubeles locally

```bash
    brew install kubeless
```


## Install Kubeless on cluster

_Note: check if RBAC is used within the target cluster!_

- If RBAC is enabled:
  ```bash
   kubectl create ns kubeless 
   export RELEASE=$(curl -s https://api.github.com/repos/kubeless/kubeless/releases/latest | grep tag_name | cut -d '"' -f 4)
   kubectl create -f https://github.com/kubeless/kubeless/releases/download/$RELEASE/kubeless-$RELEASE.yaml
  ```
  
- If RBAC is not enabled:
  ```bash
    kubectl create ns kubeless
    export RELEASE=$(curl -s https://api.github.com/repos/kubeless/kubeless/releases/latest | grep tag_name | cut -d '"' -f 4)
    kubectl create -f https://github.com/kubeless/kubeless/releases/download/v1.0.8/kubeless-non-rbac-$RELEASE.yaml
  ```

## Deploy function to cluster

