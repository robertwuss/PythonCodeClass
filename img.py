from PIL import Image


for i in range (1000):

    input_filename = 'sunflower{}.jpg'.format(i)
    output_filename = 'sunflower{}.jpg'.format(i + 1)

    img = Image.open(input_filename)
    rimg = img.rotate(90, expand=True)
    rimg.save(output_filename)

    # print ('reading{}, saving to {}
