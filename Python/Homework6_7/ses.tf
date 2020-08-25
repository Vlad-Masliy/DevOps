resource "aws_ses_email_identity" "source" {
  email = "vladyslav.maslii@nure.ua"
}

resource "aws_ses_email_identity" "destination" {
  email = "vlad.maslii2019@gmail.com"
}