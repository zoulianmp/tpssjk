# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Index, Integer, String, Unicode, VARBINARY
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Component(Base):
    __tablename__ = 'Component'

    CompIntID = Column(Unicode(255), primary_key=True)
    ComponentID = Column(Unicode(255), nullable=False)
    ComponentName = Column(String(255, u'Latin1_General_BIN2'))
    DevIntFK = Column(String(255, u'Latin1_General_BIN2'))


class ComponentHistory(Base):
    __tablename__ = 'ComponentHistory'

    ComponentHistoryId = Column(Unicode(255), primary_key=True)
    CompIntFK = Column(String(255, u'Latin1_General_BIN2'))
    ActionDate = Column(DateTime, nullable=False)
    Action = Column(String(255, u'Latin1_General_BIN2'))
    Version = Column(String(255, u'Latin1_General_BIN2'))
    SerialNumber = Column(String(255, u'Latin1_General_BIN2'))
    Description = Column(String(255, u'Latin1_General_BIN2'))
    ComponentGroup = Column(String(255, u'Latin1_General_BIN2'))


class DevWorkstationRel(Base):
    __tablename__ = 'DevWorkstationRel'

    DevWorkstationRelID = Column(Integer, primary_key=True)
    DevIntFK = Column(Unicode(255), nullable=False)
    WorkstationIntFK = Column(Unicode(255), nullable=False)


class Device(Base):
    __tablename__ = 'Device'

    DevIntID = Column(Unicode(255), primary_key=True, unique=True)
    DeviceID = Column(Unicode(255), nullable=False)
    SerialNumber = Column(Unicode(255), nullable=False)
    DeviceName = Column(String(255, u'Latin1_General_BIN2'))
    SiteIntFK = Column(String(255, u'Latin1_General_BIN2'))


class HotFix(Base):
    __tablename__ = 'HotFix'

    HotFixIntID = Column(Unicode(255), primary_key=True)
    HotFixID = Column(String(255, u'Latin1_General_BIN2'))
    OperatingSystemIntFK = Column(String(255, u'Latin1_General_BIN2'))
    Description = Column(String(255, u'Latin1_General_BIN2'))
    DateApplied = Column(DateTime)


class Inventory(Base):
    __tablename__ = 'Inventory'

    SiteIntID = Column(Unicode(255), primary_key=True)
    SiteName = Column(String(255, u'Latin1_General_BIN2'))
    SiteDescription = Column(String(255, u'Latin1_General_BIN2'))


class LastRead(Base):
    __tablename__ = 'LastRead'

    ObjectKey = Column(Unicode(128), primary_key=True)
    ReadTS = Column(DateTime, nullable=False)


class NetworkAdapter(Base):
    __tablename__ = 'NetworkAdapter'

    NetworkAdapterIntID = Column(Unicode(255), primary_key=True)
    WorkstationIntFK = Column(String(255, u'Latin1_General_BIN2'))
    NicIndex = Column(Integer, nullable=False)
    NicMACAddr = Column(Unicode(255), nullable=False)
    NicIPAddr = Column(String(255, u'Latin1_General_BIN2'))
    NicDescription = Column(String(255, u'Latin1_General_BIN2'))


class OperatingSystem(Base):
    __tablename__ = 'OperatingSystem'

    OperatingSystemIntID = Column(Unicode(255), primary_key=True)
    WorkstationIntFK = Column(String(255, u'Latin1_General_BIN2'))
    OperatingSystemName = Column(String(255, u'Latin1_General_BIN2'))
    DotNETFrameworkVersions = Column(String(255, u'Latin1_General_BIN2'))
    MSIInstallerVersion = Column(String(255, u'Latin1_General_BIN2'))


class Product(Base):
    __tablename__ = 'Product'

    ProdIntID = Column(Unicode(255), primary_key=True)
    ProductID = Column(String(255, u'Latin1_General_BIN2'))
    ProductName = Column(String(255, u'Latin1_General_BIN2'))
    LastUsed = Column(DateTime)
    WorkstationIntFK = Column(Unicode(255), nullable=False)
    PCSN = Column(String(255, u'Latin1_General_BIN2'))


class ProductHistory(Base):
    __tablename__ = 'ProductHistory'

    ProductHistoryID = Column(Unicode(255), primary_key=True)
    ProdIntFK = Column(String(255, u'Latin1_General_BIN2'))
    ActionDate = Column(DateTime, nullable=False)
    Action = Column(Unicode(255), nullable=False)
    Build = Column(String(255, u'Latin1_General_BIN2'))
    ServicePack = Column(String(255, u'Latin1_General_BIN2'))
    SetupVersion = Column(String(255, u'Latin1_General_BIN2'))
    ExternalVersion = Column(String(255, u'Latin1_General_BIN2'))
    InstallerPerson = Column(String(255, u'Latin1_General_BIN2'))
    Description = Column(String(255, u'Latin1_General_BIN2'))
    ApplicationFamily = Column(String(255, u'Latin1_General_BIN2'))
    nls = Column(String(255, u'Latin1_General_BIN2'))


class SchemaDatum(Base):
    __tablename__ = 'SchemaData'

    Version = Column(BigInteger, primary_key=True)


class SecurityTokenCache(Base):
    __tablename__ = 'SecurityTokenCache'

    ID = Column(BigInteger, nullable=False)
    UserID = Column(Unicode(100), nullable=False)
    UserHashID = Column(Unicode(50), primary_key=True)
    UserName = Column(Unicode(100), nullable=False)
    UserCUID = Column(Unicode(100), nullable=False)
    UserGroupID = Column(Unicode(100), nullable=False)
    LanguageID = Column(Unicode(100), nullable=False)
    SecToken = Column(Unicode, nullable=False)
    DateTime = Column(DateTime, nullable=False)


class Setting(Base):
    __tablename__ = 'Settings'

    SettingsID = Column(Integer, primary_key=True)
    ObjectKey = Column(Unicode(128), nullable=False)
    GroupKey = Column(Unicode(64), nullable=False)
    AttributeKey = Column(Unicode(128), nullable=False)
    Type = Column(Unicode(64), nullable=False)
    Value = Column(Unicode, nullable=False)


class Workstation(Base):
    __tablename__ = 'Workstation'

    WorkstationIntID = Column(Unicode(255), primary_key=True, unique=True)
    Hostname = Column(String(255, u'Latin1_General_BIN2'))
    WorkstationID = Column(String(255, u'Latin1_General_BIN2'), unique=True)
    TotalPhysicalMemory = Column(String(255, u'Latin1_General_BIN2'))
    HardwareDescription = Column(String(255, u'Latin1_General_BIN2'))
    LastReplication = Column(DateTime)
    SiteIntFK = Column(Unicode(255), nullable=False)
    CPUModel = Column(String(255, u'Latin1_General_BIN2'))
    CPUFrequency = Column(String(255, u'Latin1_General_BIN2'))
    VideoCardModel = Column(String(255, u'Latin1_General_BIN2'))
    VideoCardDriver = Column(String(255, u'Latin1_General_BIN2'))
    DellTag = Column(String(255, u'Latin1_General_BIN2'))


class Sysdiagram(Base):
    __tablename__ = 'sysdiagrams'
    __table_args__ = (
        Index('UK_principal_name', 'principal_id', 'name', unique=True),
    )

    name = Column(Unicode(128), nullable=False)
    principal_id = Column(Integer, nullable=False)
    diagram_id = Column(Integer, primary_key=True)
    version = Column(Integer)
    definition = Column(VARBINARY(-1))
