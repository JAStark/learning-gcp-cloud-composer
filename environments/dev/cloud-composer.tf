resource "google_composer_environment" "demo" {
  name      = "dev-demo-environment"
  region    = var.region

  config {
    software_config {
      image_version = "composer-2.0.11-airflow-2.2.3"
    }
  }

}
