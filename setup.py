from setuptools import setup

setup(
    name="electrum-nxs-server",
    version="0.9",
    scripts=['run_electrum_nxs_server','electrum-nxs-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumnxsserver':'src'
        },
    py_modules=[
        'electrumnxsserver.__init__',
        'electrumnxsserver.utils',
        'electrumnxsserver.storage',
        'electrumnxsserver.deserialize',
        'electrumnxsserver.networks',
        'electrumnxsserver.blockchain_processor',
        'electrumnxsserver.server_processor',
        'electrumnxsserver.processor',
        'electrumnxsserver.version',
        'electrumnxsserver.ircthread',
        'electrumnxsserver.stratum_tcp',
        'electrumnxsserver.stratum_http'
    ],
    description="Namecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/spesmilo/electrum-server/",
    long_description="""Server for the Electrum-NXS Lightweight Namecoin Wallet"""
)


