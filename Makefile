run:
	docker network create web || true && docker-compose up

deploy:
	ansible-playbook -i cicd/inventory cicd/all.yml

make qq:
	git add . && git commit -am "Auto commit" && git push && ansible-playbook -i cicd/inventory cicd/all.yml 