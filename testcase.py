
import os
import core.crypto

key = core.crypto.new_key()

print('key', key)

# change as appropriate for your system ..
data_folder = os.path.abspath(os.path.join('/', 'temp', 'cryptographybugtestcase'))

input_file_path = os.path.join(data_folder, 'in.txt')
encrypted_file_path = os.path.join(data_folder, 'enc.fer')
output_file_path = os.path.join(data_folder, 'out.txt')

if not os.path.exists(data_folder):
    os.mkdir(data_folder)

c = core.crypto.Crypto(key)

input_data = 'hi there!'

with open(input_file_path, 'w') as f:
    f.write(input_data)

c.encrypt(input_file_path, encrypted_file_path)
c.decrypt(encrypted_file_path, output_file_path)

with open(output_file_path) as f:
    output_data = f.read()

print(output_data)

print('compares OK:', input_data == output_data)
