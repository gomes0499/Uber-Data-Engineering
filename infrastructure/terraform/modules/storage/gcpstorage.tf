resource "google_storage_bucket" "raw_data_bucket" {
  name          = "wu7raw"
  location      = "US"
  force_destroy = true

  uniform_bucket_level_access = true
}

resource "google_storage_bucket" "processed_data_bucket" {
  name          = "wu7process"
  location      = "US"
  force_destroy = true

  uniform_bucket_level_access = true
}
