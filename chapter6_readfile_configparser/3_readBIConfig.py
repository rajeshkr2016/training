import configparser
config = configparser.RawConfigParser()
configFile='BIConfig.ini'
config.read_file(open(configFile))

for each_section in config.sections():
    #print(each_section)
    print(each_section , config.get(each_section,'account'), config.get(each_section,'hostname'), config.get(each_section,'status'))