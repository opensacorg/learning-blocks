from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import Field

class RoleEnum(str, Enum):
    administrator = "administrator"
    aide = "aide"
    guardian = "guardian"
    parent = "parent"
    proctor = "proctor"
    relative = "relative"
    student = "student"
    teacher = "teacher"
    vendor = "vendor"

class LocationEnum(str, Enum):
    school = "school"
    district = "district"
    state = "state"

class CCIEnum(str, Enum):
    college = "college"
    career = "career"
    college_career = "college_career"

class HigherGroupEnum(str, Enum):
    SED = "Socioeconomically Disadvantaged"
    NoSED = "Not Socioeconomically Disadvantaged"
    EL = "English Learner"
    SWD = "Students with Disabilities"
    FosterYouth = "Foster Youth"
    Homeless = "Homeless"
    Migrant = "Migrant"



class SubgroupEnum(str, Enum):
    AfricanAmerican = "African American/Black"
    AmericanIndian = "American Indian or Alaska Native"
    Asian = "Asian"
    Filipino = "Filipino"
    HispanicLatino = "Hispanic or Latino"
    NativeHawaiian = "Native Hawaiian or Pacific Islander"
    TwoOrMoreRaces = "Two or More Races"
    White = "White"

class GenderSubgroupEnum(str, Enum):
    Male = "Male"
    Female = "Female"
    NonBinary = "Non-Binary"

# Economic Status Subgroups
class EconomicStatusEnum(str, Enum):
    FRPM_Eligible = "Free/Reduced-Price Meal Eligible"
    FRPM_NotEligible = "Not Eligible for FRPM"


class ColorEnum(str, Enum):
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    NA = "NA"     

class TrueFalseEnum(str, Enum):
    true = "true"
    false = "false"

class LevelEnum(str, Enum):
    very_low = "very_low"
    low = "low"
    meduim = "medium"
    high = "high"
    very_high = "very_high"
    no_performance_level = "no_performance_level"   

class InterventionTiersEnum(int, Enum):
    tier1 = 1
    tier2 = 2
    tier3 = 3
