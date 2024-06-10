resource "aws_s3_bucket" "example" {
  bucket = "unique-mlops-bucket-123456"  # Name should be unique

  tags = {
    Name        = "MLOps bucket"
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_acl" "example_acl" {
  bucket = aws_s3_bucket.example.id
  acl    = "private"
}
