resource "aws_s3_bucket" "example" {
  bucket = "mlops-bucket"
  acl    = "private"

  tags = {
    Name        = "MLOps bucket"
    Environment = "Dev"
  }
}
