def getInfoDatabase(file_database_location,name_celebrity):
  with open(file_database_location) as file:
    info_celebrity = {}
    keys_info_celebrity = file.readline().strip().split(",")

    for line in file:
      values_info_celebrity = line.strip().split(",")
      if name_celebrity in values_info_celebrity:
        for i in range(len(keys_info_celebrity)):
          info_celebrity[keys_info_celebrity[i]] = values_info_celebrity[i]

    return info_celebrity
