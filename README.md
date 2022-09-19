# SAM: Sketch dAta Model

## Primitive Parameters

We describe all the parameters for primitives corresponding to the code in the files contained in the folder `/sam/catalog_primitive/`. Each primitive is a python class inheriting from the abstract class `Primitive` defined in `/sam/primitive.py`. In particular all primitives have a Boolean parameter `status_construction` indicating if a primitive is to be physically realized or simply serve as a reference for other primitives.

- **point** (dof: 2):
    - x (float): x coordinate
    - y (float): y coordinate

- **line**  (dof: 4):
    - pnt1 (point): starting point
    - pnt2 (point): ending point

- **circle** (dof: 3):
    - center (point): center
    - radius (float): radius

- **arc** (dof: 5):
    - center (point): center
    - radius (float): radius
    - angle_start (float): starting angle relative to the absolute horizontal axis
    - angle_end (float): ending angle relative to the absolute horizontal axis
    - radian (bool): if true then angles are in radians otherwise in degrees

Note that a point can have a field `parent` refering to the primitive it is used for in the case of a line, circle or arc.

## Constraint Parameters

Each constraint is a python class inheriting from the abstract class `Constraint` defined in `/sam/constraint.py`. Primitives involved by the constraint are stored as python references in the `references` attribute. The `references` attribute is a python list and accepts any type and any number of primitives. If the constraint involves only one primitive, there is only one element in the list. Constraints are divided into two groups: [geometric constraints](sam/catalog_constraint/geometric_constraint.py) and [dimension constraints](sam/catalog_constraint/dimension_constraint.py). Dimension constraints accept parameter values while geometric constraints do not.

#### Dimension constraints

- **angle**:
    - angle (float)

- **distance**:
    - distance_min (float)

- **length**:
    - length (float)

- **horizontalDistance**:
    - distance_min (float)

- **verticalDistance**:
    - distance_min (float)

- **radius**:
    - radius (float)

#### Geometric constraints

- **coincident**
- **equal**
- **horizontal**
- **midpoint**
- **vertical**
- **tangent**
- **parallel**
- **perpendicular**

## Installation (pip)

Follow this procedure if you intend to install sam as a dependency for your project.

Clone the repository, ensure your [pip](https://pip.pypa.io/en/stable/getting-started/) version is at least 22.0 and run

```sh
    cd sam
    pip install -e .
```

## Installation (dev)

Do NOT follow this if you want to install sam for the preprocessing or autoconstraint model repositories.
Follow this procedure if you intend to develop the sam repository itself. 

We use conda as an environment manager and poetry as dependency manager.

1. Generate a conda env 

First, create and activate a basic conda env from the [env.yml](./env/env.yml) file. 

Run 
```
    conda env create -f ./env/env.yml
```

then 

```
    conda activate basic_env
```



2. Install poetry and package dependencies

To install package dependencies with poetry, 

```
    poetry install
```

To update package dependencies, 
```
    poetry update
```


## Testing 

To run all the tests:

```
    poetry run pytest 
```

To run a specific test: 
```
    poetry run pytest path/my_test
```


See test coverage : [TO COMPLETE]