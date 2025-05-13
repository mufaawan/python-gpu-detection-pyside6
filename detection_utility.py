
import platform
import subprocess
import json

def get_nvidia_info():
    if platform.system() not in ["Windows", "Linux"]:
        return []
    try:
        import GPUtil
    except ImportError:
        return [{"type": "NVIDIA", "error": "GPUtil not installed"}]

    try:
        gpus = GPUtil.getGPUs()
        results = []
        for gpu in gpus:
            results.append({
                "name": gpu.name,
                "id": gpu.id,
                "type": "NVIDIA",
                "vendor": "NVIDIA Corporation",
                "memory": f"{gpu.memoryTotal} MB",
                "temperature": f"{gpu.temperature} C"
            })
        return results
    except Exception as e:
        return [{"type": "NVIDIA", "error": str(e)}]

def get_opencl_info():
    try:
        import pyopencl as cl
    except ImportError:
        return [{"type": "OpenCL", "error": "pyopencl not installed"}]

    gpus = []
    try:
        platforms = cl.get_platforms()
    except Exception:
        return [{"type": "OpenCL", "error": "No OpenCL platforms found"}]

    for platform_ in platforms:
        try:
            devices = platform_.get_devices(device_type=cl.device_type.GPU)
        except:
            continue
        for device in devices:
            try:
                if device.get_info(cl.device_info.HOST_UNIFIED_MEMORY):
                    continue
            except:
                pass

            if not device.get_info(cl.device_info.AVAILABLE):
                continue

            gpu = {}
            try:
                gpu["name"] = device.get_info(cl.device_info.BOARD_NAME_AMD)
                gpu["type"] = "AMD"
            except:
                continue
           

            try:
                gpu["vendor"] = device.vendor
            except:
                gpu["vendor"] = "Unknown"

            try:
                gpu["memory"] = f"{device.get_info(cl.device_info.GLOBAL_MEM_SIZE) / (1024 ** 2):.0f} MB"
            except:
                gpu["memory"] = "Unknown"

            gpus.append(gpu)
    return gpus

def get_macos_gpu_info():
    if platform.system() != "Darwin":
        return []

    try:
        output = subprocess.check_output(
            ["system_profiler", "SPDisplaysDataType", "-json"],
            universal_newlines=True
        )
        data = json.loads(output)
        gpu_info = data.get("SPDisplaysDataType", [])
        results = []
        for gpu in gpu_info:
            results.append({
                "name": gpu.get("sppci_model", "Unknown"),
                "type": "macOS",
                "vendor": gpu.get("sppci_vendor", "Unknown"),
                "memory": gpu.get("spdisplays_vram", "Unknown")
            })
        return results
    except Exception as e:
        return [{"type": "macOS", "error": str(e)}]
