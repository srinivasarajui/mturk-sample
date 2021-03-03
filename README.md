# mturk sample python code

A sample Python Project to explore the API's of [Amazon Mechanical Turk](https://www.mturk.com) (MTurk)

This code is simplified version from [here](https://github.com/aws-samples/mturk-code-samples/tree/master/Python)

You can explore the full API reference documentation [here](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/WhatIs.html).


## Using this repo.
Create a .env from .env.sample file and place correct AWS key values in .env file.

Run main.py to create task( HIT )
Run retrieveAndApproveHitSample.py to get task status and approve the response.
Note: please update hit_id in retrieveAndApproveHitSample.py based on your env


Next Step is to setup [Developer Sandbox](https://requestersandbox.mturk.com/) accounts as described [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkGettingStartedGuide/SetUp.html) and Use it for development and testing.