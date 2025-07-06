import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    response = glue.start_job_run(JobName='extract_to_csv')
    return {"status": "Job started", "run_id": response['JobRunId']}
