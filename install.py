from setup import ExtensionInstaller

def loader():
    return BigboyInstaller()

class BigboyInstaller(ExtensionInstaller):
    def __init__(self):
        super(BigboyInstaller, self).__init__(
            version="0.1",
            name='bigboy',
            description='a very big boy',
            author="Jeff Sisson",
            author_email="jeff@bigboy.us",
            config={
                'StdReport': {
                    'bigboy': {
                        'skin':'bigboy',
                        'HTML_ROOT':'bigboy'}}},
            files=[('skins/bigboy',
                    ['skins/bigboy/index.html.tmpl',
                    'skins/bigboy/style.css',
                    'skins/bigboy/script.js',
                    'skins/bigboy/insconsolata.woff',
                    'skins/bigboy/insconsolata-bold.woff',
                    'skins/bigboy/Inconsolata-Regular.ttf',
                     'skins/bigboy/skin.conf'])
                   ]
            )
