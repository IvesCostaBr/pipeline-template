import os
import threading
from src.utils import show_log


def executor(data, provider: str, module: str = None, asyncer: bool = False):
    module_path = f"src.providers.{provider}"

    if not module:
        module = "default"
    module_path += f".{module}"

    try:
        function = getattr(__import__(
            module_path, fromlist=["exec"]), "exec")

    except Exception as ex:
        raise Exception(f"error execute step {str(ex)}")

    if asyncer:
        show_log.info("Executing step async -> {}:{}".format(provider, module))
        threading.Thread(target=function, args=(data)).start()
        return True

    result = function(data)
    return result
