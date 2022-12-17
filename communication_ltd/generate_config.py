# import configparser
#
# # CREATE OBJECT
# config_file = configparser.ConfigParser()
#
#
# # ADD NEW SECTIONS AND SETTINGS
# config_file["Password Management"] = {
#         "Password Length": "10",
#         "Password Complexity": "upperCase,lowerCase,numbers,specialCharacters (Options: uppercase,lowercase,numbers,specialcharacters)",
# #        "Allow Upper-case Letters in Password (y/n)": "y",
# #        "Allow Lower-case Letters in Password (y/n)": "y",
# #        "Allow numbers in Password (y/n)": "y",
# #        "Allow Special Characters in Password (y/n)": "y",
#         "Password History": "3",
#         "Password Black List": "[123456789]",
#         "Max Try to Login": "3"
#         }
#
# # SAVE CONFIG FILE
# with open(r"configurations.ini", 'w') as configfileObj:
#     config_file.write(configfileObj)
#     configfileObj.flush()
#     configfileObj.close()
#
# print("Config file 'configurations.ini' created")
#
# # PRINT FILE CONTENT
# read_file = open("configurations.ini", "r")
# content = read_file.read()
# print("Content of the config file are:\n")
# print(content)
# read_file.flush()
# read_file.close()