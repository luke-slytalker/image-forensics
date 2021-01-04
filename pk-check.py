import sys


imgfile = sys.argv[1]

with open(imgfile, 'rb') as f:
    # read in the image
    s = f.read()

resp = ''
# PIXEL KNOT byte string
#JPG header variants -- we really only need the 4th one
head1 = s.find(b'\xff\xd8\xff\xdb\x00\x84\x00')
head2 = s.find(b'\xff\xd8\xff\xe0\x00\x10\x4a')
head3 = s.find(b'\xff\xd8\xff\xe1\x00\x18\x45')
head4 = s.find(b'\xff\xd8\xff')

string1 = s.find(b'\x46\x49\x46\x00\x01\x01')

string2a = s.find \
    (b'\x03\x02\x02\x03\x02\x02\x03\x03\x03\x03\x04\x03\x03\x04\x05\x08\x05\x05\x04\x04\x05\x0a\x07\x07\x06\x08\x0c\x0a\x0c\x0c\x0b\x0a\x0b\x0b\x0d\x0e\x12\x10\x0d\x0e\x11\x0e\x0b\x0b\x10\x16\x10\x11\x13\x14\x15\x15\x15\x0c\x0f\x17\x18\x16\x14\x18\x12\x14\x15\x14')
string2b = s.find \
    (b'\x04\x03\x03\x04\x03\x03\x04\x04\x03\x04\x05\x04\x04\x05\x06\x0a\x07\x06\x06\x06\x06\x0d\x09\x0a\x08\x0a\x0f\x0d\x10\x10\x0f\x0d\x0f\x0e\x11\x13\x18\x14\x11\x12\x17\x12\x0e\x0f\x15\x1c\x15\x17\x19\x19\x1b\x1b\x1b\x10\x14\x1d\x1f\x1d\x1a\x1f\x18\x1a\x1b\x1a')
string2c = s.find \
    (b'\x49\x49\x2a\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xec\x00\x11\x44\x75\x63\x6b\x79\x00\x01\x00\x04\x00\x00\x00\x3c\x00\x00\xff\xee\x00\x0e\x41\x64\x6f\x62\x65\x00\x64\xc0\x00\x00\x00\x01\xff\xdb\x00\x84\x00\x06\x04\x04\x04\x05\x04\x06\x05')

string3 = s.find \
    (b'\x05\x04\x05\x09\x05\x05\x09\x14\x0d\x0b\x0d\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14\x14')

# byte string specific to ALL PixelKnot processed images
found = s.find(b'\xFF\xC0\x00\x11\x08')

last10 = s.find(b'\x03\x01\x22\x00\x02\x11\x01\x03\x11\x01')

last5a = s.find(b'\xff\xda\x00\x0c\x03')
last5b = s.find(b'\x8a\x29\x8c\x28\xa2')
last5c = s.find(b'\xfe\xe5\x58\x8e\x3f')
last5d = s.find(b'\x09\xe1\x85\x52\xcd')


if head1 == 0 or head2 == 0 or head3 == 0 or head4 == 0:
    # found the proper header
    print("-- header found")
    if string1 > 1:
        # found next string
        print("-- 2nd string")
        if (string2a != 0) or (string2b != 0) or (string2c != 0):
            # found next string
            print("-- 3rd string")
            if (found > 0):
                # FOUND MAIN PK STRING
                print("-- FOUND MAIN PixelKnot STRING !!!")
                if (last10 > 0):
                    # found the 10 byte string
                    print("-- found 10-byte string")
                    if (last5a > 0) or (last5b > 0) or (last5c > 0) or (last5d > 0):
                        # pretty spot on that its a PixelKnot file
                        print("-- found LAST 5")
                        resp = "PIXELKNOT FOUND!!!!!"
                        #resp = jsonify({'PixelKnot' :'YES'})
                        #resp.status_code = 201
                        #return resp

                    else:
                        resp = "No indicators found."
                        #resp = jsonify({'PixelKnot' :'NO'})
                        #resp.status_code = 201
                else:
                    resp = "No indicators found."
                    #resp = jsonify({'PixelKnot': 'NO'})
                    #resp.status_code = 201
            else:
                resp = "No indicators found."
                #resp = jsonify({'PixelKnot': 'NO'})
                #resp.status_code = 201
        else:
            resp = "No indicators found."
            #resp = jsonify({'PixelKnot': 'NO'})
            #resp.status_code = 201
    else:
        resp = "No indicators found."
        #resp = jsonify({'PixelKnot': 'NO'})
        #resp.status_code = 201
else:
    resp = "Only JPG or JPEG files allowed."
    #resp = jsonify({'error': 'Allowed file types are jpg or jpeg'})
    #resp.status_code = 201
    #return resp

print(resp)
#return resp

