run:
	docker network create web || true && docker-compose up
deploy:
	ansible-playbook -i cicd/inventory cicd/all.yml