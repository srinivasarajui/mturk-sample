import boto3


ACCESS_KEY='AKIAIRKIOKM7DBWKTEEQ'
SECRET_KEY='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'
session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
client = session.client(service_name='mturk',region_name='us-east-1')
user_balance = client.get_account_balance()
print("Your account balance is {}".format(user_balance['AvailableBalance']))

question_sample = open("question.xml", "r").read()

worker_requirements = [{
    'QualificationTypeId': '000000000000000000L0',
    'Comparator': 'GreaterThanOrEqualTo',
    'IntegerValues': [80],
    'RequiredToPreview': True,
}]

response = client.create_hit(
    MaxAssignments=3,
    LifetimeInSeconds=600,
    AssignmentDurationInSeconds=600,
    Reward="0.00",
    Title='Answer a simple question',
    Keywords='question, answer, research',
    Description='Answer a simple question. Created from mturk-code-samples.',
    Question=question_sample,
    QualificationRequirements=worker_requirements,
)

hit_type_id = response['HIT']['HITTypeId']
hit_id = response['HIT']['HITId']
print("\nCreated HIT: {}".format(hit_id))

#Created HIT: 37Y5RYYI1TR456H2ZG1WISQDM7OSX6
