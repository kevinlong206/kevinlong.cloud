
data "aws_route53_zone" "my_dns_zone" {
  name         =  var.myapp_dnszone
}



resource "aws_route53_record" "alias_route53_record" {

  zone_id = data.aws_route53_zone.my_dns_zone.id 
  name    = var.myapp_hostname
  type    = "A"

  alias {
    name                   = aws_alb.my_loadbalancer.dns_name
    zone_id                = aws_alb.my_loadbalancer.zone_id
    evaluate_target_health = true
  }
}

resource "aws_route53_record" "acm_dns_record" {
  for_each = {
    for dvo in aws_acm_certificate.my_acm_cert.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.my_dns_zone.id
}