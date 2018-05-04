import glob
import xml.etree.ElementTree as et

app_setting_key = input('Digite a chave do App Settings você quer trocar o valor ex:(ByPassCrypto): ')
app_setting_value = input('Digite o valor da chave ex:(True): ')

def main():
    if app_setting_key == '':
        print('Chave inválida')
        return

    if app_setting_value == '':
        print('Valor inválido')
        return
    
    for filename in glob.iglob('C:/sandbox/**/Web.config', recursive = True):        
        handle_file(filename)

def handle_file(filename):
    root = et.parse(filename)
    configurations = root.find("appSettings")
    if configurations == None:
        return
    
    config_setting = configurations.iterfind("add")
    for config in configurations:
        if config.attrib['key'] == app_setting_key:            
            config.attrib['value'] = app_setting_value
    print(filename + ' Atualizado com Sucesso')
    root.write(filename)

if __name__ == "__main__":
    main()
