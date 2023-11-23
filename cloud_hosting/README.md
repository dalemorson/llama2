# Cloud Hosting

Taken from this [page](https://ai.meta.com/llama/get-started/).

## Amazon Web Services

AWS provides multiple ways to host your Llama models. (SageMaker Jumpstart, EC2, Bedrock etc). In this document we are going to outline the steps to host your models using SageMaker Jumpstart and Bedrock. You can refer to other offerings directly on the AWS site.

### Bedrock

A fully managed service that offers a choice of high performing foundation models, available via an API, to build generative AI applications, simplifying development while maintaining privacy and security. You can read more about the product here and follow instructions to use Llama 2 with Bedrock here.

### EC2 Instance

To deploy models on EC2 instances, you must first request access to the model from our Llama download form, Hugging Face or Kaggle. Once you have this model you can either deploy it on a Deep Learning AMI image that has both Pytorch and Cuda installed or create your own EC2 instance with GPUs and install all the required dependencies. For detailed instructions on how to set up your Deep Learning AMI image you can refer here or to set up your own EC2 instance here.

### SageMaker JumpStart

Amazon SageMaker enables ML practitioners to build, train and deploy machine learning models for any use case with fully managed infrastructure, tools and workflows. With SageMaker JumpStart, ML practitioners can choose from a broad selection of publicly available foundational models and deploy them on SageMaker Instances for model training and deployments. You can read more about it here.

## Cloudflare

### Workers AI

Is a serverless GPU-powered inference on Cloudflare’s global network. It’s an AI inference as a service platform, empowering developers to run AI models with just a few lines of code. Learn more about Workers AI here and look at the documentation here to get started to use Llama 2 models here.

## Google Cloud Platform (GCP) - Model Garden

GCP is a suite of cloud computing services that provides computing resources as well as virtual machines. Building on top of GCP services, Model Garden on Vertex AI offers infrastructure to jumpstart your ML project with a single place to discover, customize, and deploy a wide range of models. With more than 100 foundation models available to developers, you can deploy AI models with a few clicks as well as running fine-tuning tasks in Notebook in Google Colab.

### Vertex AI

We have collaborated with Vertex AI from Google Cloud to fully integrate Llama 2, offering pre-trained, chat and CodeLlama in various sizes. Getting started from here, note that you may need to request proper GPU computing quota as a prerequisite.

## Hugging Face

You must first request a download using the same email address as your Hugging Face account. After doing so, you can request access to any of the models on Hugging Face and within 1-2 days your account will be granted access to all versions.

## Kaggle

Kaggle is an online community of data scientists and machine learning engineers. It not only allows users to find datasets for building their AI models, but also allows users to search and discover hundreds of trained, ready-to-deploy machine learning models in one place. Moreover, community members can also publish their innovative works with these models as in Notebooks, backed by Google Cloud AI platform for computing resources and virtual machines.

We have collaborated with Kaggle to fully integrate Llama 2, offering pre-trained, chat and CodeLlama in various sizes. To download Llama 2 model artifacts from Kaggle, you must first request a download using the same email address as your Kaggle account. After doing so, you can request access to Llama 2 and Code Lama models. You get access to downloads once your request is processed.

## Microsoft Azure & Windows

With Microsoft Azure you can access Llama 2 in one of two ways, either by downloading the Llama 2 model and deploying it on a virtual machine or using Azure Model Catalog.

### Azure Virtual Machine

To run Llama with an Azure VM, you can set up your own VM or use Azure’s Data Science VM which comes with Pytorch, CUDA, NVIDIA System Management and other ML tools already installed. To use the Data Science VM, follow the instructions here to set one up. Make sure to set this VM up with a GPU enabled image. However, if you would like to set up your own VM, you can follow the quickstart instructions on the Microsoft site here. You can stop at the “Connect to virtual machine” step. Once you have a VM set up, you can follow the instructions here to access the models locally on the VM.

### Azure Model Catalog

Azure Model Catalog is a hub for exploring collections of foundation models. Built on top of Azure ML platform, Model Catalog provides options to run ML tasks such as fine-tuning and evaluation with just a few clicks. In general, it is a good starting point for beginner developers to try out their favorite models and also integrated with powerful tools for senior developers to build AI applications for production.

We have worked with Azure to fully integrate Llama 2 with Model Catalog, offering both pre-trained chat and CodeLlama models in various sizes. Please follow the instructions here to get started with.

### ONNX for Windows

ONNX is an open format built to represent machine learning models. It defines a common set of operators and a common file format to enable AI developers to use models with a variety of frameworks, tools, runtimes and compilers. One of the main advantages of using ONNX is that it allows models to be easily exported from one framework, such as TensorFlow, and imported into another framework, such as PyTorch.

Pairing with ONNX runtime, it would accelerate your development with a flexible interface to integrate hardware-specific libraries and essentially allows you to run ML tasks including inferencing on different platforms such as Windows easily.

Get started developing applications for Windows/PC with the official ONNX Llama 2 repo here and ONNX runtime here. Note that, to use the ONNX Llama 2 repo you will need to submit a request to download model artifacts from sub-repos. This request will be reviewed by the Microsoft ONNX team.