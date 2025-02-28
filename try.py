def validate_aadhaar(aadhaar_number):
    verhoeff_table_d = [[0,1,2,3,4,5,6,7,8,9], [1,2,3,4,0,6,7,8,9,5], 
                        [2,3,4,0,1,7,8,9,5,6], [3,4,0,1,2,8,9,5,6,7], 
                        [4,0,1,2,3,9,5,6,7,8], [5,9,8,7,6,0,4,3,2,1], 
                        [6,5,9,8,7,1,0,4,3,2], [7,6,5,9,8,2,1,0,4,3], 
                        [8,7,6,5,9,3,2,1,0,4], [9,8,7,6,5,4,3,2,1,0]]
    verhoeff_table_p = [[0,1,2,3,4,5,6,7,8,9], [1,5,7,6,2,8,3,0,9,4], 
                        [5,8,0,3,7,9,6,1,4,2], [8,9,1,6,0,4,3,5,2,7], 
                        [9,4,5,3,1,2,6,8,7,0], [4,2,8,6,5,7,3,9,0,1], 
                        [2,7,9,3,8,0,6,4,1,5], [7,0,4,6,9,1,3,2,5,8]]
    inv = [0,4,3,2,1,5,6,7,8,9]

    def checksum(number):
        c = 0
        num_list = [int(i) for i in str(number)][::-1]
        for i, num in enumerate(num_list):
            c = verhoeff_table_d[c][verhoeff_table_p[(i % 8)][num]]
        return inv[c]

    return checksum(aadhaar_number) == 0

aadhaar_number = int(input("enter aadhar number:")) # Replace with actual Aadhaar
if validate_aadhaar(aadhaar_number):
    print("Valid Aadhaar Number Format")
else:
    print("Invalid Aadhaar Number")

