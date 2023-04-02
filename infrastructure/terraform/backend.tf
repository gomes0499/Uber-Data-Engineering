terraform {
  backend "gcs" {
    bucket  = "wu7tfstate"
    prefix  = "terraform/state"
  }
}
