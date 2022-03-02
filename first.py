# Import os module
import os
# Import sys module
message = "hello Mr Ghoulem"
file = open("build.env", "w")
file.write("message = " + message)
