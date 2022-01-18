
resource "aws_lb_target_group" "my_loadbalancer" {
  name        = "${var.myapp_name}-tg"
  port        = 8080
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = aws_vpc.my_vpc.id

  health_check {
    port = 8080
    enabled = true
    path    = "/"
  }

  depends_on = [aws_alb.my_loadbalancer]
}

resource "aws_alb" "my_loadbalancer" {
  name               = "${var.myapp_name}-lb"
  internal           = false
  load_balancer_type = "application"

  subnets = [
    aws_subnet.public1.id,
    aws_subnet.public2.id
  ]

  security_groups = [
    aws_security_group.http.id,
    aws_security_group.https.id,
    aws_security_group.egress_all.id,
  ]

  depends_on = [aws_internet_gateway.igw]
}

resource "aws_alb_listener" "my_loadbalancer_http" {
  load_balancer_arn = aws_alb.my_loadbalancer.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type = "redirect"

    redirect {
      port        = "443"
      protocol    = "HTTPS"
      status_code = "HTTP_301"
    }
  }
}

resource "aws_alb_listener" "my_loadbalancer_https" {
  load_balancer_arn = aws_alb.my_loadbalancer.arn
  port              = "443"
  protocol          = "HTTPS"
  certificate_arn   = aws_acm_certificate.my_acm_cert.arn

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.my_loadbalancer.arn
  }
}

output "alb_url" {
  value = "http://${aws_alb.my_loadbalancer.dns_name}"
}