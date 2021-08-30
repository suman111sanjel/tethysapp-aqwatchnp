# from t
from tethysapp.aqwatchnp.app import Aqwatchnp

TethysAppName = Aqwatchnp.package

AllRegion={0:'HKH',
           1:'AFGHANISTAN',
           4:'BANGLADESH',
           7:'BHUTAN',
           8:'CHINA',
           3:'INDIA',
           6:'MYANMAR',
           5:'NEPAL',
           2:'PAKISTAN'}

initilizationData = {
    'country': 'Nepal',
    'navLogoImage': '/static/' + TethysAppName + '/images/nologo.png',
    'defaultView': '''
    {
        center: ol.proj.transform([84, 28.5], 'EPSG:4326', 'EPSG:3857'),
        zoom: 7,
        extent: [6702855.884774126, 1769255.1930753174, 12194542.852403797, 4812621.833531793]
    }
    ''',
    'DefaultPlotInfo':'''
    {
        colorScheme: 'jet',
        BBOX: [79, 26, 89, 31],
        tickSpan: 2,
        Resolution: 600,
        width: 12,
        height: 9
    }
    ''',
    'TethysAppName': TethysAppName,
    'AdminLevel': 'l2Jumla',
    'regionOrCountryId': 5,
    'TethysAPIAppName':'aqwatchapi',
    'MaskWMS':'false',
    'ForceMaxZoomOut': 'false'
}
