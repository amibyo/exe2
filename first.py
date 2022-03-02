# Import os module
import os
# Import sys module
message = "hello_Mr_Ghoulem"
file = open("build.env", "w")
file.write("message = " + message)
