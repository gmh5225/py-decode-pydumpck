import os
from typing import Tuple
from .common import resources, current_path
import pydumpck.py_common_dump as dmp
import pydumpck.configuration as configuration
from .common.res_type import *
import shutil

def test_arch_file(res_type_arch: Tuple):
    file_path, target_type = res_type_arch
    output_dir = f'{os.path.dirname(file_path)}/output'
    configuration.thread_output_directory = output_dir
    configuration.progress_session_timeout = 120
    dumper = dmp.CommonDump()
    dumper.handle_arch_file(file_path)
    assert current_path != None, 'none'
    assert os.path.exists(output_dir), f'fail to run'
    shutil.rmtree(output_dir)