# Blog Generation

## Tech stack

* AWS Bedrock
* AWS API gateway
* AWS Lambda
* AWS S3

![Block diagram of app.](../assets/blog/blog_e2e.png)

My first Hello World project in the world of GenAI involves crafting a 100-word blog post. I opted for the AWS Bedrock service, tapping into the Llama2 LLM model for this task. Among the array of LLM options offered by AWS Bedrock, Llama stood out for its cost-free accessibility. Built on the Transformer architecture, Llama models excel in processing input sequences of varying lengths and producing outputs of flexible sizes.

For our specific needs, we've selected the "Llama 2 chat 13 B" model. Leveraging AWS services, we've constructed an end-to-end solution primed for deployment in a production environment. API Gateway triggers a Lambda function housing our core logic, which interfaces with Llama APIs.

Employing a serverless architecture, we've crafted a Lambda function. API Gateway facilitates POST requests to this function, triggering the generation process. The resultant blog content is been uploaded to AWS S3 bucket.


The response is archived in the S3 bucket as a PDF document. For a comprehensive overview, refer to the complete code provided in the link below.

---