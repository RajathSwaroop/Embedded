# Embedded
My Embedded work
* AWS_IOT - includes python program to upload sensor data to the aws cloud using certificate and private key specific to account
* Program to communicate to the LoRa (Low power Radio) module from raspberry Pi.

Source of original code.
*https://github.com/aws/aws-iot-device-sdk-python (Amazon AWS IOT Python SDK)

Code execution
install the SDK first:

git clone https://github.com/aws/aws-iot-device-sdk-python.git
cd aws-iot-device-sdk-python
python setup.py install

executing the program:
* python AWS_IOT_sensordata.py topic_name

topic_name can be anything that is same as the one supplied at receiver side on AWS IOT cloud


