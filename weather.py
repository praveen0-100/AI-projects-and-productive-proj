import requests
print("\t\twelcome to the weather forcasting BOT")
print('just enter the city you want see the weather report for and click on the button! it is simple!\n')

city_name=input('enter the city (or) country to know the weather report:')
print('\n\n')

def Gen_report(c):
    url='https://wttr.in/{}'.format(c)
    try:
        data=requests.get(url)
        T=data.text
    except:
        T='Error ocurred'
    print(T)

Gen_report(city_name)
