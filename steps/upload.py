import requests


def upload(cookies):
    r = requests.request(
        method='POST',
        url='https://xxcapp.xidian.edu.cn/xisuncov/wap/open-report/save',
        data={
            'szgjcs': '',
            'szcs': '',
            'szgj': '',
            'csmjry': '0',
            'tw': '2',
            'sfcxtz': '0',
            'sfjcbh': '0',
            'sfcxzysx': '0',
            'qksm': '',
            'sfyyjc': '0',
            'jcjgqr': '0',
            'remark': '',
            'address': '广东省广州市黄埔区九佛街道凤湖中路广州绿地城',
            'geo_api_info': {
                'type': 'complete',
                'position': {
                    'Q': '23.321510687935',
                    'R': '113.54531738281298',
                    'lng': '113.545317',
                    'lat': '23.321511',
                },
                'location_type': 'html5',
                'accuracy': '153',
                'isConverted': 'true',
                'status': '1',
                'addressComponent': {
                    'citycode': '020',
                    'adcode': '440112',
                    'businessAreas': [],
                    'neighborhoodType': '',
                    'neighborhood': '',
                    'building': '',
                    'buildingType': '',
                    'street': '峻岚街',
                    'streetNumber': '7号',
                    'country': '中国',
                    'province': '广东省',
                    'city': '广州市',
                    'district': '黄埔区',
                    'towncode': '440112019000',
                    'township': '九佛街道',
                },
                'formattedAddress': '广东省广州市黄埔区九佛街道凤湖中路广州绿地城',
                'roads': [],
                'crosses': [],
                'pois': [],
                'info': 'SUCCESS',
            },
            'area': '广东省 广州市 黄埔区',
            'province': '广东省',
            'city': '广州市',
            'sfzx': '1',
            'sfjcwhry': '0',
            'sfjchbry': '0',
            'sfcyglq': '0',
            'gllx': '',
            'glksrq': '',
            'jcbhlx': '',
            'jcbhrq': '',
            'bztcyy': '',
            'sftjhb': '0',
            'sftjwh': '0',
            'sfjcjwry': '0',
            'jcjg': '',
            'date': '20220315',
            'uid': '534679',
            'created': '1647351492',
            'jcqzrq': '',
            'sfjcqz': '',
            'szsqsfybl': '0',
            'sfsqhzjkk': '0',
            'sqhzjkkys': '',
            'sfygtjzzfj': '0',
            'gtjzzfjsj': '',
            'id': '11683636',
            'gwszdd': '',
            'sfyqjzgc': '',
            'jrsfqzys': '',
            'jrsfqzfy': '',
            'ismoved': '0',
        },
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        },
        cookies=cookies)

    if r.status_code != 200:
        raise RuntimeError('填写失败，状态码为：{}'.format(r.status_code))
    body = r.json()
    if body['e'] != 0:
        raise RuntimeError('填写失败，错误信息为：{}'.format(body['m']))
    print('填写成功')
