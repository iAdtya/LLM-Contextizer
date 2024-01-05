from openai import OpenAI
import time

OPENAI_API_KEY='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'

client = OpenAI()

#Create file fr fine-tuning
file =client.files.create(
  file=open("genZ.jsonl", "rb"),
  purpose="fine-tune",
)

print(f"File ID: {file.id},File Status:{file.status}")

#create a finte-tuning job
job = client.fine_tuning.jobs.create(
  training_file = file.id,
  model="gpt-3.5-turbo-1106"
)

print(f"File ID: {job.id},File Status:{job.status}")

while True:
    time.sleep(10)  
    job = client.fine_tuning.jobs.retrieve(job.id)
    if job.status == 'succeeded':
        model_name = f"ft-{job.model}:suffix:{job.id}"
        print(f"Job ID: {job.id}, Final Job Status: {job.status}")
        print(f"Model Name: {model_name}")
        break
    elif job.status == 'failed':
        print(f"Job ID: {job.id}, Final Job Status: {job.status}")
        break
    else:
        print(f"Checking... Job ID: {job.id}, Current Job Status: {job.status}")