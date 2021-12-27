---
title: "Infrastructure as Code and Continuous Delivery using Terraform, GitHub Actions and AWS Fargate"
date: 2021-12-26T12:41:16-08:00
draft: false 
---
#
## Background

This tutorial aims to cover all the basics involved in setting up cloud infrastructure for continuous delivery of a microservice to AWS Fargate, automating everything, with as few manual steps as possible.

There is a lot of information to cover, and it is by no means exhaustive, for example it is scoped to a single service and does not cover integration strategies.

I assume you understand the basics of cloud computing and AWS services, what Terraform is, what a docker container is, etc.

It is important to note that while most of the services provisioned by these code examples are eligible for the AWS "Free Tier", *not* all of them are and you *will* incur some cost if you follow this. The charges should be negligable (dollars?), but this is 100% on you.

### What is Fargate though? Why Fargate?
Fargate is a "serverless" version of "Elastic Container Service", meaning you do not operate or manage any virtual machines (EC2 instances), that is all handled by AWS. I chose it because I had not personally used it before, and understand that it is growing in popularity. My understanding is that for smaller/lower traffic projects, Fargate can have significant cost savings over traditional ECS or Kubernetes, but for larger sites the cost may be higher.



## Initial Setup / Prerequisites
1. AWS account )If it is less than 1 year since creation, most of what is provisioned by the terraform in this tutorial will be in the "free tier")
2. GitHub account and setup a github repo (or fork mine)
3. A domain name or subdomain (and access to set the nameservers for the domain)


{{<github repo="kevinlong206/profound" file="terraform/00_vars.tf" lang="hcl" options="lineNos=table">}}
TEST

Ok then. Here be go blogging again

sdsd