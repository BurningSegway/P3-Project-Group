
(cl:in-package :asdf)

(defsystem "wsg_gripper-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "GripperCommand" :depends-on ("_package_GripperCommand"))
    (:file "_package_GripperCommand" :depends-on ("_package"))
  ))