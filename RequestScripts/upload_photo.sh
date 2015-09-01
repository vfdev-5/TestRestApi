#!/bin/bash

# Upload a photo 

curl -S localhost:8000/api/photo/ -F "image=@/home/vfdev/Downloads/wastes.jpg;filename=uploaded_file_123.jpg;type=image/*" -H 'Authorization: Token 20bc9187c436e47ce7d2caa7f896a40dd91782ee' > log.html

echo


