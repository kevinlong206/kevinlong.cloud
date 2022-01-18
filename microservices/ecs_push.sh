aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 934982441582.dkr.ecr.us-west-2.amazonaws.com
#docker build -t klong_profound .
docker tag docker-gs-ping:multistage 934982441582.dkr.ecr.us-west-2.amazonaws.com/klong_profound:latest
docker push 934982441582.dkr.ecr.us-west-2.amazonaws.com/klong_profound:latest
