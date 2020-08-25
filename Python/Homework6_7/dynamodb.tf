resource "aws_dynamodb_table" "example" {
  name           = "Python_Homework_7"
  read_capacity  = 10
  write_capacity = 10
  hash_key       = "Download_files"

  attribute {
    name = "Download_files"
    type = "S"
  }
}