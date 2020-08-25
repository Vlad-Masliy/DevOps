resource "aws_s3_bucket" "bucket" {
  bucket = "my-bucket-for-python-cdp-h7"
  acl    = "private"

}