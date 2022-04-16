resource "google_composer_environment" "demo" {
  name    = "prod-demo-environment"
  region  = "europe-west2"

  config {
    software_config {
      image_version = "composer-1.18.6-airflow-1.10.15"
    }
  }

}
