'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import argparse
import serial


# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


# Read in command-line parameters
parser = argparse.ArgumentParser()
#parser.add_argument("-e", "--endpoint", action="store", required=True, dest="host", help="Your AWS IoT custom endpoint")
#parser.add_argument("-r", "--rootCA", action="store", required=True, dest="rootCAPath", help="Root CA file path")
#parser.add_argument("-c", "--cert", action="store", dest="certificatePath", help="Certificate file path")
#parser.add_argument("-k", "--key", action="store", dest="privateKeyPath", help="Private key file path")
parser.add_argument("-w", "--websocket", action="store_true", dest="useWebsocket", default=False,help="Use MQTT over WebSocket")
#parser.add_argument("-id", "--clientId", action="store", dest="clientId", default="basicPubSub",help="Targeted client id")
parser.add_argument("-t", "--topic", action="store", dest="topic", default="sdk/test/Python", help="Targeted topic")

ser = serial.Serial("/dev/ttyS0",9600,timeout=10000)
print(ser)
temp = 1234.23
humid = 1234.23
pressure = 1234.43
args = parser.parse_args()
host = "a152my6096snyb.iot.us-west-2.amazonaws.com" #args.host
rootCAPath = "/home/pi/Desktop/deviceSDK/cert/cert.pem" #args.rootCAPath
certificatePath = "/home/pi/Desktop/deviceSDK/cert/f44225df91-certificate.pem.crt" #args.certificatePath
privateKeyPath = "/home/pi/Desktop/deviceSDK/cert/f44225df91-private.pem.key" #args.privateKeyPath
useWebsocket = args.useWebsocket
clientId = "Pi_1"#args.clientId
topic = args.topic



'''if args.useWebsocket and args.certificatePath and args.privateKeyPath:
    parser.error("X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.")
    exit(2)

if not args.useWebsocket and (not args.certificatePath or not args.privateKeyPath):
    parser.error("Missing credentials for authentication.")
    exit(2)
'''
# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
if useWebsocket:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
    myAWSIoTMQTTClient.configureEndpoint(host, 443)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath)
else:
    myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    myAWSIoTMQTTClient.configureEndpoint(host, 8883)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe(topic, 1, customCallback)
time.sleep(2)AWS

# Publish to the same topic in a loop forever
loopCount = 0
flag1 = 0
flag2 = 0
flag3 = 0
while True:
    data = ser.readline()
    for i in range(len(data)):
	        if data[i] == 'p':
                        temp = float(data[i+2:len(data)])
                        flag1 = 1
			print(temp)
		elif data[i] == 'd':
			humid = float(data[i+2:len(data)])
			flag2 = 1
			print(humid)
		elif data[i] == 'r' and data[i+1]== '=':
			pressure = float(data[i+2:len(data)])
			flag3 = 1
			print(pressure)
		if flag1 == 1  and flag2 == 1 and flag3 == 1:
                        myAWSIoTMQTTClient.publish(topic, "temp:" + str(temp)+":humid:"+str(humid)+":press:"+str(pressure), 1)
    loopCount += 1
    time.sleep(1)