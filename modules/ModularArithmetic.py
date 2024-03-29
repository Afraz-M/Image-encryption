import numpy as np
from PIL import Image

def EncryptBinary_MA(input_image, share_size):
    image = np.asarray(input_image).astype(np.uint8)
    (row, column) = image.shape
    shares = np.random.randint(0, 2, size=(row, column, share_size))
    shares[:,:,-1] = image.copy()
    for i in range(share_size-1):
        shares[:,:,-1] = (shares[:,:,-1] + shares[:,:,i])%2


    return shares, image

def DecryptBinary_MA(shares):
    (row, column, share_size) = shares.shape
    shares_image = shares.copy()
    for i in range(share_size-1):
        shares_image[:,:,-1] = (shares_image[:,:,-1] - shares_image[:,:,i] + 2)%2

    final_output = shares_image[:,:,share_size-1]
    output_image = Image.fromarray(final_output.astype(np.uint8) * 255)
    return output_image, final_output

def EncryptColour_MA(input_image, share_size):
    image = np.asarray(input_image)
    print("Image shape", image.shape)
    (row, column, depth) = image.shape
    shares = np.random.randint(0, 256, size=(row, column, depth, share_size))
    shares[:,:,:,-1] = image.copy()
    for i in range(share_size-1):
        shares[:,:,:,-1] = (shares[:,:,:,-1] + shares[:,:,:,i])%256

    return shares, image

def DecryptColour_MA(shares):
    (row, column, depth, share_size) = shares.shape
    shares_image = shares.copy()
    for i in range(share_size-1):
    	shares_image[:,:,:,-1] = (shares_image[:,:,:,-1] - shares_image[:,:,:,i] + 256)%256

    final_output = shares_image[:,:,:,share_size-1]
    output_image = Image.fromarray(final_output.astype(np.uint8))
    return output_image, final_output

def EncryptGrayscale_MA(input_image, share_size):
    image = np.asarray(input_image)
    (row, column) = image.shape
    shares = np.random.randint(0, 256, size=(row, column, share_size))
    shares[:,:,-1] = image.copy()
    for i in range(share_size-1):
        shares[:,:,-1] = (shares[:,:,-1] + shares[:,:,i])%256
    return shares, image

def DecryptGrayscale_MA(shares):
    (row, column, share_size) = shares.shape
    shares_image = shares.copy()
    for i in range(share_size-1):
    	shares_image[:,:,-1] = (shares_image[:,:,-1] - shares_image[:,:,i] + 256)%256

    final_output = shares_image[:,:,share_size-1]
    output_image = Image.fromarray(final_output.astype(np.uint8))
    return output_image, final_output
