terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "jenkins-server" {
  ami           = "ami-0aa7d40eeae50c9a9"
  instance_type = "t2.micro"
  

  tags = {
    Name = "Jenkins-prod"
  }
  
  user_data              = <<EOF
    #!/bin/bash
    yum update -y
     yum update –y
    wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
    rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
    yum upgrade -y
    amazon-linux-extras install java-openjdk11 -y
    yum install jenkins -y
    systemctl enable jenkins
    systemctl start jenkins
    EOF
}
resource "aws_security_group" "jenkinssg" {
  name        = "jenkinssg"
  description = "Allow SSH and HTTP Traffic"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "myjenkinsartifactsprod222023" {
  bucket = "myjenkinsartifactsprod222023"
  
}