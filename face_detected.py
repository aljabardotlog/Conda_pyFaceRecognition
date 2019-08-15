import face_recognition as fr

#https://herophotographyjakarta.files.wordpress.com/2016/12/group1.jpg -> image from
image = fr.load_image_file('./groups/group1.jpg')
face_loc = fr.face_locations(image)

print(f'{len(face_loc)} People')

