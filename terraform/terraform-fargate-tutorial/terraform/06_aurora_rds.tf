
data "aws_secretsmanager_secret_version" "creds" {
  # Fill in the name you gave to your secret
  secret_id = "master_rds_password"
}

locals {
  db_creds = jsondecode(
    data.aws_secretsmanager_secret_version.creds.secret_string
  )
}



resource "aws_db_subnet_group" "db_subnet_group" {
  name       = "db_subnet_group"
  subnet_ids = [aws_subnet.private1.id, aws_subnet.private2.id]

  tags = {
    Name = "My DB subnet group"
  }
}



resource "aws_db_instance" "my_rds_db" {
  identifier             = "${var.myapp_name}-db"
  instance_class         = "db.t2.micro"
  allocated_storage      = 5
  engine                 = "mysql"
  engine_version         = "8.0"
  username = local.db_creds.master_username
  password = local.db_creds.master_password
  db_subnet_group_name   = aws_db_subnet_group.db_subnet_group.name
  vpc_security_group_ids = [aws_security_group.rds.id]
  parameter_group_name   = aws_db_parameter_group.my_rds_db.name
  publicly_accessible    = true
  skip_final_snapshot    = true
}


resource "aws_db_parameter_group" "my_rds_db" {
  name   = "${var.myapp_name}-dbparams"
  family = "mysql8.0"

/*   parameter {
    name  = "log_connections"
    value = "1"
  } */
}