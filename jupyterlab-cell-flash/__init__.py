import json
import os.path as osp

HERE = osp.abspath(osp.dirname(__file__))

with open(osp.join(HERE, 'static', 'package.json')) as fid:
    data = json.load(fid)

__version__ = data['version']


def _jupyter_labextension_paths():
    return [{
        'src': 'static',
        'dest': data['name']
    }]
