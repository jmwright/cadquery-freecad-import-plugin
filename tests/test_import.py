import tempfile
import os
import cadquery as cq
from cadquery_freecad_import_plugin.plugin import import_freecad_part
import pytest


def test_static_import():
    """
    Test an import of a part without adjusting any parameters.
    """

    # Find the path to the test items
    cur_path = os.path.join(os.getcwd(), "tests", "test_assets", "case-top-3mm.FCStd")

    # Do the import
    result = import_freecad_part(cur_path)

    # Make sure the solid is the correct size
    assert result.val().BoundingBox().xlen == pytest.approx(155.0)
    assert result.val().BoundingBox().ylen == pytest.approx(157.0)
    assert result.val().BoundingBox().zlen == pytest.approx(6.0)

    # Make sure the part has the correct number of faces
    assert result.faces().size() == 67
    assert result.edges().size() == 190


def test_parametric_import():
    """
    Test an import of a part with adjusting the internal rail spacing parameter.
    """

    # Find the path to the test items
    cur_path = os.path.join(os.getcwd(), "tests", "test_assets", "base_shelf.FCStd")

    # Do the import
    result = import_freecad_part(
        cur_path, parameters={"internal_rail_spacing": {"value": 152.4, "units": "mm"}}
    )

    # Make sure the solid is the correct size
    assert result.val().BoundingBox().xlen == pytest.approx(157.4)
    assert result.val().BoundingBox().ylen == pytest.approx(115.0)
    assert result.val().BoundingBox().zlen == pytest.approx(28.0)

    # Make sure the part has the correct number of faces
    assert result.faces().size() == 425
    assert result.edges().size() == 1255
