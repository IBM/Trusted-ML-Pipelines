# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument('--params', type=str, required=True)
    parser.add_argument('--secret-name', type=str)
    parser.add_argument('--output-secret-name-file', type=str, default='/tmp/secret_name')
    args = parser.parse_args()

    # download config file
    # the default creds.ini is in the public accesible github repo
    import subprocess
    import os
    json_params = json.loads(args.params)

    secret_name = args.secret_name

    try:
        command = ['kubectl', 'delete', 'secret', secret_name]
        subprocess.run(command, check=True)
    except Exception as e:
        print('No previous secret: ' + secret_name + '. Secret deletion is not performed.')

    # gather all secrets
    command = ['kubectl', 'create', 'secret', 'generic', secret_name]

    for attribute, value in json_params.items():
        command.append('--from-literal=%s=\'%s\'' % (attribute, value))

    # create the secret
    subprocess.run(command, check=True)

    # verify secret is created
    subprocess.run(['kubectl', 'describe', 'secret', secret_name], check=True)

    # indicate that secret is created and pass the secret name forward
    from pathlib import Path
    Path(args.output_secret_name_file).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output_secret_name_file).write_text(secret_name)
