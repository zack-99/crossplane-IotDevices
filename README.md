# crossplane-IotDevices

##Creazione Cluster con Kind:

 `kind create cluster --name crossplane`
 
##Installazione Crossplane all'interno del Cluster:

`helm install crossplane --namespace crossplane-system --create-namespace crossplane-stable/crossplane`

##Installazione Provider Kubernetes all'interno del Cluster:

`kubectl apply -f kubernetes-provider.yaml`

##Configurazione richiesta se il Provider Kubernetes esegue all'interno del Cluster:

`SA=$(kubectl -n crossplane-system get sa -o name | grep provider-kubernetes | sed -e 's|serviceaccount\/|crossplane-system:|g')
kubectl create clusterrolebinding provider-kubernetes-admin-binding --clusterrole cluster-admin --serviceaccount="${SA}"
kubectl apply -f  kubernetes-provider-config.yaml`

##Creazione Namespace in cui verrano eseguiti i dispositivi IoT:

`kubectl create namespace iot-namespace`

##Creazione della CompositeResourceDefinition (CRD)

`kubectl apply -f iot-device-crd.yaml`

##Creazione della Composition

`kubectl apply -f iot-device-composition.yaml`

##Creazione device simulati

Si utilizzano i Claim come `xdevice-claim.yaml`, in cui è possibile modificare i `parameters` per ottenere il comportamento desiderato.
Il dispositivo IoT si crea applicando il comando: 

`kubectl apply -f xdevice-claim.yaml`.
