class Test:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size

    def get_visible_items(self):
        for x in range(self.page_size):
            print(self.items[x])

    def prev_page(self):
        print(self.items)

    def first_page(self):
        for f in range(self.page_size):
            print(self.items[f])

    def last(self):
        last = []
        remainder = len(self.items) % self.page_size
        if remainder == 0:
            last.clear()
            for x in range(-1, -remainder-1):
                last.append(list[x])
        elif remainder == 1:
            last.clear()
            for x in range(-1, -remainder):
                last.append(list[x])
        elif remainder == 2:
            last.clear()
            for x in range(-1, -remainder+1):
                last.append(list[x])
        elif remainder == 3:
            last.clear()
            for x in range(-1, -remainder+2):
                last.append(list[x])


alphabet_list = list("abcdefghijklmnopqrstuvwxyz")

p = Test(alphabet_list, 4)
p.get_visible_items()
