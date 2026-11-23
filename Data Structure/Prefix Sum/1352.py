class ProductOfNumbers:
    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
        else:
            self.products.append(self.products[-1] * num)

    def getProduct(self, k: int) -> int:
        return (
            0 if len(self.products) <= k else self.products[-1] // self.products[-k - 1]
        )


if __name__ == "__main__":
    obj = ProductOfNumbers()
    obj.add(3)
    obj.add(0)
    obj.add(2)
    obj.add(5)
    obj.add(4)
    print(obj.getProduct(2))
    print(obj.getProduct(3))
    print(obj.getProduct(4))
    obj.add(8)
    print(obj.getProduct(2))
