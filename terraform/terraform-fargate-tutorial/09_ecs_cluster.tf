resource "aws_ecs_cluster" "my_ecs_cluster" {
  name = "${var.myapp_name}-ecscluster"
  capacity_providers = ["FARGATE"]

  default_capacity_provider_strategy {
    capacity_provider = "FARGATE"
  }

  setting {
    name  = "containerInsights"
    value = "disabled"
  }
}



resource "aws_ecs_task_definition" "myapp_task" {
  family = "${var.myapp_name}-family"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "256"
  memory                   = "1024"

  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
  
  container_definitions = jsonencode([
    {
      name      = "${var.myapp_name}-task"
      image     = "${var.my_app_dockerimage}"
      cpu       = 10
      memory    = 512
      essential = true
      portMappings = [
        {
          containerPort = 8080
          hostPort      = 8080
        }
      ]
    },
  ])
}





resource "aws_ecs_service" "my_service" {
  name            = "${var.myapp_name}-service"
  cluster         = aws_ecs_cluster.my_ecs_cluster.id
  task_definition = aws_ecs_task_definition.myapp_task.arn
  desired_count   = 3
  //iam_role        = aws_iam_role.foo.arn
  //depends_on      = [aws_iam_role_policy.foo]

  network_configuration {
    subnets = [
      aws_subnet.private1.id,
      aws_subnet.private2.id,

      
    ]
    security_groups = [
      aws_security_group.ingress_api.id,
      aws_security_group.egress_all.id,
    ]
  }


  capacity_provider_strategy {
    weight = 100
    capacity_provider = "FARGATE"
  }


  load_balancer {
    target_group_arn = aws_lb_target_group.my_loadbalancer.arn
    container_name   = "${var.myapp_name}-task"
    container_port   = 8080
  }
}