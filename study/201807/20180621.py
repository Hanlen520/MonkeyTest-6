#!/user/bin/env python
# -*- coding:utf-8 -*-
from httprunner import HttpRunner
import time,os,io,yaml

if __name__ == '__main__':
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H-%M-%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s-%03d" % (data_head, data_secs)

    kwargs = {
        "failfast": False,
    }
    runner = HttpRunner(**kwargs)

    testcase_dir_path = os.path.join(os.getcwd(), "suite")
    # testcase_dir_path = os.path.join(testcase_dir_path, time_stamp)

    url = "/v1/init/version"
    method = 'get'

    base_url='http://api.sdhh.51lianqian.net:7035'
    config = {
        'config': {
            'name': 'base_url config',
            'request': {
                'base_url':base_url
            }
        }
    }
    testcase_list = []

    testcase_list.append(config)
    req={'method':method,'url':url}
    req1={'name':'find','request':req}

    testcase_list.append({'test':req1})
    with io.open('find' + '.yml', 'w', encoding='utf-8') as stream:
        yaml.dump(testcase_list, stream, indent=4, default_flow_style=False, encoding='utf-8')

    runner.run('find.yml')