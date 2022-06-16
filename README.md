# SAM: Sketch dAta Model

## Primitive Parameters

We describe all the parameters for primitives corresponding to the code in the files contained in the folder `/sam/catalog_primitive/`. Each primitive is a python class inheriting from the abstract class `Primitive` defined in `/sam/primitive.py`. In particular all primitives have a Boolean parameter `status_construction` indicating if a primitive is to be physically realized or simply serve as a reference for oterh primitives.

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

Each constraint is a python class inheriting from the abstract class `Constraint` defined in `/sam/constraint.py`. 

## Installation


We use conda as an environment manager and poetry as dependency manager.

1. Generate a conda env 

First, create and activate a basic conda env from the [env_prep.yml](./env/env.yml) file. 

Run 
```
    conda env create -f ./env/env.yml
```

then 

```
    conda activate basic_env
```

NB: it can be good to change the conda name env into [env_basic_conda.yml](./env/env_basic_conda.yml) file.


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

For running all the tests:

```
    poetry run pytest 
```

For running a specific test: 
```
    poetry run pytest path/my_test
```


See test coverage : [TO COMPLETE]