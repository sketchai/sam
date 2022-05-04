# Conversion de séquences SketchGraphs en python Shaper.

Voir notebook conv_shaper.ipynb.

# Proposition de modèle pivot en mémoire, permettant de convertir les esquisses en différents formats
Les différents formats sont les suivants :
- json onShape
- format SketchGraphs
- python Shaper
- SVG

Comme dans SketchGraphs, on distingue les géométries (dessins : lignes, cercles etc.) des contraintes qui peuvent leur être appliquées (horizontal, parallel, perpendiculaire, length etc.).

## Géométries :

### Classe abstraite :
```
class geometryPivot(): # équivalent de la classe abstraite Entity de SketchGraphs (voir fichier _entity.py)
- id : entite.entityId
- auxiliary : entite.isConstruction
```
### Point :
**Proposition format pivot :**<br/>
```
class pointPivot(geometryPivot):
- x : entite.x
- y : entite.y
```
**Exemple :**
- **SketchGraphs :**
<br/>`NodeOp(label=<EntityType.Point: 0>, parameters={'isConstruction': True, 'x': 0.0, 'y': 0.0})`
- **Shaper :**
<br/>`SketchPoint_13 = Sketch_1.addPoint(0.0, 0.0)`
<br/>`SketchPoint_13.setAuxiliary(True)`
---
### Line :
**Proposition format pivot :**<br/>
```
class linePivot(geometryPivot):
- x_start : entite.start_point[0]
- y_start : entite.start_point[1]
- x_end : entite.end_point[0]
- y_end : entite.end_point[1]
```
Méthodes et attributs de "entite" (start_point, etc.) définies dans la classe Line du fichier _entity.py.

**Exemple :**
- **SketchGraphs :**
<br/>`NodeOp(label=<EntityType.Line: 1>, parameters={'isConstruction': False, 'dirX': 1.0, 'dirY': 0.0, 'pntX': -0.0014692433178424835, 'pntY': 0.08645165973590943, 'startParam': -0.1075, 'endParam': 0.10749999999999998})`
- **Shaper :**
<br/>`SketchLine_1 = Sketch_1.addLine(-0.10896924331784248, 0.08645165973590943, 0.1060307566821575, 0.086451659735
90943)`
---
### Circle :
**Proposition format pivot :**<br/>
```
class circlePivot(geometryPivot):
- x_center : entite.xCenter
- y_center : entite.yCenter
- radius : entite.radius
```
**Exemple :**
- **SketchGraphs :**
<br/>`NodeOp(label=<EntityType.Circle: 2>, parameters={'isConstruction': False, 'clockwise': False, 'xCenter': 0.0, 'yCenter': 0.0, 'xDir': 1.0, 'yDir': 0.0, 'radius': 0.03187218819219461})`
- **Shaper :**
<br/>`SketchCircle_1 = Sketch_1.addCircle(0.0, 0.0, 0.03187218819219461)`
---
### Arc of circle :

**Proposition format pivot:**<br/>
```
class arcPivot(geometryPivot):
- x_center : entite.center_point[0]
- y_center : entite.center_point[1]
- radius : entite.radius
- angle_start : entite.angle[1]
- angle_end : entite.angle[0]
```
Par convention, on est dans le sens trigonométrique et entre 0 et 360. Par exemple, l'arc AB où A(0,-1) et B(1,0) sera encodé par 
arc_AB_CC = arcPivot(x_center = 0, y_center=0, radius = 1 , angle_start=270, angle_end= 360) tandis que l'arc BA sera encodé par 
arc_AB_CW = arcPivot(x_center = 0, y_center=0, radius = 1 , angle_start= 0, angle_end= 270).

CC: Counter-Clock / CW: Clock-Wise


**Proposition format pivot pour la modélisation (à discuter):**<br/>
```
class arcPivot(geometryPivot):
- x_center : entite.center_point[0]
- y_center : entite.center_point[1]
- x_start : entite.start_point[0]
- y_start : entite.start_point[1]
- x_end : entite.end_point[0]
- y_end : entite.end_point[1]
```
**Exemple :**
- **SketchGraphs :**
<br/>`NodeOp(label=<EntityType.Arc: 6>, parameters={'isConstruction': False, 'clockwise': False, 'xCenter': -0.003, 'yCenter': -0.003, 'xDir': 1.0, 'yDir': 3.6739403974420594e-16, 'radius': 0.003, 'startParam': 1.5707963267948963, 'endParam': 3.141592653589793})`
- **Shaper :**
<br/>`SketchArc_8 = Sketch_1.addArc(-0.003, -0.003, -0.0030000000000000005, 0.0, -0.006, -0.003000000000000001, False)`
---
## Contraintes :

_UNSUPPORTED_CONSTRAINTS = (
    ConstraintType.Circular_Pattern,
    ConstraintType.Linear_Pattern,
    ConstraintType.Midpoint,
    ConstraintType.Mirror,
)

### Horizontal :
**Exemple : segment horizontal**
- **SketchGraphs :**
```
[NodeOp(label=<EntityType.External: 7>, parameters={}),
 NodeOp(label=<EntityType.Line: 1>, parameters={}),
 NodeOp(label=<SubnodeType.SN_Start: 101>, parameters={}),
 EdgeOp(label=<ConstraintType.Subnode: 101>, references=(2, 1), parameters={}),
 NodeOp(label=<SubnodeType.SN_End: 102>, parameters={}),
 EdgeOp(label=<ConstraintType.Subnode: 101>, references=(3, 1), parameters={}),
 EdgeOp(label=<ConstraintType.Horizontal: 4>, references=(1,), parameters={}),
 NodeOp(label=<EntityType.Stop: 8>, parameters={})]
```
- **Shaper :**
```
SketchLine_1 = Sketch_1.addLine(-0.5, 0.0, 0.5, 0.0)
Sketch_1.setHorizontal(SketchLine_1.result())
```
---
### Length :
**Exemple : segment horizontal avec longueur (cote)**
- **SketchGraphs :**
```
[NodeOp(label=<EntityType.External: 7>, parameters={}),
NodeOp(label=<EntityType.Line: 1>, parameters={}),
NodeOp(label=<SubnodeType.SN_Start: 101>, parameters={}),
EdgeOp(label=<ConstraintType.Subnode: 101>, references=(2, 1), parameters={}),
NodeOp(label=<SubnodeType.SN_End: 102>, parameters={}),
EdgeOp(label=<ConstraintType.Subnode: 101>, references=(3, 1), parameters={}),
EdgeOp(label=<ConstraintType.Horizontal: 4>, references=(1,), parameters={}),
EdgeOp(label=ConstraintType.Length, references=(1,), parameters={'direction': 'HORIZONTAL', 'length': '2'}),
NodeOp(label=<EntityType.Stop: 8>, parameters={})]
```
- **Shaper :**
```
SketchLine_1 = Sketch_1.addLine(-0.5, 0.0, 0.5, 0.0)
Sketch_1.setHorizontal(SketchLine_1.result())
Sketch_1.setLength(SketchLine_1.result(), 2)
```
---
### Parallel :
**Exemple : 2 segments parallèles**
- **SketchGraphs :**
```
seq = [
    NodeOp(label=EntityType.External),
    NodeOp(label=EntityType.Line,
        parameters={'isConstruction': False, 'dirX': 3, 'dirY': 1, 'pntX': 0, 'pntY': 0, 'startParam': 1, 'endParam': 3}),
    NodeOp(label=SubnodeType.SN_Start),
    EdgeOp(label=ConstraintType.Subnode, references=(2, 1)),
    NodeOp(label=SubnodeType.SN_End),
    EdgeOp(label=ConstraintType.Subnode, references=(3, 1)),
    NodeOp(label=EntityType.Line,
        parameters={'isConstruction': False, 'dirX': 0.5, 'dirY': 2, 'pntX': 0, 'pntY': 0, 'startParam': 1, 'endParam': 3}),
    EdgeOp(label=ConstraintType.Parallel, references=(4, 1), parameters={}),
    NodeOp(label=EntityType.Stop)]
```
- **Shaper :**
```
SketchLine_1 = Sketch_1.addLine(3, 1, 9, 3)
SketchLine_4 = Sketch_1.addLine(0.5, 2.0, 1.5, 6.0)
Sketch_1.setParallel(SketchLine_1.result(), SketchLine_4.result())
```
