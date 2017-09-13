# pact-demo

# How to run it
You need to get a version of the pact broker running, you can find the 
instructions here: https://github.com/DiUS/pact_broker-docker

# Prerequisites
`pip install -r requirements.txt`

# Creating a pact and uploading it to the broker
Run the following commands from the root directory:
1. `cd ./src/memes_website/tests`
2. `ENV PYTHONPATH=. pytest`

A pact `memes-website-memes-service.json` should be genarated.

Now lets upload that file to the broker.
Go back to the root directory and run the following command:
`make push-pact`

If you go to `http://localhost`, you should see the pact on the pact broker.

# Verifying the pact on the provider
To verify the pact we need to run the priverder service, in this case
`Memes-Service`.
``

From the root directory run:
`make verify-pact`

That's see, you just created a pact, share using a pact broker and verified it.

If you want to learn more about the Pact Framework visit: https://docs.pact.io/
