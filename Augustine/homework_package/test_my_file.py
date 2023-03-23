import numpy as np
import pytest
from lvc_hamiltonian import LVC


@pytest.fixture(scope="module")
def lvc_instance():
    return LVC()


def test_VA(lvc_instance):
    expected_va = 98.2578125
    assert np.isclose(lvc_instance.VA, expected_va)



def test_VD(lvc_instance):
    expected_vd = 144.0078125
    assert np.isclose(lvc_instance.VD, expected_vd)


def test_VC(lvc_instance):
    expected_vc = 28.5
    assert np.isclose(lvc_instance.VC, expected_vc)



