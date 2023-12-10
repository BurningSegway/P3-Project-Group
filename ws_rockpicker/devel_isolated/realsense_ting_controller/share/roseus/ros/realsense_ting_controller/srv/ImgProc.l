;; Auto-generated. Do not edit!


(when (boundp 'realsense_ting_controller::ImgProc)
  (if (not (find-package "REALSENSE_TING_CONTROLLER"))
    (make-package "REALSENSE_TING_CONTROLLER"))
  (shadow 'ImgProc (find-package "REALSENSE_TING_CONTROLLER")))
(unless (find-package "REALSENSE_TING_CONTROLLER::IMGPROC")
  (make-package "REALSENSE_TING_CONTROLLER::IMGPROC"))
(unless (find-package "REALSENSE_TING_CONTROLLER::IMGPROCREQUEST")
  (make-package "REALSENSE_TING_CONTROLLER::IMGPROCREQUEST"))
(unless (find-package "REALSENSE_TING_CONTROLLER::IMGPROCRESPONSE")
  (make-package "REALSENSE_TING_CONTROLLER::IMGPROCRESPONSE"))

(in-package "ROS")





(defclass realsense_ting_controller::ImgProcRequest
  :super ros::object
  :slots (_request ))

(defmethod realsense_ting_controller::ImgProcRequest
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

(defclass realsense_ting_controller::ImgProcResponse
  :super ros::object
  :slots (_response ))

(defmethod realsense_ting_controller::ImgProcResponse
  (:init
   (&key
    ((:response __response) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _response __response)
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; float32[] _response
    (* 4    (length _response)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _response
     (write-long (length _response) s)
     (dotimes (i (length _response))
       (sys::poke (elt _response i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _response
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _response (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _response i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(defclass realsense_ting_controller::ImgProc
  :super ros::object
  :slots ())

(setf (get realsense_ting_controller::ImgProc :md5sum-) "27a3ac67f0bd767a8424b890cbe335fe")
(setf (get realsense_ting_controller::ImgProc :datatype-) "realsense_ting_controller/ImgProc")
(setf (get realsense_ting_controller::ImgProc :request) realsense_ting_controller::ImgProcRequest)
(setf (get realsense_ting_controller::ImgProc :response) realsense_ting_controller::ImgProcResponse)

(defmethod realsense_ting_controller::ImgProcRequest
  (:response () (instance realsense_ting_controller::ImgProcResponse :init)))

(setf (get realsense_ting_controller::ImgProcRequest :md5sum-) "27a3ac67f0bd767a8424b890cbe335fe")
(setf (get realsense_ting_controller::ImgProcRequest :datatype-) "realsense_ting_controller/ImgProcRequest")
(setf (get realsense_ting_controller::ImgProcRequest :definition-)
      "string request
---
float32[] response
")

(setf (get realsense_ting_controller::ImgProcResponse :md5sum-) "27a3ac67f0bd767a8424b890cbe335fe")
(setf (get realsense_ting_controller::ImgProcResponse :datatype-) "realsense_ting_controller/ImgProcResponse")
(setf (get realsense_ting_controller::ImgProcResponse :definition-)
      "string request
---
float32[] response
")



(provide :realsense_ting_controller/ImgProc "27a3ac67f0bd767a8424b890cbe335fe")


