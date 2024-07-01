import boto3
import botocore.config
import json
from datetime import datetime


def lambda_handler(event, context):
    # TODO implement
    event = json.loads(event['body'])
    topic = event['topic']

    generate_blog = blog_generate_using_bedrock(topic=topic)

    if generate_blog:
        current_time = datetime.now().strftime('%H%M%S')
        s3_key = f"blog_output/{current_time}.txt"
        s3_bucket_name = 'ambalgi-awsbedrock1'
        save_blog_details_s3(s3_key, s3_bucket_name, generate_blog)
    else:
        print("No blog was generated")

    return {
        'statusCode': 200,
        'body': json.dumps('Blog generation is completed!')
    }


def blog_generate_using_bedrock(topic: str) -> str:
    """
        {
            "modelId": "meta.llama2-13b-chat-v1",
            "contentType": "application/json",
            "accept": "application/json",
            "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
        }
    """
    prompt = f'<s>[INST]Human: Write a 100 words blog on the topic {topic} Assistant: [/INST]'
    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }
    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="us-west-2",
            config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 2})
        )
        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId="meta.llama2-13b-chat-v1"
        )
        response_content = response.get('body').read()
        response_data = json.loads(response_content)
        print(response_data)
        return response_data['generation']
    except Exception as e:
        print(f"Error occurred with {e}")
        return ""


def save_blog_details_s3(s3_key, s3_bucket, generate_blog):
    s3 = boto3.client('s3')
    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body= generate_blog)
    except Exception as e:
        print(e)
