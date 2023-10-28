from engine.Camera import *

camera: Camera = Camera(1920, 1080)
follow: Follow = Follow(camera)

camera.setmethod(follow)