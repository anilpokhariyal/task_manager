docker network create task_manger_network || true && docker-compose -f docker/docker-compose.yml build task-manager && docker-compose -f docker/docker-compose.yml up -d task-manager
