from robot.api.deco import keyword, library


@library("TestMath")
class TestMath:

    @keyword("Get Sum")
    def get_sum(self, a: int, b: int) -> int:
        return a + b
