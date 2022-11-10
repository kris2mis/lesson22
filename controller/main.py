#ЗАДАЧА ИЗ stage_30
from model.point2d import Point2D  # импторт из пакета


def main():
    point1 = Point2D()
    point2 = Point2D()
    print(point1.calculate_distance(6))

    # print(hex(id(point)))
    # print((hex(hash(point))))


if __name__ == "__main__":
    main()
