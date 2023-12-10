; Auto-generated. Do not edit!


(cl:in-package realsense_ting_controller-srv)


;//! \htmlinclude ImageCapture-request.msg.html

(cl:defclass <ImageCapture-request> (roslisp-msg-protocol:ros-message)
  ((request
    :reader request
    :initarg :request
    :type cl:string
    :initform ""))
)

(cl:defclass ImageCapture-request (<ImageCapture-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImageCapture-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImageCapture-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name realsense_ting_controller-srv:<ImageCapture-request> is deprecated: use realsense_ting_controller-srv:ImageCapture-request instead.")))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <ImageCapture-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader realsense_ting_controller-srv:request-val is deprecated.  Use realsense_ting_controller-srv:request instead.")
  (request m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImageCapture-request>) ostream)
  "Serializes a message object of type '<ImageCapture-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'request))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'request))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImageCapture-request>) istream)
  "Deserializes a message object of type '<ImageCapture-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'request) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'request) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImageCapture-request>)))
  "Returns string type for a service object of type '<ImageCapture-request>"
  "realsense_ting_controller/ImageCaptureRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImageCapture-request)))
  "Returns string type for a service object of type 'ImageCapture-request"
  "realsense_ting_controller/ImageCaptureRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImageCapture-request>)))
  "Returns md5sum for a message object of type '<ImageCapture-request>"
  "33ea4e5aeb30f5913da681ca459d55f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImageCapture-request)))
  "Returns md5sum for a message object of type 'ImageCapture-request"
  "33ea4e5aeb30f5913da681ca459d55f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImageCapture-request>)))
  "Returns full string definition for message of type '<ImageCapture-request>"
  (cl:format cl:nil "string request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImageCapture-request)))
  "Returns full string definition for message of type 'ImageCapture-request"
  (cl:format cl:nil "string request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImageCapture-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'request))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImageCapture-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ImageCapture-request
    (cl:cons ':request (request msg))
))
;//! \htmlinclude ImageCapture-response.msg.html

(cl:defclass <ImageCapture-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:string
    :initform ""))
)

(cl:defclass ImageCapture-response (<ImageCapture-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImageCapture-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImageCapture-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name realsense_ting_controller-srv:<ImageCapture-response> is deprecated: use realsense_ting_controller-srv:ImageCapture-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <ImageCapture-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader realsense_ting_controller-srv:response-val is deprecated.  Use realsense_ting_controller-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImageCapture-response>) ostream)
  "Serializes a message object of type '<ImageCapture-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'response))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'response))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImageCapture-response>) istream)
  "Deserializes a message object of type '<ImageCapture-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'response) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'response) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImageCapture-response>)))
  "Returns string type for a service object of type '<ImageCapture-response>"
  "realsense_ting_controller/ImageCaptureResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImageCapture-response)))
  "Returns string type for a service object of type 'ImageCapture-response"
  "realsense_ting_controller/ImageCaptureResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImageCapture-response>)))
  "Returns md5sum for a message object of type '<ImageCapture-response>"
  "33ea4e5aeb30f5913da681ca459d55f3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImageCapture-response)))
  "Returns md5sum for a message object of type 'ImageCapture-response"
  "33ea4e5aeb30f5913da681ca459d55f3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImageCapture-response>)))
  "Returns full string definition for message of type '<ImageCapture-response>"
  (cl:format cl:nil "string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImageCapture-response)))
  "Returns full string definition for message of type 'ImageCapture-response"
  (cl:format cl:nil "string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImageCapture-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'response))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImageCapture-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ImageCapture-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ImageCapture)))
  'ImageCapture-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ImageCapture)))
  'ImageCapture-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImageCapture)))
  "Returns string type for a service object of type '<ImageCapture>"
  "realsense_ting_controller/ImageCapture")