import boto3
from decouple import config
from xml.dom.minidom import parseString

ACCESS_KEY=config('ACCESS_KEY')
SECRET_KEY=config('SECRET_KEY')
hit_id = '37Y5RYYI1TR456H2ZG1WISQDM7OSX6'
session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)
client = session.client(service_name='mturk',region_name='us-east-1')
hit = client.get_hit(HITId=hit_id)
print('Hit {} status: {}'.format(hit_id, hit['HIT']['HITStatus']))

response = client.list_assignments_for_hit(
    HITId=hit_id,
    AssignmentStatuses=['Submitted', 'Approved'],
    MaxResults=10,
)

assignments = response['Assignments']

print('The number of submitted assignments is {}'.format(len(assignments)))
for assignment in assignments:
    worker_id = assignment['WorkerId']
    assignment_id = assignment['AssignmentId']
    answer_xml = parseString(assignment['Answer'])

    # the answer is an xml document. we pull out the value of the first
    # //QuestionFormAnswers/Answer/FreeText
    answer = answer_xml.getElementsByTagName('FreeText')[0]
    # See https://stackoverflow.com/questions/317413
    only_answer = " ".join(t.nodeValue for t in answer.childNodes if t.nodeType == t.TEXT_NODE)

    print('The Worker with ID {} submitted assignment {} and gave the answer "{}"'.format(worker_id, assignment_id, only_answer))

    # Approve the Assignment (if it hasn't already been approved)
    if assignment['AssignmentStatus'] == 'Submitted':
        print('Approving Assignment {}'.format(assignment_id))
        client.approve_assignment(
            AssignmentId=assignment_id,
            RequesterFeedback='good',
            OverrideRejection=False,
        )