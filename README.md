## monitor_calibrationer

flat 모니터와 curved 모니터에 각각 chess board 사진을 띄워서 calibration과 distortion correction을 해보는 간단한 테스트

테스트 전에는 curved 모니터로 chess board를 calibration과 distortion correction을 했을때 일그러짐이 심할 거라고 예상했지만 의외로
flat 모니터로 chess board를 calibration과 distortion correction을 했을때 일그러짐이 더 심했던거같다.

## flat.avi Camera Calibration Results

- The number of selected images = 10
- RMS error = 0.31737851753645974
- Camera matrix (K) =
  [[1.11361069e+03 0.00000000e+00 6.32623125e+02]
[0.00000000e+00 1.11380296e+03 3.74014938e+02]
[0.00000000e+00 0.00000000e+00 1.00000000e+00]]
- Distortion coefficient (k1, k2, p1, p2, k3, ...) = [ 5.31123153e-03 -1.41949715e+00 -1.70347456e-03 -1.24311832e-04
  7.40326177e+00]

## curved.avi Camera Calibration Results

- The number of selected images = 8
- RMS error = 1.0101675323493111
- Camera matrix (K) =
  [[1.22407575e+03 0.00000000e+00 6.63775166e+02]
[0.00000000e+00 1.24338160e+03 5.05569875e+02]
[0.00000000e+00 0.00000000e+00 1.00000000e+00]]
- Distortion coefficient (k1, k2, p1, p2, k3, ...) = [ 0.14512652 -0.35633017 0.04920413 0.00560403 1.6626042 ]
