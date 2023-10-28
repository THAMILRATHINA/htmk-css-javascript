# startup code begin
from param import *
from math import *
Units("feet")
saved_sds2_version = '7.025'
saved_python_version = (2, 3, 0, 'final', 0)
try:
    from shape import Shape
    from point import Point, PointLocate
    from member import Member, MemberLocate
    from mtrl_list import MtrlLocate, HoleLocate
    from cons_line import ConsLine
    from cons_circle import ConsCircle
    from rnd_plate import RndPlate
    from rect_plate import RectPlate
    from bnt_plate import BntPlate
    from rolled_section import RolledSection
    from weld_add import Weld
    from flat_bar import FlatBar
    from hole_add import Hole
    from bolt_add import Bolt
    from roll_plate import RollPl
    from sqr_bar import SqrBar
    from rnd_bar import RndBar
    from shr_stud import ShrStud
    from grate import Grate
    from grate_trd import GrateTrd
    from deck import Deck
    from mtrl_fit import MtrlFit
    from version import CurrentVersion, VersionCompare
    curr_version = CurrentVersion()
except ImportError:
    curr_version = 'None' 
    def VersionCompare( v1, v2 ):
        return -1
if VersionCompare( curr_version, '6.311' ) >= 0:
    from job import Job
    from fab import Fabricator
if VersionCompare( curr_version, '6.311' ) >= 0:
    from plate_layout import PlateLayout
if VersionCompare( curr_version, '6.314' ) >= 0:
    from plate_layout import BntPlateLayout
if VersionCompare( curr_version, '6.4' ) >= 0:
    from mtrl_cut import MtrlCut
if VersionCompare( curr_version, '7.006' ) >= 0:
    from member import MemberAllocated
if VersionCompare( curr_version, '7.009' ) >= 0:
    from job import JobName
    from fab import FabricatorName

try:
    p1 = PointLocate("Locate 1st point")
    p2 = PointLocate("Locate 2nd point")
    # construction line begin
    cl1 = ConsLine()
    cl1.pt1 = p1
    cl1.pt2 = p2
    cl1.pen = "Green"
    cl1.add()
    # construction line end
    def drw_cline(x, z):
        # construction line begin
        cl2 = ConsLine()
        cl2.pt1 = x
        cl2.angle = cl1.angle + 90
        cl2.pen = z
        cl2.add()
        # construction line end

    r = yes_or_no("Which way you need to divide?","by number","by spacing")
    drw_cline(p1,"Cyan")
    drw_cline(p2,"Cyan")
    p0 = (p2-p1)
    d = p1.dist(p2)
    bill = [p1]


    if r == "by number":
        no = Prompt(10, "No. of Equal spaces")
        s = float(d/no)
        for count in xrange(1,no):
            m = (((p0.x)**2)+((p0.y)**2)+((p0.z)**2))**(0.50)
            p3 = Point((p0.x)/m,(p0.y)/m,(p0.z)/m)
            p4 = (p1)+((p3.x)*s,(p3.y)*s,(p3.z)*s)
            bill.insert(count,p4)
            drw_cline(p4,"Green")
            p1 = p4
    else:
        # Dialog begin
        spc = Prompt("1-0", "Enter the spacing")
        # Dialog end
        no1 = int(ceil(d/spc))
        for count in xrange(1,no1):
            m = (((p0.x)**2)+((p0.y)**2)+((p0.z)**2))**(0.50)
            p3 = Point((p0.x)/m,(p0.y)/m,(p0.z)/m)
            p4 = (p1)+((p3.x)*spc,(p3.y)*spc,(p3.z)*spc)
            bill.insert(count,p4)
            drw_cline(p4,"Green")
            p1 = p4
except Exception as e:
    pass