import threading
import time
import pyrealsense2 as rs
import torch
import numpy as np
from custom_scripts.common.constants import (
    WRIST_CAM_SN,
    EXO_CAM_SN,
    TABLE_CAM_SN,
)

def get_sn(camera):
    if camera == 'wrist':
        return WRIST_CAM_SN
    elif camera == 'exo':
        return EXO_CAM_SN
    elif camera == 'table':
        return TABLE_CAM_SN
    else:
        raise ValueError("Invalid camera name. Choose 'wrist', 'exo', or 'table'.")


class RealSenseCamera:
    def __init__(self, camera, fps):
        self.camera = camera
        self.camera_sn = get_sn(self.camera)

        self.rs_config = rs.config()
        self.rs_config.enable_device(self.camera_sn)
        self.rs_config.enable_stream(rs.stream.color)

        self.rs_pipeline = rs.pipeline()
        self.rs_pipeline.start(self.rs_config)
        self.image_thread = threading.Thread(target=self.fetch_image_data, args=(self.rs_pipeline, self.camera))

        self.lock = threading.Lock()

        self.fps = fps


    def start_recording(self):
        self.image_thread.start()


    def fetch_image_data(self, rs_pipeline, cam):
        while True:
            t0 = time.time()
            frames = rs_pipeline.wait_for_frames()
            image = np.array(frames.get_color_frame().get_data()).astype(dtype = np.uint8)
            image = torch.from_numpy(image).permute(2,0,1).unsqueeze(0).to(dtype = torch.float32) / 255.0

            self.lock.acquire()
            self.image = image
            self.lock.release()

            t1 = time.time()
            time.sleep(max(0,1/self.fps-(t1-t0)))


    def get_camera_info(self):
        return self.camera.get_camera_info()

    def get_intrinsics(self):
        return self.camera.get_intrinsics()

    def get_extrinsics(self):
        return self.camera.get_extrinsics()

    def get_depth_frame(self):
        return self.camera.get_depth_frame()

    def get_color_frame(self):
        return self.camera.get_color_frame()