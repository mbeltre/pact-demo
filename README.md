# pact-demo
A simple demo to demonstrate how to work with the Pact Framework in python.

In this example we'll have a Provider `Memes-Service` and a Consumer 
`Memes-Website`. 

The `Memes-Website` will create a pact with the provider and publish it to
a pact broker. And the `Memes-Service` will download that pact and verify it.

# How to run it
You need to get a version of the pact broker running, you can find the 
instructions here: https://github.com/DiUS/pact_broker-docker

# Let's get services running
1. `git clone git@github.com:mbeltre/pact-demo.git`
2. `cd pact-demo`
3. `pip install -r requirements.txt`
4. Run the Memes-Service `python ./src/memes_service/app.py`
5. Open another terminal and go to the root directory, then run:
`python ./src/memes_website/app.py`

Now visit `http://localhost:5001/index`, you should see a very funny meme :)

# Creating a pact and uploading it to the broker
Run the following commands from the root directory:
1. `cd ./src/memes_website`
2. `ENV PYTHONPATH=. pytest`

A pact `memes-website-memes-service.json` should be generated.

Now let's upload that file to the broker:
1. `cd ../..`
2. `make push-pact`

If you go to `http://localhost`, you should see the pact on the pact broker.

# Verifying the pact on the provider
To verify the pact we need to run the provider service, in this case
`Memes-Service`. 

Run:
1. `make verify-pact`

That's see, you just created a pact, share using a pact broker and verified it.

If you want to learn more about the Pact Framework visit: https://docs.pact.io/
