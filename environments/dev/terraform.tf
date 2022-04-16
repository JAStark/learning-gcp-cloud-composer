terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "~> 3.89.0"
    }
  }
  backend "gcs" {
    bucket = "flask-app-tfstate"
    prefix = "env/learning_cloud_composer/dev"
  }
}

provider "google" {
  # Configuration options
  project = var.project
  region  = var.region

}
