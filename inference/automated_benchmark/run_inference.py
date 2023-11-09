import subprocess
import argparse
from pathlib import Path
import click
import sys
import typer

def main():

    path_to_model = ""
    aws_role = ""
    huggingface_token = ""
    huggingface_repo = ""
    aws_access_key_id = ""
    aws_secret_access_key = ""
    aws_session_token = ""

    server = typer.prompt("Server")
    if server == "ray":
        answer = typer.prompt("Do you want to use local folder with model files? [Y/n]")
        if answer.lower() == "y":
            path_to_model = typer.prompt("Path to model")
        else:
            huggingface_token = typer.prompt("HuggingFace token")
            huggingface_repo = typer.prompt("HuggingFace repository")
    else:
        huggingface_token = typer.prompt("HuggingFace token")
        huggingface_repo = typer.prompt("HuggingFace repository")
    model_type = typer.prompt("Model type")
    task = typer.prompt("Task")

    if server == "tgi_sagemaker":
        aws_role = typer.prompt("AWS Sagemaker Execution Role")
        aws_access_key_id = typer.prompt("aws_access_key_id")
        aws_secret_access_key = typer.prompt("aws_secret_access_key")
        aws_session_token = typer.prompt("aws_session_token")

    subprocess.run(["chmod", "+x", f"./script_inference.sh"])
    subprocess.run([f"./script_inference.sh", huggingface_repo, huggingface_token,
                                        model_type, task, server, path_to_model, aws_role,
                                        aws_access_key_id, aws_secret_access_key, aws_session_token])
    
if __name__ == '__main__':
    main()