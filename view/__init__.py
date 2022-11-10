# Send messages:

# 1) methods (object)
# point = Point2D()
# point.method ()
# Point2D.method () <-- Type Error


# 2) functions

# point = Point2D()
# point.function() <-- Type Error
# Point2D.function()


# 3) staticmethod (function )
# то, что можно вызвать на класе и на экземпляре - статические методы
# они для самодостаточной функции или кода

# point = Point2D()
# point.some()  замена на Point2D.some() <-- it's work
# Point2D.some() <--it's work


# 4) методы класса
# сlassmethod - это не функция, а полноценный метод

# point = Point2D()
# point.some() --> замена на Point2D.some()  <-- it's work
# Point2D.some() <--it's work
