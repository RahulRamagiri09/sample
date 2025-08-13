# Test Terraform file to verify secret scanner ignores specific keywords

resource "google_compute_network" "main" {
  name                    = "main-network"
  auto_create_subnetworks = false
  mtu                     = 1460
}

resource "google_compute_subnetwork" "private" {
  name          = "private-subnet"
  ip_cidr_range = "10.0.0.0/24"
  region        = "us-central1"
  network       = google_compute_network.main.id
}

resource "google_kms_keyring" "keyring" {
  name     = "my-keyring"
  location = "global"
}

resource "google_project" "my_project" {
  name       = "My Project"
  project_id = "my-project-12345"
}

# This line should be ignored because it contains "keyrings"
data "google_kms_keyring" "existing_keyring" {
  name     = "existing-keyring"
  location = "global"
}

# This line should be ignored because it contains "networks"
locals {
  network_config = {
    name = "test-network"
    cidr = "10.1.0.0/16"
  }
}

# This line should be ignored because it contains "subnetworks"
variable "subnetwork_config" {
  description = "Subnetwork configuration"
  type = object({
    name = string
    cidr = string
  })
}

# This line should be ignored because it contains "projects/"
resource "google_project_service" "apis" {
  project = "projects/my-project-12345"
  service = "compute.googleapis.com"
}

# This line should NOT be ignored (contains a potential secret)
variable "database_password" {
  description = "Database password"
  type        = string
  default     = "super-secret-password-123"
}

# This line should NOT be ignored (contains a potential secret)
resource "google_storage_bucket" "bucket" {
  name     = "my-secret-bucket"
  location = "US"
  
  # This should be flagged as a potential secret
  labels = {
    api_key = "sk-1234567890abcdef"
  }
}