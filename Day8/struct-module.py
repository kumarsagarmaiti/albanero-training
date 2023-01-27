# The module struct is used to convert the native data types of Python into string of bytes and vice versa. 
# struct module enables conversion between Python objects and C struct represented as bytes object. The C struct representation can be converted back to Python object. The Python struct module is used to provide a simple Pythonic interface to access and manipulate C’s structure datatype. This can be a handy tool if you ever need to deal with C code and don’t have the time to write tools in C since it is a low-level language.
# It is mainly used to store data to disk or transferred over network. Bytes are machine readable, so they can directly be stored into disk. The struct in Python is used for file handling in the case of binary-stored data.
# It supports object that support buffer protocol and provide either read-only or read-wrtiable buffer.
# bytes and bytearray are built in objects which implements buffer protocol. 

# Format
# Format of struct is specified as string which is used for packing and unpacking of data. 
# Format string contains format characters which specifies type to be packed or unpacked.

# Here, format refers to the format of the packing. This is needed since we need to specify the datatype of the byte-string, as it is used with C code. The below table lists the most common values for format. We need one format per value to specify it’s datatype.

# Format	C Datatype	Python type
#   c	        char	a string of length 1
#   ?	        _Bool	bool
#   h	        short	integer
#   l	        long	integer
#   i	        int	    integer
#   f	        float	float
#   d	        double	float
#   s	        char[]	string

# struct.pack()
# The method struct.pack() is used to convert the data types into bytes. It takes multiple arguments based on the first string.

# We have to pass the first string with format characters as mention in the above table. We can pass any arguments as we want. Let's see some examples.

# struct.pack('14s i', b'Tutorialspoint', 2020)
# struct.pack('i i f 3s', 1, 2, 3.5, b'abc')

# struct.unpack()¶
# We have another method struct.unpack() that converts bytes to native Python data types. It takes two arguments, the first one is similar to the pack() method and the second one is the result of struct.pack() method.

# struct.calcsize()
# Syntax:
# struct.calcsize(fmt)
# fmt: format 
# Return the size of the struct (and hence of the string) corresponding to the given format. calcsize() is important function, and is required for function such as struct.pack_into() and struct.unpack_from(), which require offset value and buffer as well. The offset value can be given by the struct.calcsize() function. 

# struct.pack_into()
# Syntax:
# struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# fmt: data type format
# buffer: writable buffer which starts at offset (optional)
# v1,v2.. : values 

# struct.unpack_from()
# Syntax:
# struct.unpack_from(fmt, buffer[,offset = 0])fmt: data type format
# buffer: writable buffer which starts at offset (optional)

# struct.pack_into()
# This function is used pack values into a Python string buffer, available in the ctypes module.

# Format: struct.pack_into(fmt, buffer, offset, v1, v2, …)

# Here, fmt refers to the format specifier, as always. buffer is the string buffer which will now contain the packed values, specified. You can also specify an offset location from the base address from which packing will occur.

# This does not return any value, and simply stores the values into the buffer string.

# import struct 
# import ctypes 
 
# # We will create a string buffer having a size
# # equal to that of a struct with 'iic' values.
# buf_size = struct.calcsize('iic') 
 
# # Create the string buffer
# buff = ctypes.create_string_buffer(buf_size) 
   
# # struct.pack() returns the packed data 
# struct.pack_into('iic', buff, 0, 1, 2, b'A')
 
# print(buff)
 
# # Display the contents of the buffer
# print(buff[:])
# Output

# <ctypes.c_char_Array_9 object at 0x7f4bccef1040>
# b'\x01\x00\x00\x00\x02\x00\x00\x00A'
# Indeed, we get our packed values in the buffer string.

# struct.unpack_from()
# Similar to unpack(), a counterpart exists for unpacking values from a buffer string. This does the reverse of struct.pack_into().

# Format: struct.unpack_from(fmt, buffer, offset)

# This will return a tuple of values, similar to struct.unpack().

# import struct 
# import ctypes 
 
# # We will create a string buffer having a size
# # equal to that of a struct with 'iic' values.
# buf_size = struct.calcsize('iic') 
 
# # Create the string buffer
# buff = ctypes.create_string_buffer(buf_size) 
   
# # struct.pack() returns the packed data 
# struct.pack_into('iic', buff, 0, 1, 2, b'A')
 
# print(struct.unpack_from('iic', buff, 0))
# Output

# (1, 2, b'A')