resource "aws_s3_bucket" "example1" {
  bucket = "unique-mlops-bucket-1"  # Name should be unique

  tags = {
    Name        = "MLOps bucket 1"
    Environment = "Dev"
  }
}
