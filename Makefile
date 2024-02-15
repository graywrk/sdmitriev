run:
	docker network create web || true && docker-compose up --build

deploy:
	ansible-playbook -i cicd/inventory cicd/ansible/all.yml

qq:
	git add . && git commit -am "Auto commit" && git push && ansible-playbook -i cicd/ansible/inventory cicd/ansible/all.yml 
