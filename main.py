import requests
import os
import sys

def get_latest_version():
    response = requests.get('https://example.com/latest-version')
    return response.text

def check_version(current_version):
    latest_version = get_latest_version()
    if current_version != latest_version:
        return True
    return False

def force_update():
    os.system('python -m pip install --upgrade --force-reinstall .')

def main():
    current_version = '1.0.0'  # Bu versiyani o'zingizga o'zgartiring
    if check_version(current_version):
        print('Yangi versiya mavjud. Yangilash boshlanmoqda...')
        force_update()
        sys.exit(0)
    print('Sizda eng so'nggi versiya bor.')

if __name__ == '__main__':
    main()
```

```python
# get_latest_version() funksiyasi yangi versiyani olib keladi
# check_version() funksiyasi hozirgi versiyani yangi versiyaga solishtiradi
# force_update() funksiyasi yangilashni boshlaydi
# main() funksiyasi bosh qismdir
