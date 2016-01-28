# -*-coding: utf-8-*-
from __future__ import division

import numpy as np


class Hockett(object):
    r"""hardening hockett-sherby

        name
            "hockett"

        parameters
            ["a","sig0","c","n"]

        model
            :math:`\sigeq = a - (a-\sigma _0) e^{-c \epseqpl^n}`
    """
    def __init__(self, param):
        assert len(param) == 4
        self.param = param

    def sigeq(self, epseq):
        param = self.param
        sigref = param[0] - (param[0] - param[1]) * np.exp(-param[2] * np.array(epseq) ** param[3])
        return sigref


if __name__ == '__main__':

    h = Hockett([1500., 1400., 7., .65])
    eps = np.linspace(0., 1., 200)
    sig = h.sigeq(eps)
    print sig
