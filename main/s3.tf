provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "example" {
  bucket = "my-test-s3-terraform-bucket-git-build-52"
  acl = "private"
  versioning {
    enabled = true
  }
}
