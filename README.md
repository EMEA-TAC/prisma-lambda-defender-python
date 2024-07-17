# prisma-lambda-defender-python
**Deploy serverless defender on AWS Lambda function**

Prisma Cloud Serverless Defenders protect serverless functions at runtime. Currently, Prisma Cloud supports AWS Lambda functions.

Serverless Defender protects serverless functions at runtime. It monitors your functions to ensure they execute as designed.

**Per-function policies let you control:**

- Process activity. Enables verification of launched subprocesses against policy.

- Network connections. Enables verification of inbound and outbound connections, and permits outbound connections to explicitly allowed domains.

- File system activity. Controls which parts of the file system functions can access.

- Prisma Cloud supports AWS Lambda functions (Linux) and Azure Functions (Windows only).

**Securing serverless functions**

To secure a serverless function, embed the Prisma Cloud Serverless Defender into it. The steps are:

1. (Optional) If you are not using a deployment framework like SAM or Serverless Framework, download a ZIP file that contains your function source code and dependencies.

2. Embed the Serverless Defender into the function.

3. Deploy using the Terraform template the function with the defender to AWS or upload the updated ZIP file to the cloud provider. 

4. Define a serverless protection runtime policy.

5. Define a serverless WAAS policy.

**Deploying the Terraform template.**

The provided example contains simple "Hello Prisma" function on python. 

1. Open Compute Console, and go to Manage > Defenders > Defenders: Deployed > Manual deploy > Single Defender.
2. The DNS name Serverless Defender uses to connect to your Compute Console is prepopulated for you.
3. In Choose Defender type, select Serverless.
4. In Runtime, select Python.
5. Download the Serverless Defender package to your workstation.
6. Unzip the Serverless Defender bundle into your terraform directory.
7. Generate the value for the TW_POLICY environment variable by specifying your function’s name and region. If Any is selected for region, only policies that contain * in the region label will be matched. Serverless Defender uses TW_POLICY to determine how to connect to Compute Console to retrieve policy and send audits. Copy the value generated for TW_POLICY, and add it as enviromental variable in to the template:
   
environment {
    variables = {
      TW_POLICY = ""
    }
  }
}

8. Deploy the edited terraform script.

   



