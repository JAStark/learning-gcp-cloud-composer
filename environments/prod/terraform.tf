terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 3.89.0"
    }
  }
  backend "gcs" {
    bucket = "learning_cloud_composer"
    prefix = "env/prod"
  }
}

provider "google" {
  # Configuration options
  project = var.project
  region  = var.region

}
