def _get_linestyle(entity):
    return '--' if entity.isConstruction else '-'


def sketch_point(ax, point: Point, color='black', show_subnodes=False):
    ax.scatter(point.x, point.y, c=color, marker='.')


def sketch_circle(ax, circle: Circle, color='black', show_subnodes=False):
    patch = matplotlib.patches.Circle(
        (circle.xCenter, circle.yCenter), circle.radius,
        fill=False, linestyle=_get_linestyle(circle), color=color)
    if show_subnodes:
        ax.scatter(circle.xCenter, circle.yCenter, c=color, marker='.', zorder=20)
    ax.add_patch(patch)


def sketch_arc(ax, arc: Arc, color='black', show_subnodes=False):
    angle = math.atan2(arc.yDir, arc.xDir) * 180 / math.pi
    startParam = arc.startParam * 180 / math.pi
    endParam = arc.endParam * 180 / math.pi

    if arc.clockwise:
        startParam, endParam = -endParam, -startParam

    ax.add_patch(
        matplotlib.patches.Arc(
            (arc.xCenter, arc.yCenter), 2 * arc.radius, 2 * arc.radius,
            angle=angle,
            theta1=startParam,
            theta2=endParam,
            linestyle=self., color=color))
