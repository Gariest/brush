

import time
import cv2
import sys
import time
import json
from gevent import getcurrent, wait
from uuid import uuid4
import datetime

class Response(object):
    def __init__(self):
        self.response = None
        self.status = None
        self.headers = []
    #def setSemaphore(self,semaphore):
        #self.semaphore = semaphore
    def setStatus(self, status):
        self.status = status
    def setHeaders(self, headers):
        self.headers = headers
    def setResponse(self, response):
        self.response = response
    def setResponseSync(self, response):
        self.response = response
    def waitForSignal(self):
        self.event.wait()
    def __iter__(self):
        #wait(self.semaphore)
        yield self.response

def app(environ, start_response):
    if(environ['SERVER_PORT']== '84'):

        if( "/photo" in environ['RAW_URI'] and environ['REQUEST_METHOD'] == 'GET' ):
            img = cv2.imread('img.jpg')
            mask = cv2.imread('mask_inverse.png')
            img_og = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
            mask_og = cv2.cvtColor(mask, cv2.COLOR_RGBA2GRAY)
            dst = img_og.copy()
            cv2.xphoto.inpaint(img_og,mask_og, dst,0)
            #dst = cv2.inpaint(img, mask_og, 3, cv2.INPAINT_TELEA)
            dst_og = cv2.cvtColor(dst, cv2.COLOR_LAB2RGB)
            #cv2.imwrite('result.jpg', dst)
            is_success, im_buf_arr = cv2.imencode(".jpg", dst_og)
            bytesReturn = io.BytesIO(im_buf_arr)
            print(bytesReturn.getbuffer().nbytes)
            response = Response()
            responseHeaders = [
                ('Content-Type', 'image/jpeg'),
                ('Content-Length', str(bytesReturn.getbuffer().nbytes))
            ]
            start_response('200', responseHeaders)
            return environ['wsgi.file_wrapper'](bytesReturn)
            
            
    error = Response()
    errorResponse = b"Not Implemented"
    errorResponseHeaders = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(errorResponse)))
    ]
    start_response('501', errorResponseHeaders)
    error.setResponseSync(errorResponse)
    return error
