; Auto-generated. Do not edit!


(cl:in-package wsg_gripper-srv)


;//! \htmlinclude GripperCommand-request.msg.html

(cl:defclass <GripperCommand-request> (roslisp-msg-protocol:ros-message)
  ((command
    :reader command
    :initarg :command
    :type cl:string
    :initform ""))
)

(cl:defclass GripperCommand-request (<GripperCommand-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GripperCommand-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GripperCommand-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wsg_gripper-srv:<GripperCommand-request> is deprecated: use wsg_gripper-srv:GripperCommand-request instead.")))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <GripperCommand-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wsg_gripper-srv:command-val is deprecated.  Use wsg_gripper-srv:command instead.")
  (command m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GripperCommand-request>) ostream)
  "Serializes a message object of type '<GripperCommand-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GripperCommand-request>) istream)
  "Deserializes a message object of type '<GripperCommand-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GripperCommand-request>)))
  "Returns string type for a service object of type '<GripperCommand-request>"
  "wsg_gripper/GripperCommandRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GripperCommand-request)))
  "Returns string type for a service object of type 'GripperCommand-request"
  "wsg_gripper/GripperCommandRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GripperCommand-request>)))
  "Returns md5sum for a message object of type '<GripperCommand-request>"
  "22c7c465d64c7e74c6ae22029c7ca150")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GripperCommand-request)))
  "Returns md5sum for a message object of type 'GripperCommand-request"
  "22c7c465d64c7e74c6ae22029c7ca150")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GripperCommand-request>)))
  "Returns full string definition for message of type '<GripperCommand-request>"
  (cl:format cl:nil "string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GripperCommand-request)))
  "Returns full string definition for message of type 'GripperCommand-request"
  (cl:format cl:nil "string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GripperCommand-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'command))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GripperCommand-request>))
  "Converts a ROS message object to a list"
  (cl:list 'GripperCommand-request
    (cl:cons ':command (command msg))
))
;//! \htmlinclude GripperCommand-response.msg.html

(cl:defclass <GripperCommand-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type cl:string
    :initform ""))
)

(cl:defclass GripperCommand-response (<GripperCommand-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GripperCommand-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GripperCommand-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name wsg_gripper-srv:<GripperCommand-response> is deprecated: use wsg_gripper-srv:GripperCommand-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <GripperCommand-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader wsg_gripper-srv:response-val is deprecated.  Use wsg_gripper-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GripperCommand-response>) ostream)
  "Serializes a message object of type '<GripperCommand-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'response))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'response))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GripperCommand-response>) istream)
  "Deserializes a message object of type '<GripperCommand-response>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GripperCommand-response>)))
  "Returns string type for a service object of type '<GripperCommand-response>"
  "wsg_gripper/GripperCommandResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GripperCommand-response)))
  "Returns string type for a service object of type 'GripperCommand-response"
  "wsg_gripper/GripperCommandResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GripperCommand-response>)))
  "Returns md5sum for a message object of type '<GripperCommand-response>"
  "22c7c465d64c7e74c6ae22029c7ca150")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GripperCommand-response)))
  "Returns md5sum for a message object of type 'GripperCommand-response"
  "22c7c465d64c7e74c6ae22029c7ca150")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GripperCommand-response>)))
  "Returns full string definition for message of type '<GripperCommand-response>"
  (cl:format cl:nil "string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GripperCommand-response)))
  "Returns full string definition for message of type 'GripperCommand-response"
  (cl:format cl:nil "string response~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GripperCommand-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'response))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GripperCommand-response>))
  "Converts a ROS message object to a list"
  (cl:list 'GripperCommand-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'GripperCommand)))
  'GripperCommand-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'GripperCommand)))
  'GripperCommand-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GripperCommand)))
  "Returns string type for a service object of type '<GripperCommand>"
  "wsg_gripper/GripperCommand")