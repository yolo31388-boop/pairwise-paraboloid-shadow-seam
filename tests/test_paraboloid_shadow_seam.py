import pytest
import math
from render import paraboloid_shadow_seam as mod

CASES = [
    ("wrap", 'm.wrap_v(1.2) == approx(0.2)'),
    ("near", 'm.near_plane(0) == approx(1e-4)'),
    ("half", 'm.half_angle(120) == 60'),
    ("offset", 'm.atlas_offset(1) == approx(0.5)'),
    ("depth", 'm.paraboloid_depth(5, 1, 11) == approx(0.5)'),
    ("basis", 'm.basis(0) == approx((1.0, 0.0))'),
    ("seam", 'm.seam_sample(0.98, 0.05) == approx(0.03)'),
    ("texel", 'm.shadow_texel(180, 512) == 256'),
    ("back", 'm.is_backface(-1) is True'),
    ("clear", 'm.clear_key("lamp") == "clear:lamp"'),
    ("dual", 'm.dual_index("back") == 1'),
    ("clamp", 'm.clamp_angle(-10) == 0'),
    ("cone", 'm.cone_area(90) == approx(6.2832, abs=1e-3)'),
    ("uv", 'm.face_uv(1, 0.2, 0.5) == approx((0.6, 0.5))'),
    ("eps", 'm.seam_epsilon(1024) == approx(0.000976, abs=1e-6)')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
