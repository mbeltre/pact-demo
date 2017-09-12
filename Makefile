push-pact:
	push_pact --broker_url http://localhost \
	--provider Memes-Service --consumer Memes-Website \
	--pact_file  ./src/memes_website/memes-website-memes-service.json \
	--consumer_version 0.1.0 \
	--tag dev

verify-pact:
	pact-verifier --provider-base-url http://localhost:5000/ --pact-urls http://localhost/pacts/provider/Memes-Service/consumer/Memes-Website/latest





