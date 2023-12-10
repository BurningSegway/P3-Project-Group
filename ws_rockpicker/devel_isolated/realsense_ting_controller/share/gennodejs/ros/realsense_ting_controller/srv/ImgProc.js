// Auto-generated. Do not edit!

// (in-package realsense_ting_controller.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ImgProcRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.request = null;
    }
    else {
      if (initObj.hasOwnProperty('request')) {
        this.request = initObj.request
      }
      else {
        this.request = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImgProcRequest
    // Serialize message field [request]
    bufferOffset = _serializer.string(obj.request, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImgProcRequest
    let len;
    let data = new ImgProcRequest(null);
    // Deserialize message field [request]
    data.request = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.request);
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'realsense_ting_controller/ImgProcRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9b13f31f7a0a36901919f7ec0d9f40d4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string request
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImgProcRequest(null);
    if (msg.request !== undefined) {
      resolved.request = msg.request;
    }
    else {
      resolved.request = ''
    }

    return resolved;
    }
};

class ImgProcResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.response = null;
    }
    else {
      if (initObj.hasOwnProperty('response')) {
        this.response = initObj.response
      }
      else {
        this.response = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImgProcResponse
    // Serialize message field [response]
    bufferOffset = _arraySerializer.float32(obj.response, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImgProcResponse
    let len;
    let data = new ImgProcResponse(null);
    // Deserialize message field [response]
    data.response = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.response.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'realsense_ting_controller/ImgProcResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7f7d5c92da2c60a9e1822680775d67aa';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] response
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImgProcResponse(null);
    if (msg.response !== undefined) {
      resolved.response = msg.response;
    }
    else {
      resolved.response = []
    }

    return resolved;
    }
};

module.exports = {
  Request: ImgProcRequest,
  Response: ImgProcResponse,
  md5sum() { return '27a3ac67f0bd767a8424b890cbe335fe'; },
  datatype() { return 'realsense_ting_controller/ImgProc'; }
};
