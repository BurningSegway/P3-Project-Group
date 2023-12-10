;; Auto-generated. Do not edit!


(when (boundp 'realsense_ting_controller::ImageCapture)
  (if (not (find-package "REALSENSE_TING_CONTROLLER"))
    (make-package "REALSENSE_TING_CONTROLLER"))
  (shadow 'ImageCapture (find-package "REALSENSE_TING_CONTROLLER")))
(unless (find-package "REALSENSE_TING_CONTROLLER::IMAGECAPTURE")
  (make-package "REALSENSE_TING_CONTROLLER::IMAGECAPTURE"))
(unless (find-package "REALSENSE_TING_CONTROLLER::IMAGECAPTUREREQUEST")
  (make-package "REALSENSE_TING_CONTROLLER::IMAGECAPTUREREQUEST"))
(unless (find-package "REALSENSE_TING_CONTROLLER::IMAGECAPTURERESPONSE")
  (make-package "REALSENSE_TING_CONTROLLER::IMAGECAPTURERESPONSE"))

(in-package "ROS")





(defclass realsense_ting_controller::ImageCaptureRequest
  :super ros::object
  :slots (_request ))

(defmethod realsense_ting_controller::ImageCaptureRequest
  (:init
   (&key
    ((:request __request) "")
    )
   (send-super :init)
   (setq _request (string __request))
   self)
  (:request
   (&optional __request)
   (if __request (setq _request __request)) _request)
  (:serialization-length
   ()
   (+
    ;; string _request
    4 (length _request)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _request
       (write-long (length _request) s) (princ _request s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _request
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _request (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass realsense_ting_controller::ImageCaptureResponse
  :super ros::object
  :slots (_response ))

(defmethod realsense_ting_controller::ImageCaptureResponse
  (:init
   (&key
    ((:response __response) "")
    )
   (send-super :init)
   (setq _response (string __response))
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; string _response
    4 (length _response)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _response
       (write-long (length _response) s) (princ _response s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _response
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _response (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass realsense_ting_controller::ImageCapture
  :super ros::object
  :slots ())

(setf (get realsense_ting_controller::ImageCapture :md5sum-) "33ea4e5aeb30f5913da681ca459d55f3")
(setf (get realsense_ting_controller::ImageCapture :datatype-) "realsense_ting_controller/ImageCapture")
(setf (get realsense_ting_controller::ImageCapture :request) realsense_ting_controller::ImageCaptureRequest)
(setf (get realsense_ting_controller::ImageCapture :response) realsense_ting_controller::ImageCaptureResponse)

(defmethod realsense_ting_controller::ImageCaptureRequest
  (:response () (instance realsense_ting_controller::ImageCaptureResponse :init)))

(setf (get realsense_ting_controller::ImageCaptureRequest :md5sum-) "33ea4e5aeb30f5913da681ca459d55f3")
(setf (get realsense_ting_controller::ImageCaptureRequest :datatype-) "realsense_ting_controller/ImageCaptureRequest")
(setf (get realsense_ting_controller::ImageCaptureRequest :definition-)
      "string request
---
string response
")

(setf (get realsense_ting_controller::ImageCaptureResponse :md5sum-) "33ea4e5aeb30f5913da681ca459d55f3")
(setf (get realsense_ting_controller::ImageCaptureResponse :datatype-) "realsense_ting_controller/ImageCaptureResponse")
(setf (get realsense_ting_controller::ImageCaptureResponse :definition-)
      "string request
---
string response
")



(provide :realsense_ting_controller/ImageCapture "33ea4e5aeb30f5913da681ca459d55f3")


