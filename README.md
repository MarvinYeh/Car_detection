# Car_detection
For InsurHack Hackathon: AI for insurance claiming process

Transfer learning of ssd_mobilenet_v1_coco_11_06_2017 on Stanford Car dataset(196 car models)
Trained on K80 GPU for 3 days, loss slightly >1

Input image are resized and squashed to one channel using resize_image.py, as some of the training picture are so fat.

Tutorials by Sentdex: https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ
