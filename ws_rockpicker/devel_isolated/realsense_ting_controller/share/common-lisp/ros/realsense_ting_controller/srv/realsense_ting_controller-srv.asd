
(cl:in-package :asdf)

(defsystem "realsense_ting_controller-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ImageCapture" :depends-on ("_package_ImageCapture"))
    (:file "_package_ImageCapture" :depends-on ("_package"))
    (:file "ImgProc" :depends-on ("_package_ImgProc"))
    (:file "_package_ImgProc" :depends-on ("_package"))
  ))