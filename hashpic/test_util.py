from .util import *
from .config import *


def test_convert_term_to_rgb():
    assert convert_term_to_rgb(0) == RGB(0, 0, 0)
    assert convert_term_to_rgb(1) == RGB(128, 0, 0)
    assert convert_term_to_rgb(2) == RGB(0, 128, 0)
    assert convert_term_to_rgb(3) == RGB(128, 128, 0)
    assert convert_term_to_rgb(4) == RGB(0, 0, 128)
    assert convert_term_to_rgb(5) == RGB(128, 0, 128)
    assert convert_term_to_rgb(6) == RGB(0, 128, 128)
    assert convert_term_to_rgb(7) == RGB(192, 192, 192)
    assert convert_term_to_rgb(8) == RGB(128, 128, 128)
    assert convert_term_to_rgb(9) == RGB(255, 0, 0)
    assert convert_term_to_rgb(10) == RGB(0, 255, 0)
    assert convert_term_to_rgb(11) == RGB(255, 255, 0)
    assert convert_term_to_rgb(12) == RGB(0, 0, 255)
    assert convert_term_to_rgb(13) == RGB(255, 0, 255)
    assert convert_term_to_rgb(14) == RGB(0, 255, 255)
    assert convert_term_to_rgb(15) == RGB(255, 255, 255)
    assert convert_term_to_rgb(16) == RGB(0, 0, 0)
    assert convert_term_to_rgb(17) == RGB(0, 0, 95)
    assert convert_term_to_rgb(18) == RGB(0, 0, 135)
    assert convert_term_to_rgb(19) == RGB(0, 0, 175)
    assert convert_term_to_rgb(20) == RGB(0, 0, 215)
    assert convert_term_to_rgb(21) == RGB(0, 0, 255)
    assert convert_term_to_rgb(22) == RGB(0, 95, 0)
    assert convert_term_to_rgb(23) == RGB(0, 95, 95)
    assert convert_term_to_rgb(24) == RGB(0, 95, 135)
    assert convert_term_to_rgb(25) == RGB(0, 95, 175)
    assert convert_term_to_rgb(26) == RGB(0, 95, 215)
    assert convert_term_to_rgb(27) == RGB(0, 95, 255)
    assert convert_term_to_rgb(28) == RGB(0, 135, 0)
    assert convert_term_to_rgb(29) == RGB(0, 135, 95)
    assert convert_term_to_rgb(30) == RGB(0, 135, 135)
    assert convert_term_to_rgb(31) == RGB(0, 135, 175)
    assert convert_term_to_rgb(32) == RGB(0, 135, 215)
    assert convert_term_to_rgb(33) == RGB(0, 135, 255)
    assert convert_term_to_rgb(34) == RGB(0, 175, 0)
    assert convert_term_to_rgb(35) == RGB(0, 175, 95)
    assert convert_term_to_rgb(36) == RGB(0, 175, 135)
    assert convert_term_to_rgb(37) == RGB(0, 175, 175)
    assert convert_term_to_rgb(38) == RGB(0, 175, 215)
    assert convert_term_to_rgb(39) == RGB(0, 175, 255)
    assert convert_term_to_rgb(40) == RGB(0, 215, 0)
    assert convert_term_to_rgb(41) == RGB(0, 215, 95)
    assert convert_term_to_rgb(42) == RGB(0, 215, 135)
    assert convert_term_to_rgb(43) == RGB(0, 215, 175)
    assert convert_term_to_rgb(44) == RGB(0, 215, 215)
    assert convert_term_to_rgb(45) == RGB(0, 215, 255)
    assert convert_term_to_rgb(46) == RGB(0, 255, 0)
    assert convert_term_to_rgb(47) == RGB(0, 255, 95)
    assert convert_term_to_rgb(48) == RGB(0, 255, 135)
    assert convert_term_to_rgb(49) == RGB(0, 255, 175)
    assert convert_term_to_rgb(50) == RGB(0, 255, 215)
    assert convert_term_to_rgb(51) == RGB(0, 255, 255)
    assert convert_term_to_rgb(52) == RGB(95, 0, 0)
    assert convert_term_to_rgb(53) == RGB(95, 0, 95)
    assert convert_term_to_rgb(54) == RGB(95, 0, 135)
    assert convert_term_to_rgb(55) == RGB(95, 0, 175)
    assert convert_term_to_rgb(56) == RGB(95, 0, 215)
    assert convert_term_to_rgb(57) == RGB(95, 0, 255)
    assert convert_term_to_rgb(58) == RGB(95, 95, 0)
    assert convert_term_to_rgb(59) == RGB(95, 95, 95)
    assert convert_term_to_rgb(60) == RGB(95, 95, 135)
    assert convert_term_to_rgb(61) == RGB(95, 95, 175)
    assert convert_term_to_rgb(62) == RGB(95, 95, 215)
    assert convert_term_to_rgb(63) == RGB(95, 95, 255)
    assert convert_term_to_rgb(64) == RGB(95, 135, 0)
    assert convert_term_to_rgb(65) == RGB(95, 135, 95)
    assert convert_term_to_rgb(66) == RGB(95, 135, 135)
    assert convert_term_to_rgb(67) == RGB(95, 135, 175)
    assert convert_term_to_rgb(68) == RGB(95, 135, 215)
    assert convert_term_to_rgb(69) == RGB(95, 135, 255)
    assert convert_term_to_rgb(70) == RGB(95, 175, 0)
    assert convert_term_to_rgb(71) == RGB(95, 175, 95)
    assert convert_term_to_rgb(72) == RGB(95, 175, 135)
    assert convert_term_to_rgb(73) == RGB(95, 175, 175)
    assert convert_term_to_rgb(74) == RGB(95, 175, 215)
    assert convert_term_to_rgb(75) == RGB(95, 175, 255)
    assert convert_term_to_rgb(76) == RGB(95, 215, 0)
    assert convert_term_to_rgb(77) == RGB(95, 215, 95)
    assert convert_term_to_rgb(78) == RGB(95, 215, 135)
    assert convert_term_to_rgb(79) == RGB(95, 215, 175)
    assert convert_term_to_rgb(80) == RGB(95, 215, 215)
    assert convert_term_to_rgb(81) == RGB(95, 215, 255)
    assert convert_term_to_rgb(82) == RGB(95, 255, 0)
    assert convert_term_to_rgb(83) == RGB(95, 255, 95)
    assert convert_term_to_rgb(84) == RGB(95, 255, 135)
    assert convert_term_to_rgb(85) == RGB(95, 255, 175)
    assert convert_term_to_rgb(86) == RGB(95, 255, 215)
    assert convert_term_to_rgb(87) == RGB(95, 255, 255)
    assert convert_term_to_rgb(88) == RGB(135, 0, 0)
    assert convert_term_to_rgb(89) == RGB(135, 0, 95)
    assert convert_term_to_rgb(90) == RGB(135, 0, 135)
    assert convert_term_to_rgb(91) == RGB(135, 0, 175)
    assert convert_term_to_rgb(92) == RGB(135, 0, 215)
    assert convert_term_to_rgb(93) == RGB(135, 0, 255)
    assert convert_term_to_rgb(94) == RGB(135, 95, 0)
    assert convert_term_to_rgb(95) == RGB(135, 95, 95)
    assert convert_term_to_rgb(96) == RGB(135, 95, 135)
    assert convert_term_to_rgb(97) == RGB(135, 95, 175)
    assert convert_term_to_rgb(98) == RGB(135, 95, 215)
    assert convert_term_to_rgb(99) == RGB(135, 95, 255)
    assert convert_term_to_rgb(100) == RGB(135, 135, 0)
    assert convert_term_to_rgb(101) == RGB(135, 135, 95)
    assert convert_term_to_rgb(102) == RGB(135, 135, 135)
    assert convert_term_to_rgb(103) == RGB(135, 135, 175)
    assert convert_term_to_rgb(104) == RGB(135, 135, 215)
    assert convert_term_to_rgb(105) == RGB(135, 135, 255)
    assert convert_term_to_rgb(106) == RGB(135, 175, 0)
    assert convert_term_to_rgb(107) == RGB(135, 175, 95)
    assert convert_term_to_rgb(108) == RGB(135, 175, 135)
    assert convert_term_to_rgb(109) == RGB(135, 175, 175)
    assert convert_term_to_rgb(110) == RGB(135, 175, 215)
    assert convert_term_to_rgb(111) == RGB(135, 175, 255)
    assert convert_term_to_rgb(112) == RGB(135, 215, 0)
    assert convert_term_to_rgb(113) == RGB(135, 215, 95)
    assert convert_term_to_rgb(114) == RGB(135, 215, 135)
    assert convert_term_to_rgb(115) == RGB(135, 215, 175)
    assert convert_term_to_rgb(116) == RGB(135, 215, 215)
    assert convert_term_to_rgb(117) == RGB(135, 215, 255)
    assert convert_term_to_rgb(118) == RGB(135, 255, 0)
    assert convert_term_to_rgb(119) == RGB(135, 255, 95)
    assert convert_term_to_rgb(120) == RGB(135, 255, 135)
    assert convert_term_to_rgb(121) == RGB(135, 255, 175)
    assert convert_term_to_rgb(122) == RGB(135, 255, 215)
    assert convert_term_to_rgb(123) == RGB(135, 255, 255)
    assert convert_term_to_rgb(124) == RGB(175, 0, 0)
    assert convert_term_to_rgb(125) == RGB(175, 0, 95)
    assert convert_term_to_rgb(126) == RGB(175, 0, 135)
    assert convert_term_to_rgb(127) == RGB(175, 0, 175)
    assert convert_term_to_rgb(128) == RGB(175, 0, 215)
    assert convert_term_to_rgb(129) == RGB(175, 0, 255)
    assert convert_term_to_rgb(130) == RGB(175, 95, 0)
    assert convert_term_to_rgb(131) == RGB(175, 95, 95)
    assert convert_term_to_rgb(132) == RGB(175, 95, 135)
    assert convert_term_to_rgb(133) == RGB(175, 95, 175)
    assert convert_term_to_rgb(134) == RGB(175, 95, 215)
    assert convert_term_to_rgb(135) == RGB(175, 95, 255)
    assert convert_term_to_rgb(136) == RGB(175, 135, 0)
    assert convert_term_to_rgb(137) == RGB(175, 135, 95)
    assert convert_term_to_rgb(138) == RGB(175, 135, 135)
    assert convert_term_to_rgb(139) == RGB(175, 135, 175)
    assert convert_term_to_rgb(140) == RGB(175, 135, 215)
    assert convert_term_to_rgb(141) == RGB(175, 135, 255)
    assert convert_term_to_rgb(142) == RGB(175, 175, 0)
    assert convert_term_to_rgb(143) == RGB(175, 175, 95)
    assert convert_term_to_rgb(144) == RGB(175, 175, 135)
    assert convert_term_to_rgb(145) == RGB(175, 175, 175)
    assert convert_term_to_rgb(146) == RGB(175, 175, 215)
    assert convert_term_to_rgb(147) == RGB(175, 175, 255)
    assert convert_term_to_rgb(148) == RGB(175, 215, 0)
    assert convert_term_to_rgb(149) == RGB(175, 215, 95)
    assert convert_term_to_rgb(150) == RGB(175, 215, 135)
    assert convert_term_to_rgb(151) == RGB(175, 215, 175)
    assert convert_term_to_rgb(152) == RGB(175, 215, 215)
    assert convert_term_to_rgb(153) == RGB(175, 215, 255)
    assert convert_term_to_rgb(154) == RGB(175, 255, 0)
    assert convert_term_to_rgb(155) == RGB(175, 255, 95)
    assert convert_term_to_rgb(156) == RGB(175, 255, 135)
    assert convert_term_to_rgb(157) == RGB(175, 255, 175)
    assert convert_term_to_rgb(158) == RGB(175, 255, 215)
    assert convert_term_to_rgb(159) == RGB(175, 255, 255)
    assert convert_term_to_rgb(160) == RGB(215, 0, 0)
    assert convert_term_to_rgb(161) == RGB(215, 0, 95)
    assert convert_term_to_rgb(162) == RGB(215, 0, 135)
    assert convert_term_to_rgb(163) == RGB(215, 0, 175)
    assert convert_term_to_rgb(164) == RGB(215, 0, 215)
    assert convert_term_to_rgb(165) == RGB(215, 0, 255)
    assert convert_term_to_rgb(166) == RGB(215, 95, 0)
    assert convert_term_to_rgb(167) == RGB(215, 95, 95)
    assert convert_term_to_rgb(168) == RGB(215, 95, 135)
    assert convert_term_to_rgb(169) == RGB(215, 95, 175)
    assert convert_term_to_rgb(170) == RGB(215, 95, 215)
    assert convert_term_to_rgb(171) == RGB(215, 95, 255)
    assert convert_term_to_rgb(172) == RGB(215, 135, 0)
    assert convert_term_to_rgb(173) == RGB(215, 135, 95)
    assert convert_term_to_rgb(174) == RGB(215, 135, 135)
    assert convert_term_to_rgb(175) == RGB(215, 135, 175)
    assert convert_term_to_rgb(176) == RGB(215, 135, 215)
    assert convert_term_to_rgb(177) == RGB(215, 135, 255)
    assert convert_term_to_rgb(178) == RGB(215, 175, 0)
    assert convert_term_to_rgb(179) == RGB(215, 175, 95)
    assert convert_term_to_rgb(180) == RGB(215, 175, 135)
    assert convert_term_to_rgb(181) == RGB(215, 175, 175)
    assert convert_term_to_rgb(182) == RGB(215, 175, 215)
    assert convert_term_to_rgb(183) == RGB(215, 175, 255)
    assert convert_term_to_rgb(184) == RGB(215, 215, 0)
    assert convert_term_to_rgb(185) == RGB(215, 215, 95)
    assert convert_term_to_rgb(186) == RGB(215, 215, 135)
    assert convert_term_to_rgb(187) == RGB(215, 215, 175)
    assert convert_term_to_rgb(188) == RGB(215, 215, 215)
    assert convert_term_to_rgb(189) == RGB(215, 215, 255)
    assert convert_term_to_rgb(190) == RGB(215, 255, 0)
    assert convert_term_to_rgb(191) == RGB(215, 255, 95)
    assert convert_term_to_rgb(192) == RGB(215, 255, 135)
    assert convert_term_to_rgb(193) == RGB(215, 255, 175)
    assert convert_term_to_rgb(194) == RGB(215, 255, 215)
    assert convert_term_to_rgb(195) == RGB(215, 255, 255)
    assert convert_term_to_rgb(196) == RGB(255, 0, 0)
    assert convert_term_to_rgb(197) == RGB(255, 0, 95)
    assert convert_term_to_rgb(198) == RGB(255, 0, 135)
    assert convert_term_to_rgb(199) == RGB(255, 0, 175)
    assert convert_term_to_rgb(200) == RGB(255, 0, 215)
    assert convert_term_to_rgb(201) == RGB(255, 0, 255)
    assert convert_term_to_rgb(202) == RGB(255, 95, 0)
    assert convert_term_to_rgb(203) == RGB(255, 95, 95)
    assert convert_term_to_rgb(204) == RGB(255, 95, 135)
    assert convert_term_to_rgb(205) == RGB(255, 95, 175)
    assert convert_term_to_rgb(206) == RGB(255, 95, 215)
    assert convert_term_to_rgb(207) == RGB(255, 95, 255)
    assert convert_term_to_rgb(208) == RGB(255, 135, 0)
    assert convert_term_to_rgb(209) == RGB(255, 135, 95)
    assert convert_term_to_rgb(210) == RGB(255, 135, 135)
    assert convert_term_to_rgb(211) == RGB(255, 135, 175)
    assert convert_term_to_rgb(212) == RGB(255, 135, 215)
    assert convert_term_to_rgb(213) == RGB(255, 135, 255)
    assert convert_term_to_rgb(214) == RGB(255, 175, 0)
    assert convert_term_to_rgb(215) == RGB(255, 175, 95)
    assert convert_term_to_rgb(216) == RGB(255, 175, 135)
    assert convert_term_to_rgb(217) == RGB(255, 175, 175)
    assert convert_term_to_rgb(218) == RGB(255, 175, 215)
    assert convert_term_to_rgb(219) == RGB(255, 175, 255)
    assert convert_term_to_rgb(220) == RGB(255, 215, 0)
    assert convert_term_to_rgb(221) == RGB(255, 215, 95)
    assert convert_term_to_rgb(222) == RGB(255, 215, 135)
    assert convert_term_to_rgb(223) == RGB(255, 215, 175)
    assert convert_term_to_rgb(224) == RGB(255, 215, 215)
    assert convert_term_to_rgb(225) == RGB(255, 215, 255)
    assert convert_term_to_rgb(226) == RGB(255, 255, 0)
    assert convert_term_to_rgb(227) == RGB(255, 255, 95)
    assert convert_term_to_rgb(228) == RGB(255, 255, 135)
    assert convert_term_to_rgb(229) == RGB(255, 255, 175)
    assert convert_term_to_rgb(230) == RGB(255, 255, 215)
    assert convert_term_to_rgb(231) == RGB(255, 255, 255)
    assert convert_term_to_rgb(232) == RGB(8, 8, 8)
    assert convert_term_to_rgb(233) == RGB(18, 18, 18)
    assert convert_term_to_rgb(234) == RGB(28, 28, 28)
    assert convert_term_to_rgb(235) == RGB(38, 38, 38)
    assert convert_term_to_rgb(236) == RGB(48, 48, 48)
    assert convert_term_to_rgb(237) == RGB(58, 58, 58)
    assert convert_term_to_rgb(238) == RGB(68, 68, 68)
    assert convert_term_to_rgb(239) == RGB(78, 78, 78)
    assert convert_term_to_rgb(240) == RGB(88, 88, 88)
    assert convert_term_to_rgb(241) == RGB(98, 98, 98)
    assert convert_term_to_rgb(242) == RGB(108, 108, 108)
    assert convert_term_to_rgb(243) == RGB(118, 118, 118)
    assert convert_term_to_rgb(244) == RGB(128, 128, 128)
    assert convert_term_to_rgb(245) == RGB(138, 138, 138)
    assert convert_term_to_rgb(246) == RGB(148, 148, 148)
    assert convert_term_to_rgb(247) == RGB(158, 158, 158)
    assert convert_term_to_rgb(248) == RGB(168, 168, 168)
    assert convert_term_to_rgb(249) == RGB(178, 178, 178)
    assert convert_term_to_rgb(250) == RGB(188, 188, 188)
    assert convert_term_to_rgb(251) == RGB(198, 198, 198)
    assert convert_term_to_rgb(252) == RGB(208, 208, 208)
    assert convert_term_to_rgb(253) == RGB(218, 218, 218)
    assert convert_term_to_rgb(254) == RGB(228, 228, 228)
    assert convert_term_to_rgb(255) == RGB(238, 238, 238)


def test_chunk_it():
    hash = "ff00ff00"
    chunks = chunk_it(hash)
    expected = ["ff", "00", "ff", "00"]
    assert chunks == expected, "Should be ['ff', '00', 'ff', '00']"


def test_hash_to_color_codes():
    hash = "ff00ff00"
    color_codes = hash_to_color_codes(hash)
    expected = [RGB(238, 238, 238), RGB(0, 0, 0), RGB(238, 238, 238), RGB(0, 0, 0)]
    assert color_codes == expected


def test_paint_svg():
    hash = "5c1f05a8"
    size = 1200
    digest_length = 4
    colors = hash_to_color_codes(hash)
    SVG = paint_svg(size, digest_length, colors)
    expected = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="1200" height="1200" >
  <rect width="600" height="600" fill="#8700d7" x="0" y="0" rx="0"/>
  <rect width="600" height="600" fill="#0087af" x="600" y="0" rx="0"/>
  <rect width="600" height="600" fill="#800080" x="0" y="600" rx="0"/>
  <rect width="600" height="600" fill="#d75f87" x="600" y="600" rx="0"/>
</svg>\n"""
    assert SVG == expected
