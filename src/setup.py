from setuptools import setup
import setup_translate

pkg = 'Extensions.TunerServer'
setup(name='enigma2-plugin-extensions-tunerserver',
       version='3.0',
       description='Builds a virtual channels list',
       package_dir={pkg: 'TunerServer'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'LICENSE', 'maintainer.info']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
