def write_enum_class(file_name, class_name, dict_info):
    header = """import enum

class {}(enum.Enum):
""".format(class_name)

    with open(file_name, "w") as f:
        f.write(header)
        for key, value in dict_info.items():
            f.write("    {} = '{}',\n".format(key, value))
