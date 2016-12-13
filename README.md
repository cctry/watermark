# Watermark

#### Description

This program is designed to add water marks to pictures.  

#### Dependency

- Python v2.7.12
- Numpy v1.11.2
- Opencv v3.0.0

#### Usage

To insert a watermark, what are needed are a private key for RSA encryption, a picture waiting for being marked, a bi-level image used as watermark



- To insert a watermark: python watermark.py insert <origin image fliename> <mark image filename> <privateKey>

​	e.x. python watermark.py insert image.png mark.png 4fe9fw684f5d9

​	It will save the marked image and print your public key. 

- To extract a watermark: python watermark.py extract <fliename> <publicKey> [<option> <path>]

​	-s: save the extracted image to the current directory

​	-s <path>: save the extracted image to the path	

​	e.x. python watermark.py extract image.png fg8s5d64f5d9

​	It will display or save the extracted watermark.