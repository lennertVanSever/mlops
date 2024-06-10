resource "aws_s3_bucket" "example" {
  bucket = "unique-mlops-bucket-123456"  # Name should be unique

  tags = {
    Name        = "MLOps bucket"
    Environment = "Dev"
  }
}
