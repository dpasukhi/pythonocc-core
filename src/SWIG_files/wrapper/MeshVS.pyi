from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TColgp import *
from OCC.Core.SelectMgr import *
from OCC.Core.Quantity import *
from OCC.Core.Select3D import *
from OCC.Core.gp import *
from OCC.Core.TColStd import *
from OCC.Core.Bnd import *
from OCC.Core.TCollection import *
from OCC.Core.Graphic3d import *
from OCC.Core.SelectBasics import *
from OCC.Core.AIS import *
from OCC.Core.PrsMgr import *
from OCC.Core.Prs3d import *
from OCC.Core.Aspect import *

MeshVS_BuilderPriority = NewType('MeshVS_BuilderPriority', Standard_Integer)
MeshVS_ColorHasher = NewType('MeshVS_ColorHasher', Quantity_ColorHasher)
MeshVS_DisplayModeFlags = NewType('MeshVS_DisplayModeFlags', Standard_Integer)
#the following typedef cannot be wrapped as is
MeshVS_MapIteratorOfMapOfTwoNodes = NewType('MeshVS_MapIteratorOfMapOfTwoNodes', Any)
#the following typedef cannot be wrapped as is
MeshVS_MapOfTwoNodes = NewType('MeshVS_MapOfTwoNodes', Any)
MeshVS_MeshPtr = NewType('MeshVS_MeshPtr', MeshVS_Mesh)
#the following typedef cannot be wrapped as is
MeshVS_NodePair = NewType('MeshVS_NodePair', Any)
#the following typedef cannot be wrapped as is
MeshVS_SequenceOfPrsBuilder = NewType('MeshVS_SequenceOfPrsBuilder', Any)
#the following typedef cannot be wrapped as is
MeshVS_TwoColorsHasher = NewType('MeshVS_TwoColorsHasher', Any)
#the following typedef cannot be wrapped as is
MeshVS_TwoNodesHasher = NewType('MeshVS_TwoNodesHasher', Any)

class MeshVS_Array1OfSequenceOfInteger:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def __getitem__(self, index: int) -> TColStd_SequenceOfInteger: ...
    def __setitem__(self, index: int, value: TColStd_SequenceOfInteger) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[TColStd_SequenceOfInteger]: ...
    def next(self) -> TColStd_SequenceOfInteger: ...
    __next__ = next
    def Init(self, theValue: TColStd_SequenceOfInteger) -> None: ...
    def Size(self) -> int: ...
    def Length(self) -> int: ...
    def IsEmpty(self) -> bool: ...
    def Lower(self) -> int: ...
    def Upper(self) -> int: ...
    def IsDetectable(self) -> bool: ...
    def IsAllocated(self) -> bool: ...
    def First(self) -> TColStd_SequenceOfInteger: ...
    def Last(self) -> TColStd_SequenceOfInteger: ...
    def Value(self, theIndex: int) -> TColStd_SequenceOfInteger: ...
    def SetValue(self, theIndex: int, theValue: TColStd_SequenceOfInteger) -> None: ...

class MeshVS_PolyhedronVerts:
    def __init__(self) -> None: ...
    def __len__(self) -> int: ...
    def Size(self) -> int: ...
    def Clear(self) -> None: ...
    def First(self) -> False: ...
    def Last(self) -> False: ...
    def Append(self, theItem: False) -> False: ...
    def Prepend(self, theItem: False) -> False: ...
    def RemoveFirst(self) -> None: ...
    def Reverse(self) -> None: ...

class MeshVS_EntityType(IntEnum):
	MeshVS_ET_NONE: int = ...
	MeshVS_ET_Node: int = ...
	MeshVS_ET_0D: int = ...
	MeshVS_ET_Link: int = ...
	MeshVS_ET_Face: int = ...
	MeshVS_ET_Volume: int = ...
	MeshVS_ET_Element: int = ...
	MeshVS_ET_All: int = ...
MeshVS_ET_NONE = MeshVS_EntityType.MeshVS_ET_NONE
MeshVS_ET_Node = MeshVS_EntityType.MeshVS_ET_Node
MeshVS_ET_0D = MeshVS_EntityType.MeshVS_ET_0D
MeshVS_ET_Link = MeshVS_EntityType.MeshVS_ET_Link
MeshVS_ET_Face = MeshVS_EntityType.MeshVS_ET_Face
MeshVS_ET_Volume = MeshVS_EntityType.MeshVS_ET_Volume
MeshVS_ET_Element = MeshVS_EntityType.MeshVS_ET_Element
MeshVS_ET_All = MeshVS_EntityType.MeshVS_ET_All

class MeshVS_MeshSelectionMethod(IntEnum):
	MeshVS_MSM_PRECISE: int = ...
	MeshVS_MSM_NODES: int = ...
	MeshVS_MSM_BOX: int = ...
MeshVS_MSM_PRECISE = MeshVS_MeshSelectionMethod.MeshVS_MSM_PRECISE
MeshVS_MSM_NODES = MeshVS_MeshSelectionMethod.MeshVS_MSM_NODES
MeshVS_MSM_BOX = MeshVS_MeshSelectionMethod.MeshVS_MSM_BOX

class MeshVS_SelectionModeFlags(IntEnum):
	MeshVS_SMF_Mesh: int = ...
	MeshVS_SMF_Node: int = ...
	MeshVS_SMF_0D: int = ...
	MeshVS_SMF_Link: int = ...
	MeshVS_SMF_Face: int = ...
	MeshVS_SMF_Volume: int = ...
	MeshVS_SMF_Element: int = ...
	MeshVS_SMF_All: int = ...
	MeshVS_SMF_Group: int = ...
MeshVS_SMF_Mesh = MeshVS_SelectionModeFlags.MeshVS_SMF_Mesh
MeshVS_SMF_Node = MeshVS_SelectionModeFlags.MeshVS_SMF_Node
MeshVS_SMF_0D = MeshVS_SelectionModeFlags.MeshVS_SMF_0D
MeshVS_SMF_Link = MeshVS_SelectionModeFlags.MeshVS_SMF_Link
MeshVS_SMF_Face = MeshVS_SelectionModeFlags.MeshVS_SMF_Face
MeshVS_SMF_Volume = MeshVS_SelectionModeFlags.MeshVS_SMF_Volume
MeshVS_SMF_Element = MeshVS_SelectionModeFlags.MeshVS_SMF_Element
MeshVS_SMF_All = MeshVS_SelectionModeFlags.MeshVS_SMF_All
MeshVS_SMF_Group = MeshVS_SelectionModeFlags.MeshVS_SMF_Group

class MeshVS_DrawerAttribute(IntEnum):
	MeshVS_DA_InteriorStyle: int = ...
	MeshVS_DA_InteriorColor: int = ...
	MeshVS_DA_BackInteriorColor: int = ...
	MeshVS_DA_EdgeColor: int = ...
	MeshVS_DA_EdgeType: int = ...
	MeshVS_DA_EdgeWidth: int = ...
	MeshVS_DA_HatchStyle: int = ...
	MeshVS_DA_FrontMaterial: int = ...
	MeshVS_DA_BackMaterial: int = ...
	MeshVS_DA_BeamType: int = ...
	MeshVS_DA_BeamWidth: int = ...
	MeshVS_DA_BeamColor: int = ...
	MeshVS_DA_MarkerType: int = ...
	MeshVS_DA_MarkerColor: int = ...
	MeshVS_DA_MarkerScale: int = ...
	MeshVS_DA_TextColor: int = ...
	MeshVS_DA_TextHeight: int = ...
	MeshVS_DA_TextFont: int = ...
	MeshVS_DA_TextExpansionFactor: int = ...
	MeshVS_DA_TextSpace: int = ...
	MeshVS_DA_TextStyle: int = ...
	MeshVS_DA_TextDisplayType: int = ...
	MeshVS_DA_TextTexFont: int = ...
	MeshVS_DA_TextFontAspect: int = ...
	MeshVS_DA_VectorColor: int = ...
	MeshVS_DA_VectorMaxLength: int = ...
	MeshVS_DA_VectorArrowPart: int = ...
	MeshVS_DA_IsAllowOverlapped: int = ...
	MeshVS_DA_Reflection: int = ...
	MeshVS_DA_ColorReflection: int = ...
	MeshVS_DA_ShrinkCoeff: int = ...
	MeshVS_DA_MaxFaceNodes: int = ...
	MeshVS_DA_ComputeTime: int = ...
	MeshVS_DA_ComputeSelectionTime: int = ...
	MeshVS_DA_DisplayNodes: int = ...
	MeshVS_DA_SelectableAuto: int = ...
	MeshVS_DA_ShowEdges: int = ...
	MeshVS_DA_SmoothShading: int = ...
	MeshVS_DA_SupressBackFaces: int = ...
	MeshVS_DA_User: int = ...
MeshVS_DA_InteriorStyle = MeshVS_DrawerAttribute.MeshVS_DA_InteriorStyle
MeshVS_DA_InteriorColor = MeshVS_DrawerAttribute.MeshVS_DA_InteriorColor
MeshVS_DA_BackInteriorColor = MeshVS_DrawerAttribute.MeshVS_DA_BackInteriorColor
MeshVS_DA_EdgeColor = MeshVS_DrawerAttribute.MeshVS_DA_EdgeColor
MeshVS_DA_EdgeType = MeshVS_DrawerAttribute.MeshVS_DA_EdgeType
MeshVS_DA_EdgeWidth = MeshVS_DrawerAttribute.MeshVS_DA_EdgeWidth
MeshVS_DA_HatchStyle = MeshVS_DrawerAttribute.MeshVS_DA_HatchStyle
MeshVS_DA_FrontMaterial = MeshVS_DrawerAttribute.MeshVS_DA_FrontMaterial
MeshVS_DA_BackMaterial = MeshVS_DrawerAttribute.MeshVS_DA_BackMaterial
MeshVS_DA_BeamType = MeshVS_DrawerAttribute.MeshVS_DA_BeamType
MeshVS_DA_BeamWidth = MeshVS_DrawerAttribute.MeshVS_DA_BeamWidth
MeshVS_DA_BeamColor = MeshVS_DrawerAttribute.MeshVS_DA_BeamColor
MeshVS_DA_MarkerType = MeshVS_DrawerAttribute.MeshVS_DA_MarkerType
MeshVS_DA_MarkerColor = MeshVS_DrawerAttribute.MeshVS_DA_MarkerColor
MeshVS_DA_MarkerScale = MeshVS_DrawerAttribute.MeshVS_DA_MarkerScale
MeshVS_DA_TextColor = MeshVS_DrawerAttribute.MeshVS_DA_TextColor
MeshVS_DA_TextHeight = MeshVS_DrawerAttribute.MeshVS_DA_TextHeight
MeshVS_DA_TextFont = MeshVS_DrawerAttribute.MeshVS_DA_TextFont
MeshVS_DA_TextExpansionFactor = MeshVS_DrawerAttribute.MeshVS_DA_TextExpansionFactor
MeshVS_DA_TextSpace = MeshVS_DrawerAttribute.MeshVS_DA_TextSpace
MeshVS_DA_TextStyle = MeshVS_DrawerAttribute.MeshVS_DA_TextStyle
MeshVS_DA_TextDisplayType = MeshVS_DrawerAttribute.MeshVS_DA_TextDisplayType
MeshVS_DA_TextTexFont = MeshVS_DrawerAttribute.MeshVS_DA_TextTexFont
MeshVS_DA_TextFontAspect = MeshVS_DrawerAttribute.MeshVS_DA_TextFontAspect
MeshVS_DA_VectorColor = MeshVS_DrawerAttribute.MeshVS_DA_VectorColor
MeshVS_DA_VectorMaxLength = MeshVS_DrawerAttribute.MeshVS_DA_VectorMaxLength
MeshVS_DA_VectorArrowPart = MeshVS_DrawerAttribute.MeshVS_DA_VectorArrowPart
MeshVS_DA_IsAllowOverlapped = MeshVS_DrawerAttribute.MeshVS_DA_IsAllowOverlapped
MeshVS_DA_Reflection = MeshVS_DrawerAttribute.MeshVS_DA_Reflection
MeshVS_DA_ColorReflection = MeshVS_DrawerAttribute.MeshVS_DA_ColorReflection
MeshVS_DA_ShrinkCoeff = MeshVS_DrawerAttribute.MeshVS_DA_ShrinkCoeff
MeshVS_DA_MaxFaceNodes = MeshVS_DrawerAttribute.MeshVS_DA_MaxFaceNodes
MeshVS_DA_ComputeTime = MeshVS_DrawerAttribute.MeshVS_DA_ComputeTime
MeshVS_DA_ComputeSelectionTime = MeshVS_DrawerAttribute.MeshVS_DA_ComputeSelectionTime
MeshVS_DA_DisplayNodes = MeshVS_DrawerAttribute.MeshVS_DA_DisplayNodes
MeshVS_DA_SelectableAuto = MeshVS_DrawerAttribute.MeshVS_DA_SelectableAuto
MeshVS_DA_ShowEdges = MeshVS_DrawerAttribute.MeshVS_DA_ShowEdges
MeshVS_DA_SmoothShading = MeshVS_DrawerAttribute.MeshVS_DA_SmoothShading
MeshVS_DA_SupressBackFaces = MeshVS_DrawerAttribute.MeshVS_DA_SupressBackFaces
MeshVS_DA_User = MeshVS_DrawerAttribute.MeshVS_DA_User

class MeshVS_Buffer:
	@overload
	def __init__(self, theSize: int) -> None: ...

class MeshVS_CommonSensitiveEntity(Select3D_SensitiveSet):
	def __init__(self, theOwner: SelectMgr_EntityOwner, theParentMesh: MeshVS_Mesh, theSelMethod: MeshVS_MeshSelectionMethod) -> None: ...
	def BoundingBox(self) -> Select3D_BndBox3d: ...
	def Box(self, theIdx: int) -> Select3D_BndBox3d: ...
	def Center(self, theIdx: int, theAxis: int) -> float: ...
	def CenterOfGeometry(self) -> gp_Pnt: ...
	def GetConnected(self) -> Select3D_SensitiveEntity: ...
	def NbSubElements(self) -> int: ...
	def Size(self) -> int: ...
	def Swap(self, theIdx1: int, theIdx2: int) -> None: ...

class MeshVS_DataSource(Standard_Transient):
	def Get3DGeom(self, ID: int, Data: MeshVS_HArray1OfSequenceOfInteger) -> Tuple[bool, int]: ...
	def GetAddr(self, ID: int, IsElement: bool) -> None: ...
	def GetAllElements(self) -> TColStd_PackedMapOfInteger: ...
	def GetAllGroups(self, Ids: TColStd_PackedMapOfInteger) -> None: ...
	def GetAllNodes(self) -> TColStd_PackedMapOfInteger: ...
	def GetBoundingBox(self) -> Bnd_Box: ...
	@overload
	def GetDetectedEntities(self, Prs: MeshVS_Mesh, X: float, Y: float, aTol: float, Nodes: TColStd_HPackedMapOfInteger, Elements: TColStd_HPackedMapOfInteger) -> Tuple[bool, float]: ...
	@overload
	def GetDetectedEntities(self, Prs: MeshVS_Mesh, XMin: float, YMin: float, XMax: float, YMax: float, aTol: float, Nodes: TColStd_HPackedMapOfInteger, Elements: TColStd_HPackedMapOfInteger) -> bool: ...
	@overload
	def GetDetectedEntities(self, Prs: MeshVS_Mesh, Polyline: TColgp_Array1OfPnt2d, aBox: Bnd_Box2d, aTol: float, Nodes: TColStd_HPackedMapOfInteger, Elements: TColStd_HPackedMapOfInteger) -> bool: ...
	@overload
	def GetDetectedEntities(self, Prs: MeshVS_Mesh, Nodes: TColStd_HPackedMapOfInteger, Elements: TColStd_HPackedMapOfInteger) -> bool: ...
	def GetGeom(self, ID: int, IsElement: bool, Coords: TColStd_Array1OfReal, Type: MeshVS_EntityType) -> Tuple[bool, int]: ...
	def GetGeomType(self, ID: int, IsElement: bool, Type: MeshVS_EntityType) -> bool: ...
	def GetGroup(self, Id: int, Type: MeshVS_EntityType, Ids: TColStd_PackedMapOfInteger) -> bool: ...
	def GetGroupAddr(self, ID: int) -> None: ...
	def GetNodeNormal(self, ranknode: int, ElementId: int) -> Tuple[bool, float, float, float]: ...
	def GetNodesByElement(self, ID: int, NodeIDs: TColStd_Array1OfInteger) -> Tuple[bool, int]: ...
	def GetNormal(self, Id: int, Max: int) -> Tuple[bool, float, float, float]: ...
	def GetNormalsByElement(self, Id: int, IsNodal: bool, MaxNodes: int, Normals: TColStd_HArray1OfReal) -> bool: ...
	def IsAdvancedSelectionEnabled(self) -> bool: ...

class MeshVS_Drawer(Standard_Transient):
	def Assign(self, aDrawer: MeshVS_Drawer) -> None: ...
	def GetAsciiString(self, Key: int, Value: TCollection_AsciiString) -> bool: ...
	def GetBoolean(self, Key: int) -> Tuple[bool, bool]: ...
	def GetColor(self, Key: int, Value: Quantity_Color) -> bool: ...
	def GetDouble(self, Key: int) -> Tuple[bool, float]: ...
	def GetInteger(self, Key: int) -> Tuple[bool, int]: ...
	def GetMaterial(self, Key: int, Value: Graphic3d_MaterialAspect) -> bool: ...
	def RemoveAsciiString(self, Key: int) -> bool: ...
	def RemoveBoolean(self, Key: int) -> bool: ...
	def RemoveColor(self, Key: int) -> bool: ...
	def RemoveDouble(self, Key: int) -> bool: ...
	def RemoveInteger(self, Key: int) -> bool: ...
	def RemoveMaterial(self, Key: int) -> bool: ...
	def SetAsciiString(self, Key: int, Value: TCollection_AsciiString) -> None: ...
	def SetBoolean(self, Key: int, Value: bool) -> None: ...
	def SetColor(self, Key: int, Value: Quantity_Color) -> None: ...
	def SetDouble(self, Key: int, Value: float) -> None: ...
	def SetInteger(self, Key: int, Value: int) -> None: ...
	def SetMaterial(self, Key: int, Value: Graphic3d_MaterialAspect) -> None: ...

class MeshVS_DummySensitiveEntity(Select3D_SensitiveEntity):
	def __init__(self, theOwnerId: SelectMgr_EntityOwner) -> None: ...
	def BVH(self) -> None: ...
	def BoundingBox(self) -> Select3D_BndBox3d: ...
	def CenterOfGeometry(self) -> gp_Pnt: ...
	def Clear(self) -> None: ...
	def HasInitLocation(self) -> bool: ...
	def InvInitLocation(self) -> gp_GTrsf: ...
	def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
	def NbSubElements(self) -> int: ...

class MeshVS_Mesh(AIS_InteractiveObject):
	def __init__(self, theIsAllowOverlapped: Optional[bool] = False) -> None: ...
	def AcceptDisplayMode(self, theMode: int) -> bool: ...
	def AddBuilder(self, Builder: MeshVS_PrsBuilder, TreatAsHilighter: Optional[bool] = False) -> None: ...
	def ClearSelected(self) -> None: ...
	def Compute(self, PM: PrsMgr_PresentationManager3d, Prs: Prs3d_Presentation, DisplayMode: int) -> None: ...
	def ComputeSelection(self, Sel: SelectMgr_Selection, SelectMode: int) -> None: ...
	def FindBuilder(self, TypeString: str) -> MeshVS_PrsBuilder: ...
	def GetBuilder(self, Index: int) -> MeshVS_PrsBuilder: ...
	def GetBuilderById(self, Id: int) -> MeshVS_PrsBuilder: ...
	def GetBuildersCount(self) -> int: ...
	def GetDataSource(self) -> MeshVS_DataSource: ...
	def GetDrawer(self) -> MeshVS_Drawer: ...
	def GetFreeId(self) -> int: ...
	def GetHiddenElems(self) -> TColStd_HPackedMapOfInteger: ...
	def GetHiddenNodes(self) -> TColStd_HPackedMapOfInteger: ...
	def GetHilighter(self) -> MeshVS_PrsBuilder: ...
	def GetMeshSelMethod(self) -> MeshVS_MeshSelectionMethod: ...
	def GetOwnerMaps(self, IsElement: bool) -> MeshVS_DataMapOfIntegerOwner: ...
	def GetSelectableNodes(self) -> TColStd_HPackedMapOfInteger: ...
	def HilightOwnerWithColor(self, thePM: PrsMgr_PresentationManager3d, theColor: Prs3d_Drawer, theOwner: SelectMgr_EntityOwner) -> None: ...
	def HilightSelected(self, PM: PrsMgr_PresentationManager3d, Owners: SelectMgr_SequenceOfOwner) -> None: ...
	def IsHiddenElem(self, ID: int) -> bool: ...
	def IsHiddenNode(self, ID: int) -> bool: ...
	def IsSelectableElem(self, ID: int) -> bool: ...
	def IsSelectableNode(self, ID: int) -> bool: ...
	def IsWholeMeshOwner(self, theOwner: SelectMgr_EntityOwner) -> bool: ...
	def RemoveBuilder(self, Index: int) -> None: ...
	def RemoveBuilderById(self, Id: int) -> None: ...
	def SetDataSource(self, aDataSource: MeshVS_DataSource) -> None: ...
	def SetDrawer(self, aDrawer: MeshVS_Drawer) -> None: ...
	def SetHiddenElems(self, Ids: TColStd_HPackedMapOfInteger) -> None: ...
	def SetHiddenNodes(self, Ids: TColStd_HPackedMapOfInteger) -> None: ...
	@overload
	def SetHilighter(self, Builder: MeshVS_PrsBuilder) -> None: ...
	@overload
	def SetHilighter(self, Index: int) -> bool: ...
	def SetHilighterById(self, Id: int) -> bool: ...
	def SetMeshSelMethod(self, M: MeshVS_MeshSelectionMethod) -> None: ...
	def SetSelectableNodes(self, Ids: TColStd_HPackedMapOfInteger) -> None: ...
	def UpdateSelectableNodes(self) -> None: ...

class MeshVS_MeshEntityOwner(SelectMgr_EntityOwner):
	def __init__(self, SelObj: SelectMgr_SOPtr, ID: int, MeshEntity: None, Type: MeshVS_EntityType, Priority: Optional[int] = 0, IsGroup: Optional[bool] = False) -> None: ...
	def Clear(self, PM: PrsMgr_PresentationManager, Mode: Optional[int] = 0) -> None: ...
	def HilightWithColor(self, thePM: PrsMgr_PresentationManager3d, theStyle: Prs3d_Drawer, theMode: Optional[int] = 0) -> None: ...
	def ID(self) -> int: ...
	def IsGroup(self) -> bool: ...
	def IsHilighted(self, PM: PrsMgr_PresentationManager, Mode: Optional[int] = 0) -> bool: ...
	def Owner(self) -> None: ...
	def Type(self) -> MeshVS_EntityType: ...
	def Unhilight(self, PM: PrsMgr_PresentationManager, Mode: Optional[int] = 0) -> None: ...

class MeshVS_MeshOwner(SelectMgr_EntityOwner):
	def __init__(self, theSelObj: SelectMgr_SOPtr, theDS: MeshVS_DataSource, thePriority: Optional[int] = 0) -> None: ...
	def AddSelectedEntities(self, Nodes: TColStd_HPackedMapOfInteger, Elems: TColStd_HPackedMapOfInteger) -> None: ...
	def ClearSelectedEntities(self) -> None: ...
	def GetDataSource(self) -> MeshVS_DataSource: ...
	def GetDetectedElements(self) -> TColStd_HPackedMapOfInteger: ...
	def GetDetectedNodes(self) -> TColStd_HPackedMapOfInteger: ...
	def GetSelectedElements(self) -> TColStd_HPackedMapOfInteger: ...
	def GetSelectedNodes(self) -> TColStd_HPackedMapOfInteger: ...
	def HilightWithColor(self, thePM: PrsMgr_PresentationManager3d, theColor: Prs3d_Drawer, theMode: Optional[int] = 0) -> None: ...
	def IsForcedHilight(self) -> bool: ...
	def SetDetectedEntities(self, Nodes: TColStd_HPackedMapOfInteger, Elems: TColStd_HPackedMapOfInteger) -> None: ...
	def Unhilight(self, PM: PrsMgr_PresentationManager, Mode: Optional[int] = 0) -> None: ...

class MeshVS_PrsBuilder(Standard_Transient):
	def Build(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None: ...
	def CustomBuild(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, DisplayMode: int) -> None: ...
	def CustomSensitiveEntity(self, Owner: SelectMgr_EntityOwner, SelectMode: int) -> Select3D_SensitiveEntity: ...
	def GetDataSource(self) -> MeshVS_DataSource: ...
	def GetDrawer(self) -> MeshVS_Drawer: ...
	def GetFlags(self) -> int: ...
	def GetId(self) -> int: ...
	def GetPresentationManager(self) -> PrsMgr_PresentationManager3d: ...
	def GetPriority(self) -> int: ...
	def IsExcludingOn(self) -> bool: ...
	def SetDataSource(self, newDS: MeshVS_DataSource) -> None: ...
	def SetDrawer(self, newDr: MeshVS_Drawer) -> None: ...
	def SetExcluding(self, state: bool) -> None: ...
	def SetPresentationManager(self, thePrsMgr: PrsMgr_PresentationManager3d) -> None: ...
	def TestFlags(self, DisplayMode: int) -> bool: ...

class MeshVS_SensitiveFace(Select3D_SensitiveFace):
	def __init__(self, theOwner: SelectMgr_EntityOwner, thePoints: TColgp_Array1OfPnt, theSensType: Optional[Select3D_TypeOfSensitivity] = Select3D_TOS_INTERIOR) -> None: ...

class MeshVS_SensitiveMesh(Select3D_SensitiveEntity):
	def __init__(self, theOwner: SelectMgr_EntityOwner, theMode: Optional[int] = 0) -> None: ...
	def BoundingBox(self) -> Select3D_BndBox3d: ...
	def CenterOfGeometry(self) -> gp_Pnt: ...
	def GetConnected(self) -> Select3D_SensitiveEntity: ...
	def GetMode(self) -> int: ...
	def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
	def NbSubElements(self) -> int: ...

class MeshVS_SensitivePolyhedron(Select3D_SensitiveEntity):
	def __init__(self, theOwner: SelectMgr_EntityOwner, theNodes: TColgp_Array1OfPnt, theTopo: MeshVS_HArray1OfSequenceOfInteger) -> None: ...
	def BoundingBox(self) -> Select3D_BndBox3d: ...
	def CenterOfGeometry(self) -> gp_Pnt: ...
	def GetConnected(self) -> Select3D_SensitiveEntity: ...
	def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
	def NbSubElements(self) -> int: ...

class MeshVS_SensitiveQuad(Select3D_SensitiveEntity):
	@overload
	def __init__(self, theOwner: SelectMgr_EntityOwner, theQuadVerts: TColgp_Array1OfPnt) -> None: ...
	@overload
	def __init__(self, theOwner: SelectMgr_EntityOwner, thePnt1: gp_Pnt, thePnt2: gp_Pnt, thePnt3: gp_Pnt, thePnt4: gp_Pnt) -> None: ...
	def BoundingBox(self) -> Select3D_BndBox3d: ...
	def CenterOfGeometry(self) -> gp_Pnt: ...
	def GetConnected(self) -> Select3D_SensitiveEntity: ...
	def Matches(self, theMgr: SelectBasics_SelectingVolumeManager, thePickResult: SelectBasics_PickResult) -> bool: ...
	def NbSubElements(self) -> int: ...

class MeshVS_SensitiveSegment(Select3D_SensitiveSegment):
	def __init__(self, theOwner: SelectMgr_EntityOwner, theFirstPnt: gp_Pnt, theLastPnt: gp_Pnt) -> None: ...

class MeshVS_SymmetricPairHasher:
	@staticmethod
	def HashCode(theNodePair: MeshVS_NodePair, theUpperBound: int) -> int: ...
	@staticmethod
	def IsEqual(thePair1: MeshVS_NodePair, thePair2: MeshVS_NodePair) -> bool: ...

class MeshVS_Tool:
	@overload
	@staticmethod
	def CreateAspectFillArea3d(theDr: MeshVS_Drawer, UseDefaults: Optional[bool] = True) -> Graphic3d_AspectFillArea3d: ...
	@overload
	@staticmethod
	def CreateAspectFillArea3d(theDr: MeshVS_Drawer, Mat: Graphic3d_MaterialAspect, UseDefaults: Optional[bool] = True) -> Graphic3d_AspectFillArea3d: ...
	@staticmethod
	def CreateAspectLine3d(theDr: MeshVS_Drawer, UseDefaults: Optional[bool] = True) -> Graphic3d_AspectLine3d: ...
	@staticmethod
	def CreateAspectMarker3d(theDr: MeshVS_Drawer, UseDefaults: Optional[bool] = True) -> Graphic3d_AspectMarker3d: ...
	@staticmethod
	def CreateAspectText3d(theDr: MeshVS_Drawer, UseDefaults: Optional[bool] = True) -> Graphic3d_AspectText3d: ...
	@staticmethod
	def GetAverageNormal(Nodes: TColStd_Array1OfReal, Norm: gp_Vec) -> bool: ...
	@staticmethod
	def GetNormal(Nodes: TColStd_Array1OfReal, Norm: gp_Vec) -> bool: ...

class MeshVS_TwoColors:
	pass

class MeshVS_TwoNodes:
	def __init__(self, aFirst: Optional[int] = 0, aSecond: Optional[int] = 0) -> None: ...

class MeshVS_DataSource3D(MeshVS_DataSource):
	@staticmethod
	def CreatePrismTopology(BasePoints: int) -> MeshVS_HArray1OfSequenceOfInteger: ...
	@staticmethod
	def CreatePyramidTopology(BasePoints: int) -> MeshVS_HArray1OfSequenceOfInteger: ...
	def GetPrismTopology(self, BasePoints: int) -> MeshVS_HArray1OfSequenceOfInteger: ...
	def GetPyramidTopology(self, BasePoints: int) -> MeshVS_HArray1OfSequenceOfInteger: ...

class MeshVS_DeformedDataSource(MeshVS_DataSource):
	def __init__(self, theNonDeformDS: MeshVS_DataSource, theMagnify: float) -> None: ...
	def Get3DGeom(self, ID: int, Data: MeshVS_HArray1OfSequenceOfInteger) -> Tuple[bool, int]: ...
	def GetAddr(self, ID: int, IsElement: bool) -> None: ...
	def GetAllElements(self) -> TColStd_PackedMapOfInteger: ...
	def GetAllNodes(self) -> TColStd_PackedMapOfInteger: ...
	def GetGeom(self, ID: int, IsElement: bool, Coords: TColStd_Array1OfReal, Type: MeshVS_EntityType) -> Tuple[bool, int]: ...
	def GetGeomType(self, ID: int, IsElement: bool, Type: MeshVS_EntityType) -> bool: ...
	def GetMagnify(self) -> float: ...
	def GetNodesByElement(self, ID: int, NodeIDs: TColStd_Array1OfInteger) -> Tuple[bool, int]: ...
	def GetNonDeformedDataSource(self) -> MeshVS_DataSource: ...
	def GetVector(self, ID: int, Vect: gp_Vec) -> bool: ...
	def GetVectors(self) -> MeshVS_DataMapOfIntegerVector: ...
	def SetMagnify(self, theMagnify: float) -> None: ...
	def SetNonDeformedDataSource(self, theDS: MeshVS_DataSource) -> None: ...
	def SetVector(self, ID: int, Vect: gp_Vec) -> None: ...
	def SetVectors(self, Map: MeshVS_DataMapOfIntegerVector) -> None: ...

class MeshVS_ElementalColorPrsBuilder(MeshVS_PrsBuilder):
	def Build(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None: ...
	def GetColor1(self, ID: int, theColor: Quantity_Color) -> bool: ...
	@overload
	def GetColor2(self, ID: int, theColor: MeshVS_TwoColors) -> bool: ...
	@overload
	def GetColor2(self, ID: int, theColor1: Quantity_Color, theColor2: Quantity_Color) -> bool: ...
	def GetColors1(self) -> MeshVS_DataMapOfIntegerColor: ...
	def GetColors2(self) -> MeshVS_DataMapOfIntegerTwoColors: ...
	def HasColors1(self) -> bool: ...
	def HasColors2(self) -> bool: ...
	def SetColor1(self, ID: int, theColor: Quantity_Color) -> None: ...
	@overload
	def SetColor2(self, ID: int, theTwoColors: MeshVS_TwoColors) -> None: ...
	@overload
	def SetColor2(self, ID: int, theColor1: Quantity_Color, theColor2: Quantity_Color) -> None: ...
	def SetColors1(self, Map: MeshVS_DataMapOfIntegerColor) -> None: ...
	def SetColors2(self, Map: MeshVS_DataMapOfIntegerTwoColors) -> None: ...

class MeshVS_MeshPrsBuilder(MeshVS_PrsBuilder):
	@staticmethod
	def AddVolumePrs(Topo: MeshVS_HArray1OfSequenceOfInteger, Nodes: TColStd_Array1OfReal, NbNodes: int, Array: Graphic3d_ArrayOfPrimitives, IsReflected: bool, IsShrinked: bool, IsSelect: bool, ShrinkCoef: float) -> None: ...
	def Build(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None: ...
	def BuildElements(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, DisplayMode: int) -> None: ...
	def BuildHilightPrs(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IsElement: bool) -> None: ...
	def BuildNodes(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, DisplayMode: int) -> None: ...
	@staticmethod
	def HowManyPrimitives(Topo: MeshVS_HArray1OfSequenceOfInteger, AsPolygons: bool, IsSelect: bool, NbNodes: int) -> Tuple[int, int]: ...

class MeshVS_NodalColorPrsBuilder(MeshVS_PrsBuilder):
	def AddVolumePrs(self, theTopo: MeshVS_HArray1OfSequenceOfInteger, theNodes: TColStd_Array1OfInteger, theCoords: TColStd_Array1OfReal, theArray: Graphic3d_ArrayOfPrimitives, theIsShaded: bool, theNbColors: int, theNbTexColors: int, theColorRatio: float) -> None: ...
	def Build(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, IsElement: bool, DisplayMode: int) -> None: ...
	def GetColor(self, ID: int, theColor: Quantity_Color) -> bool: ...
	def GetColorMap(self) -> Aspect_SequenceOfColor: ...
	def GetColors(self) -> MeshVS_DataMapOfIntegerColor: ...
	def GetInvalidColor(self) -> Quantity_Color: ...
	def GetTextureCoord(self, theID: int) -> float: ...
	def GetTextureCoords(self) -> TColStd_DataMapOfIntegerReal: ...
	def HasColors(self) -> bool: ...
	def IsUseTexture(self) -> bool: ...
	def SetColor(self, ID: int, theColor: Quantity_Color) -> None: ...
	def SetColorMap(self, theColors: Aspect_SequenceOfColor) -> None: ...
	def SetColors(self, Map: MeshVS_DataMapOfIntegerColor) -> None: ...
	def SetInvalidColor(self, theInvalidColor: Quantity_Color) -> None: ...
	def SetTextureCoord(self, theID: int, theCoord: float) -> None: ...
	def SetTextureCoords(self, theMap: TColStd_DataMapOfIntegerReal) -> None: ...
	def UseTexture(self, theToUse: bool) -> None: ...

class MeshVS_TextPrsBuilder(MeshVS_PrsBuilder):
	def Build(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, IsElement: bool, theDisplayMode: int) -> None: ...
	def GetText(self, IsElement: bool, ID: int, Text: TCollection_AsciiString) -> bool: ...
	def GetTexts(self, IsElement: bool) -> MeshVS_DataMapOfIntegerAsciiString: ...
	def HasTexts(self, IsElement: bool) -> bool: ...
	def SetText(self, IsElement: bool, ID: int, Text: TCollection_AsciiString) -> None: ...
	def SetTexts(self, IsElement: bool, Map: MeshVS_DataMapOfIntegerAsciiString) -> None: ...

class MeshVS_VectorPrsBuilder(MeshVS_PrsBuilder):
	def Build(self, Prs: Prs3d_Presentation, IDs: TColStd_PackedMapOfInteger, IDsToExclude: TColStd_PackedMapOfInteger, IsElement: bool, theDisplayMode: int) -> None: ...
	def DrawVector(self, theTrsf: gp_Trsf, Length: float, MaxLength: float, ArrowPoints: TColgp_Array1OfPnt, Lines: Graphic3d_ArrayOfPrimitives, ArrowLines: Graphic3d_ArrayOfPrimitives, Triangles: Graphic3d_ArrayOfPrimitives) -> None: ...
	def GetMinMaxVectorValue(self, IsElement: bool) -> Tuple[float, float]: ...
	def GetVector(self, IsElement: bool, ID: int, Vect: gp_Vec) -> bool: ...
	def GetVectors(self, IsElement: bool) -> MeshVS_DataMapOfIntegerVector: ...
	def HasVectors(self, IsElement: bool) -> bool: ...
	def SetSimplePrsMode(self, IsSimpleArrow: bool) -> None: ...
	def SetSimplePrsParams(self, theLineWidthParam: float, theStartParam: float, theEndParam: float) -> None: ...
	def SetVector(self, IsElement: bool, ID: int, Vect: gp_Vec) -> None: ...
	def SetVectors(self, IsElement: bool, Map: MeshVS_DataMapOfIntegerVector) -> None: ...
	@staticmethod
	def calculateArrow(Points: TColgp_Array1OfPnt, Length: float, ArrowPart: float) -> float: ...

# harray1 classes

class MeshVS_HArray1OfSequenceOfInteger(MeshVS_Array1OfSequenceOfInteger, Standard_Transient):
    def __init__(self, theLower: int, theUpper: int) -> None: ...
    def Array1(self) -> MeshVS_Array1OfSequenceOfInteger: ...

# harray2 classes
# hsequence classes

MeshVS_SymmetricPairHasher_HashCode = MeshVS_SymmetricPairHasher.HashCode
MeshVS_SymmetricPairHasher_IsEqual = MeshVS_SymmetricPairHasher.IsEqual
MeshVS_Tool_CreateAspectFillArea3d = MeshVS_Tool.CreateAspectFillArea3d
MeshVS_Tool_CreateAspectFillArea3d = MeshVS_Tool.CreateAspectFillArea3d
MeshVS_Tool_CreateAspectLine3d = MeshVS_Tool.CreateAspectLine3d
MeshVS_Tool_CreateAspectMarker3d = MeshVS_Tool.CreateAspectMarker3d
MeshVS_Tool_CreateAspectText3d = MeshVS_Tool.CreateAspectText3d
MeshVS_Tool_GetAverageNormal = MeshVS_Tool.GetAverageNormal
MeshVS_Tool_GetNormal = MeshVS_Tool.GetNormal
MeshVS_DataSource3D_CreatePrismTopology = MeshVS_DataSource3D.CreatePrismTopology
MeshVS_DataSource3D_CreatePyramidTopology = MeshVS_DataSource3D.CreatePyramidTopology
MeshVS_MeshPrsBuilder_AddVolumePrs = MeshVS_MeshPrsBuilder.AddVolumePrs
MeshVS_MeshPrsBuilder_HowManyPrimitives = MeshVS_MeshPrsBuilder.HowManyPrimitives
MeshVS_VectorPrsBuilder_calculateArrow = MeshVS_VectorPrsBuilder.calculateArrow