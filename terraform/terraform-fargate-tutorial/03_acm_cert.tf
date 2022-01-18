resource "aws_acm_certificate" "my_acm_cert" {
  domain_name       = var.myapp_hostname
  validation_method = "DNS"
}

output "domain_validations" {
  value = aws_acm_certificate.my_acm_cert.domain_validation_options
}