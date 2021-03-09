import matplotlib.pyplot as plot
import matplotlib.image as mpimage
import numpy as np
import cv2 as OpenCV


# Setup Global Variables here



# Return an image frame or a frame from video
def GetFrame(ImagePath=0, VideoPath=0):
    # check if is a video 
    # check if it an image
    colorFrame = mpimage.imread(ImagePath)

    print("[INFO] : GetFrame() Image : Path = ", ImagePath, " Shape = ", np.shape(colorFrame))

    return colorFrame

# Return canny edges of a colored image
def GetCannyFrame(ColorFrame, LowThreshold, HighThreshold):
    grayScaleFrame = OpenCV.cvtColor(ColorFrame, OpenCV.COLOR_BGR2GRAY)
    thresholdRatio = HighThreshold/LowThreshold

    if (thresholdRatio < 2) | (thresholdRatio > 3):
        print("[WARN] : ProcessCannyFrame() : Recommended value for [HighThreshold/LowThreshold] is between : 2 & 3")

    cannyEdges     = OpenCV.Canny(grayScaleFrame, LowThreshold, HighThreshold)
    OpenCV.startWindowThread()
    OpenCV.namedWindow('Butterfly')
    plot.imshow(cannyEdges)

    return cannyEdges

# Return Polygon Enclosures
def GetPolygonEnclosure(PolygonLines):
    print("GetPolygonEnclosure() : ", np.shape(PolygonLines))

colorImageName = "test_images/SolidWhiteCurve.jpg"
colorFrame = mpimage.imread(colorImageName)
plot.imshow(colorFrame)
colorImage     = GetFrame(colorImageName)
GetCannyFrame(colorImage, 40, 150)