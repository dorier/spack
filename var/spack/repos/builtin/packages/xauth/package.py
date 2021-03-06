# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Xauth(AutotoolsPackage):
    """The xauth program is used to edit and display the authorization
    information used in connecting to the X server."""

    homepage = "http://cgit.freedesktop.org/xorg/app/xauth"
    url      = "https://www.x.org/archive/individual/app/xauth-1.0.9.tar.gz"

    version('1.0.9', 'def3b4588504ee3d8ec7be607826df02')

    depends_on('libx11')
    depends_on('libxau')
    depends_on('libxext')
    depends_on('libxmu')

    depends_on('xproto@7.0.17:')
    depends_on('pkgconfig', type='build')
    depends_on('util-macros', type='build')

    # TODO: add package for cmdtest test dependency
