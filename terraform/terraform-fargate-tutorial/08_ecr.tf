resource "aws_ecr_repository" "my_container_registry" {
  name                 = "${var.myapp_name}-ecr"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  }
}
