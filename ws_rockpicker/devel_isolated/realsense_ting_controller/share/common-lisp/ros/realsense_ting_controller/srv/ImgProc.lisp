; Auto-generated. Do not edit!


(cl:in-package realsense_ting_controller-srv)


;//! \htmlinclude ImgProc-request.msg.html

(cl:defclass <ImgProc-request> (roslisp-msg-protocol:ros-message)
  ((request
    :reader request
    :initarg :request
    :type cl:string
    :initform ""))
)

(cl:defclass ImgProc-request (<ImgProc-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImgProc-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImgProc-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name realsense_ting_controller-srv:<ImgProc-request> is deprecated: use realsense_ting_controller-srv:ImgProc-request instead.")))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <ImgProc-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader realsense_ting_controller-srv:request-val is deprecated.  Use realsense_ting_controller-srv:request instead.")
  (request m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImgProc-request>) ostream)
  "Serializes a message object of type '<ImgProc-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'request))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'request))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImgProc-request>) istream)
  "Deserializes a message object of type '<ImgProc-request>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImgProc-request>)))
  "Returns string type for a service object of type '<ImgProc-request>"
  "realsense_ting_controller/ImgProcRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImgProc-request)))
  "Returns string type for a service object of type 'ImgProc-request"
  "realsense_ting_controller/ImgProcRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImgProc-request>)))
  "Returns md5sum for a message object of type '<ImgProc-request>"
  "27a3ac67f0bd767a8424b890cbe335fe")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImgProc-request)))
  "Returns md5sum for a message object of type 'ImgProc-request"
  "27a3ac67f0bd767a8424b890cbe335fe")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImgProc-request>)))
  "Returns full string definition for message of type '<ImgProc-request>"
  (cl:format cl:nil "string request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImgProc-request)))
  "Returns full string definition for message of type 'ImgProc-request"
  (cl:format cl:nil "string request~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImgProc-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'request))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImgProc-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ImgProc-request
    (cl:cons ':request (request msg))
))
;//! \htmlinclude ImgProc-response.msg.html

(cl:defclass <ImgProc-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass ImgProc-response (<ImgProc-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImgProc-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImgProc-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name realsense_ting_controller-srv:<ImgProc-response> is deprecated: use realsense_ting_controller-srv:ImgProc-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <ImgProc-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader realsense_ting_controller-srv:response-val is deprecated.  Use realsense_ting_controller-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImgProc-response>) ostream)
  "Serializes a message object of type '<ImgProc-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'response))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'response))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImgProc-response>) istream)
  "Deserializes a message object of type '<ImgProc-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'response) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'response)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImgProc-response>)))
  "Returns string type for a service object of type '<ImgProc-response>"
  "realsense_ting_controller/ImgProcResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImgProc-response)))
  "Returns string type for a service object of type 'ImgProc-response"
  "realsense_ting_controller/ImgProcResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImgProc-response>)))
  "Returns md5sum for a message object of type '<ImgProc-response>"
  "27a3ac67f0bd767a8424b890cbe335fe")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImgProc-response)))
  "Returns md5sum for a message object of type 'ImgProc-response"
  "27a3ac67f0bd767a8424b890cbe335fe")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImgProc-response>)))
  "Returns full string definition for message of type '<ImgProc-response>"
  (cl:format cl:nil "float32[] response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImgProc-response)))
  "Returns full string definition for message of type 'ImgProc-response"
  (cl:format cl:nil "float32[] response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImgProc-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'response) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImgProc-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ImgProc-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ImgProc)))
  'ImgProc-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ImgProc)))
  'ImgProc-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImgProc)))
  "Returns string type for a service object of type '<ImgProc>"
  "realsense_ting_controller/ImgProc")