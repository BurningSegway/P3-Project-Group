;; Auto-generated. Do not edit!


(when (boundp 'wsg_gripper::GripperCommand)
  (if (not (find-package "WSG_GRIPPER"))
    (make-package "WSG_GRIPPER"))
  (shadow 'GripperCommand (find-package "WSG_GRIPPER")))
(unless (find-package "WSG_GRIPPER::GRIPPERCOMMAND")
  (make-package "WSG_GRIPPER::GRIPPERCOMMAND"))
(unless (find-package "WSG_GRIPPER::GRIPPERCOMMANDREQUEST")
  (make-package "WSG_GRIPPER::GRIPPERCOMMANDREQUEST"))
(unless (find-package "WSG_GRIPPER::GRIPPERCOMMANDRESPONSE")
  (make-package "WSG_GRIPPER::GRIPPERCOMMANDRESPONSE"))

(in-package "ROS")





(defclass wsg_gripper::GripperCommandRequest
  :super ros::object
  :slots (_command ))

(defmethod wsg_gripper::GripperCommandRequest
  (:init
   (&key
    ((:command __command) "")
    )
   (send-super :init)
   (setq _command (string __command))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass wsg_gripper::GripperCommandResponse
  :super ros::object
  :slots (_response ))

(defmethod wsg_gripper::GripperCommandResponse
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

(defclass wsg_gripper::GripperCommand
  :super ros::object
  :slots ())

(setf (get wsg_gripper::GripperCommand :md5sum-) "22c7c465d64c7e74c6ae22029c7ca150")
(setf (get wsg_gripper::GripperCommand :datatype-) "wsg_gripper/GripperCommand")
(setf (get wsg_gripper::GripperCommand :request) wsg_gripper::GripperCommandRequest)
(setf (get wsg_gripper::GripperCommand :response) wsg_gripper::GripperCommandResponse)

(defmethod wsg_gripper::GripperCommandRequest
  (:response () (instance wsg_gripper::GripperCommandResponse :init)))

(setf (get wsg_gripper::GripperCommandRequest :md5sum-) "22c7c465d64c7e74c6ae22029c7ca150")
(setf (get wsg_gripper::GripperCommandRequest :datatype-) "wsg_gripper/GripperCommandRequest")
(setf (get wsg_gripper::GripperCommandRequest :definition-)
      "string command
---
string response
")

(setf (get wsg_gripper::GripperCommandResponse :md5sum-) "22c7c465d64c7e74c6ae22029c7ca150")
(setf (get wsg_gripper::GripperCommandResponse :datatype-) "wsg_gripper/GripperCommandResponse")
(setf (get wsg_gripper::GripperCommandResponse :definition-)
      "string command
---
string response
")



(provide :wsg_gripper/GripperCommand "22c7c465d64c7e74c6ae22029c7ca150")


