import configparser
config = configparser.RawConfigParser()
configFile='BIConfig.ini'
config.read_file(open(configFile))



for each_section in config.sections():
    print(each_section , config.get(each_section,'account'), config.get(each_section,'hostname'))
    if config.get(each_section,'account') == 'cxcxaacco':
        config[each_section]['account']='NewcxcxaaccoJul2018'

with open(configFile, 'w') as configfile:    # save
    config.write(configfile)
