import logging
import os
import json
import glob
import requests

def get_json():
    files = []
    for target in ['BM1684', 'BM1684X']:
        files.append(glob.glob(f'{target}_failed_cases.json'))
    return files

def post_failed_cases(sdk, fn):
    root = os.path.dirname(os.path.dirname(__file__))
    logging.info(f'Working dir {root}')

    with open(fn, 'r') as f:
        data = json.load(f)
    f.close()
    if len(data) == 0 or len(data["cases"]) == 0:
        logging.info(f'No model compilation failed!')
        return

    toolchain = sdk.split('_')[0]
    cmt_id = sdk.split('_')[1]
    target = fn.split('_')[0]
    case_names = [case["case_name"] for case in data["cases"]]

    with open('./README.md', 'r') as f:
        for line in f.readlines():
            for i in range(len(case_names)):
                case_name = case_names[i].replace('_', '\_')
                if case_name in line:
                    case_names[i] = line.split('|')[2].split('(')[1].split(')')[0]

    params = {"cases": [{"case_name": case_name,"toolchain": toolchain,"commit_sha": cmt_id,"target": target} for case_name in case_names]}

    params = f"{params}"
    json_param = {
        'JSON_PARAM': params
    }

    url = 'http://172.28.142.24:8092/job/model-zoo-regression/buildWithParameters'
    auth_info = os.environ.get('JENKINS_AUTH').split(':')
    auth = (auth_info[0], auth_info[1])
    print('Post failed cases to jenkins: ', url)
    print("json_param: ", json_param)
    response = requests.post(url, auth=auth, params=json_param)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Post failed cases to blame regression test')
    parser.add_argument(
        '--sdk', type=str, help='the version of toolchain sdk')
    args = parser.parse_args()

    files = get_json()
    if len(files) == 0:
        logging.info(f'No model compilation failed!')
        return

    for fn in files:
        post_failed_cases(args.sdk, fn[0])

if __name__ == '__main__':
    main()