import pytz
from datetime import datetime
import requests

# تابعی برای گرفتن زمان یک کشور با استفاده از نام آن
def get_country_time(country):
    # ارسال درخواست به API برای دریافت اطلاعات مربوط به کشور
    url = f"https://restcountries.com/v2/name/{country}?fullText=true"
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve country information from API. {str(e)}"
    
    # بررسی درستی دریافت اطلاعات از API
    if response.status_code != 200:
        return "Error: Could not retrieve country information from API."
    
    # دریافت منطقه زمانی کشور
    time_zone = response.json()[0]['timezones'][0]
    
    # تبدیل منطقه زمانی به شیء pytz
    tz = pytz.timezone(time_zone)
    
    # گرفتن زمان جاری کشور و تبدیل به زمان محلی
    country_time = datetime.now(tz)
    return f"Current time in {country}: {country_time.strftime('%H:%M:%S')}"

if __name__ == '__main__':
    # گرفتن نام کشور از کاربر
    country = input("Enter a country name: ")
    
    # گرفتن زمان کشور و چاپ آن
    print(get_country_time(country))
