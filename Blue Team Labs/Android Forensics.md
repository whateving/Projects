# We are currently in the process of hiring a new Junior Forensics analyst, and in order to assess their skills prior to finalizing the hiring decision, we provided them with an Android Image to answer a set of specific questions. However, the candidate was unable to answer all of the questions correctly. We need your help answering these questions.


# What is the Device Hotspot password?

## Firstly I pushed the .img file i was gived through the FTKimager and exported the files found in the root directory of the user volume.

<img width="744" height="645" alt="image" src="https://github.com/user-attachments/assets/8c58d561-072c-46c3-b1ed-8f72ab094a21" />

## Then I processed the files through android file viewer app called aleapp and got the hotspot passphrase in the report:

<img width="972" height="685" alt="image" src="https://github.com/user-attachments/assets/b4b9165f-074c-4b3f-8e9a-b073d040ce5f" />


# There is an image taken by the phone camera when was it taken?(Answer Format: YYYY:MM:DD)

## The answer to this question can be found in root>media>DCIM>camera

<img width="972" height="685" alt="image" src="https://github.com/user-attachments/assets/6aa33fa4-a853-4517-ab38-88293f22cbc8" />


# What is the SMS message that was sent to "s3dawy" ?

## We can get this from the report we got from Q1:

<img width="972" height="685" alt="image" src="https://github.com/user-attachments/assets/3c3983a4-7693-47e6-bc17-89cab2bcf488" />


# What is the phone number of the only contact on the device?

## Same thing, can be taken from the report:

<img width="972" height="685" alt="image" src="https://github.com/user-attachments/assets/8bc48050-f58b-4327-ba17-00d03bfc59f7" />


# What was the user’s last web search?

<img width="972" height="685" alt="image" src="https://github.com/user-attachments/assets/5526a352-8956-411d-919d-ad77107bff26" />


# What was the Google account linked to the device?

## Can also be derived from the report as so:

<img width="972" height="685" alt="image" src="https://github.com/user-attachments/assets/ab761cd0-69f4-4a7e-a560-f5a62005323c" />

# What was the pattern used to unlock the phone? (Note: The pattern is represented as numbers corresponding to dot positions.)

## I took this hash from gesture.key, downloaded gesturerainbowtable.db, and compared this hash against the db to find the pattern

<img width="1014" height="677" alt="image" src="https://github.com/user-attachments/assets/0a5722fe-e269-461e-a470-dc5bfeffd401" />

<img width="1406" height="377" alt="image" src="https://github.com/user-attachments/assets/55d0d9d7-bfd7-4dca-99ca-2d57ba18a01d" />

# What are the manufacturer and device model? (Format: Manufacturer-Model)

## The answer to this last question can be found in the system volume, in build.prop file, by search and combining the values of the following 2 variables (Manufacturer: Line 23 states ro.product.manufacturer=InnJoo & Model: Line 20 states ro.product.model=Max3_Pro_LTE):

<img width="972" height="685" alt="image" src="https://github.com/user-attachments/assets/c6cbfc8b-d8b3-400f-af03-c239cb7566b8" />
