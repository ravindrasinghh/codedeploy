provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "example" {
  bucket = "my-test-codebuild"
  acl = "private"
  versioning {
    enabled = true
  }
}
