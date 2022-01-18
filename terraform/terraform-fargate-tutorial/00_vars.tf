variable "region" {
  default = "us-west-2"
}

variable "myapp_name" {
  default = "klongapi"
}

# This DNS zone must already exist in route53 in your AWS account. 

variable "myapp_dnszone" {
  default = "kevinlong.cloud"
}

variable "myapp_hostname" {
  default = "klongapi.kevinlong.cloud"
}

variable "my_app_dockerimage" {
  default = "olliefr/docker-gs-ping"
}

variable "db_username" {
  default = "rds_user"
}