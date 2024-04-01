import numpy as np
import cv2 as cv

# The given video and calibration data
video_file = 'flat.avi'
K = np.array(  [[1.11361069e+03, 0.00000000e+00, 6.32623125e+02],
[0.00000000e+00, 1.11380296e+03, 3.74014938e+02],
[0.00000000e+00, 0.00000000e+00, 1.00000000e+00]]) # Derived from `calibrate_camera.py`
dist_coeff = np.array([ 5.31123153e-03, -1.41949715e+00, -1.70347456e-03, -1.24311832e-04, 7.40326177e+00])

# Open a video
video = cv.VideoCapture(video_file)
assert video.isOpened(), 'Cannot read the given input, ' + video_file

# Run distortion correction
show_rectify = True
map1, map2 = None, None
while True:
    # Read an image from the video
    valid, img = video.read()
    if not valid:
        break

    # Rectify geometric distortion (Alternative: `cv.undistort()`)
    info = "Original"
    if show_rectify:
        if map1 is None or map2 is None:
            map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
        img = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
        info = "Rectified"
    cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    # Show the image and process the key event
    cv.imshow("Geometric Distortion Correction", img)
    key = cv.waitKey(10)
    if key == ord(' '):     # Space: Pause
        key = cv.waitKey()
    if key == 27:           # ESC: Exit
        break
    elif key == ord('\t'):  # Tab: Toggle the mode
        show_rectify = not show_rectify

video.release()
cv.destroyAllWindows()