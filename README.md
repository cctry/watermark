# Watermark

#### Description

This program is designed to add water marks to pictures and use RSA encryption-decryption pair to exam or extract  

#### Dependency

- Python v2.7.12
- Numpy v1.11.2
- Opencv v3.0.0

#### Usage

To insert a watermark, what are needed are a public key for RSA encryption, a picture waiting for being marked, a bi-level image used as watermark



- To insert a watermark: python watermark.py insert \<origin image fliename\> \<mark image filename\> [\<publicKey\>]

> e.x. python watermark.py insert image.png mark.png [public.pem]

​	It will save the marked image at the current directory. 
   If you want to generate keys, please leave it blank. 

- To extract a watermark: python watermark.py extract \<fliename\> \<privateKey\> [-s \<path\>]

​	-s: save the extracted image to the current directory

​	-s <path>: save the extracted image to the path	

   > e.x. python watermark.py extract image.png private.pem

​	It will display the extracted watermark.
   
   > e.x. python watermark.py extract image.png private.pem -s %PATH

   It will save the extracted watermark to the 'PATH'
