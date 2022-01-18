


# Generate a random password for the RDS database user, and store it in AWS "Secrets Manager"
resource "random_password" "my_rds_password"{
  length           = 16
  special          = true
  override_special = "_!%^"
}

resource "aws_secretsmanager_secret" "my_rds_password" {
  name = "${var.myapp_name}-rds_password"
}

resource "aws_secretsmanager_secret_version" "my_rds_password" {
  secret_id = aws_secretsmanager_secret.my_rds_password.id
  secret_string = random_password.my_rds_password.result
}

# Same thing for the database username, but instead of randomly generated,
# we take it from a terraform variable.

resource "aws_secretsmanager_secret" "my_rds_username" {
  name = "${var.myapp_name}-rds_password"
}

resource "aws_secretsmanager_secret_version" "my_rds_username" {
  secret_id = aws_secretsmanager_secret.my_rds_username.id
  secret_string = var.db_username
}