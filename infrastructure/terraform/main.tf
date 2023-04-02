module "gcp-gke" {
    source = "./modules/k8s"
}

module "gcp-storage" {
    source = "./modules/storage"
}