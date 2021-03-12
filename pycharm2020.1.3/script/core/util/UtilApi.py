import asyncio
from typing import Callable
# from TcpServer import ev_loop


# try:
#     ev_loop =
# except RuntimeError:
#     ev_loop = None


# usage: r = await AioApi.async_wrap(lambda: requests.request("GET", 'http://baidu.com', timeout=2))
# lambda关键字不可少
from common import gr


def async_wrap(func: Callable):
    try:
        return asyncio.get_running_loop().run_in_executor(None, func)
    except RuntimeError:
        pass  # 正常情况不可能会发生调用此async_wrap比server启动还要早, 所以直接pass


def get_global_entity_mailbox(entity_unique_name):
    return gr.etcd_service_node.get_entity_info(entity_unique_name)


def register_entity_globally():
    pass


def register_entity_to_etcd(entity, name, tag=None):
    ip = gr.local_ip
    port = gr.local_port


def unregister_entity_from_etcd(name):
    pass