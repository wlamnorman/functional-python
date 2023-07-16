import turtle
import numpy as np

N_BRANCH_LEVELS: int = 11

# controls trunk branch length and width
TRUNK_LEN = 100
TRUNK_WIDTH = 13

# controls reduction in width and length of branches per iteration
WIDTH_SHRINKAGE_FACTOR: float = 0.8
LEN_SHRINKAGE_FACTOR: float = 0.8

# controls separation of branches (the degree at which they grow out of previous branch)
DEG_OF_ROTATION = 30


def f_(x: float) -> float:
    return np.exp(-x) / (np.exp(-x) + 0.0001)


def generate_tree() -> None:
    def draw_trunk(trunk_len: float, trunk_width: float) -> None:
        turtle.width(trunk_width)
        turtle.left(90)
        turtle.penup()
        turtle.back(trunk_len * 1.5)
        turtle.pendown()
        turtle.forward(trunk_len)

    def iter_draw_branch(
        iterations_left: int,
        left: bool = True,
        right: bool = True,
        branch_len: float = TRUNK_LEN,
        branch_width: float = TRUNK_WIDTH,
    ) -> None:
        turtle.width(branch_width)

        if iterations_left == 0:
            green_shade = float(np.random.uniform(0.4, 1, 1)[0])
            turtle.pencolor((0, green_shade, 0))
            turtle.circle(branch_width * 8)
            turtle.pencolor("black")

        if iterations_left > 0:
            if left and np.random.binomial(1, 0.89, 1):
                length_scaling_factor: float = np.random.uniform(0.85, 1.1)
                rotational_error: float = np.random.uniform(-0.05, 0.05, 1)
                turtle.left(DEG_OF_ROTATION + rotational_error)
                turtle.forward(
                    branch_len * LEN_SHRINKAGE_FACTOR * length_scaling_factor
                )
                iter_draw_branch(
                    iterations_left - 1,
                    branch_len=branch_len
                    * LEN_SHRINKAGE_FACTOR
                    * length_scaling_factor,
                    branch_width=branch_width * WIDTH_SHRINKAGE_FACTOR,
                )
                turtle.back(branch_len * LEN_SHRINKAGE_FACTOR * length_scaling_factor)
                turtle.right(DEG_OF_ROTATION + rotational_error)

            if right and np.random.binomial(1, 0.96, 1):
                length_scaling_factor: float = np.random.uniform(0.85, 1.1)
                rotational_error: float = np.random.uniform(-0.05, 0.05, 1)
                turtle.right(DEG_OF_ROTATION + rotational_error)
                turtle.forward(
                    branch_len * LEN_SHRINKAGE_FACTOR * length_scaling_factor
                )
                if iterations_left > 0:
                    iter_draw_branch(
                        iterations_left - 1,
                        branch_len=branch_len
                        * LEN_SHRINKAGE_FACTOR
                        * length_scaling_factor,
                        branch_width=branch_width * WIDTH_SHRINKAGE_FACTOR,
                    )
                turtle.back(branch_len * LEN_SHRINKAGE_FACTOR * length_scaling_factor)
                turtle.left(DEG_OF_ROTATION + rotational_error)

            # add random branches (higher probability for outer branches)
            if np.random.uniform(0, 1, 1) < f_(iterations_left):
                b: int = np.random.binomial(1, 0.5, 1)
                if b:
                    iter_draw_branch(
                        iterations_left - 1,
                        left=True,
                        right=False,
                        branch_len=branch_len * WIDTH_SHRINKAGE_FACTOR * 0.7,
                        branch_width=branch_width * WIDTH_SHRINKAGE_FACTOR * 0.7,
                    )
                else:
                    iter_draw_branch(
                        iterations_left - 1,
                        left=False,
                        right=True,
                        branch_len=branch_len * WIDTH_SHRINKAGE_FACTOR * 0.7,
                        branch_width=branch_width * WIDTH_SHRINKAGE_FACTOR * 0.7,
                    )

        turtle.width(branch_width / WIDTH_SHRINKAGE_FACTOR)

    turtle.colormode()
    turtle.tracer(0)
    # turtle.speed(1)
    turtle.hideturtle()
    draw_trunk(TRUNK_LEN, TRUNK_WIDTH)
    iter_draw_branch(
        iterations_left=N_BRANCH_LEVELS, branch_len=TRUNK_LEN, branch_width=TRUNK_WIDTH
    )
    turtle.update()
    turtle.done()


if __name__ == "__main__":
    generate_tree()
