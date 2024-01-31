from engine.Camera import *

camera: Camera = Camera(1920, 1080)
follow: Follow = Follow(camera)
bd: BorderFollow = BorderFollow(camera, (250,250), (500,500))

camera.setmethod(follow)