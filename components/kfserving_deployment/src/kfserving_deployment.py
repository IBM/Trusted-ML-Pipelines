# Copyright 2019 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import argparse
import requests

from app import run_safe

def get_secret(path):
    with open(path, 'r') as f:
        cred = f.readline().strip('\'')
    f.close()
    return cred

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_id', type=str, help='Training model id', default="training-dummy")
    parser.add_argument('--metric_path', type=str, help='Path for deployment output', default="/tmp/log.txt")
    parser.add_argument('--cleanup', type=bool, help='Cleanup previous model deployments', default=False)
    parser.add_argument('--model_serving_image', type=str, help='Model serving container image', default="tomcli/,:pytorch")
    parser.add_argument('--deployment_name', type=str, help='Model Deployment Name', default='model-serving')
    parser.add_argument('--model_class_name', type=str, help='PyTorch model class name', default='ModelClass')
    parser.add_argument('--model_file_name', type=str, help='Model binary filename', default='model.pt')
    parser.add_argument('--model_class_file', type=str, help='File that contains the PyTorch model class', default='model_class.py')

    args = parser.parse_args()

    model_id = args.model_id
    metric_path = args.metric_path
    cleanup = args.cleanup
    model_serving_image = args.model_serving_image
    model_class_name = args.model_class_name
    model_class_file = args.model_class_file
    deployment_name = args.deployment_name
    model_file_name = args.model_file_name
    namespace = "default"  # TODO: Parametize namespace when kubeflow supports user auth.

    s3_url = get_secret("/app/secrets/s3_url")
    bucket_name = get_secret("/app/secrets/result_bucket")
    s3_username = get_secret("/app/secrets/s3_access_key_id")
    s3_password = get_secret("/app/secrets/s3_secret_access_key")
    knative_ingress = get_secret("/app/secrets/knative_ingress")

    try:
        local_cluster_deployment = str(get_secret("/app/secrets/local_cluster_deployment").lower()) == 'true'
    except Exception as e:
        local_cluster_deployment = False

    try:
        knative_custom_domain = get_secret("/app/secrets/knative_custom_domain")
    except Exception as e:
        knative_custom_domain = 'example.com'

    if local_cluster_deployment:
        kfserving_url = None
    else:
        kfserving_url = get_secret("/app/secrets/kfserving_url")

    # Model Deployment parameters
    formData = {
        "deployment_name": deployment_name,
        "container_image": model_serving_image,
        "model_file_name": model_file_name,
        "check_status_only": False,
        "model_class_name": model_class_name,
        "model_class_file": model_class_file,
        "endpoint_url": s3_url,
        "access_key_id": s3_username,
        "secret_access_key": s3_password,
        "training_results_bucket": bucket_name,
        "training_id": model_id,
    }

    # Deploy model with Knative route.
    if cleanup:
        if local_cluster_deployment:
            # Using K8s api
            metrics = run_safe(formData, "DELETE")
        else:
            response = requests.delete(kfserving_url, params=formData)
            metrics = response.json()
        print("Successfully cleanup old deployments")
    else:
        if local_cluster_deployment:
            # Using K8s api
            metrics = run_safe(formData, "POST")
        else:
            response = requests.post(kfserving_url, json=formData)
            metrics = response.json()

        # Print out the necessary endpoints and debugging outputs.
        metrics['Prediction_Host'] = deployment_name + "." + namespace + "." + knative_custom_domain
        metrics['Prediction_Endpoint'] = knative_ingress
        # print("Debugging outputs:")
        # print(metrics)
        metrics.pop('details', None)

        print("\n\nEndpoint IP for these models: " + metrics['Prediction_Endpoint'] + " . Model prediction host is " + metrics['Prediction_Host'])

    with open(metric_path, "w") as report:
        report.write(json.dumps(metrics))
