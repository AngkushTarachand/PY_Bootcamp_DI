class Pagination:
    def __int__(self, items, page_size=10):
        self.items = []
        self.page_size = page_size

    def get_visible_items(self):
        for x in range(self.page_size):
            print(self.items[x])

    def prev_page(self):
        print(self.items)

    def first_page(self):
        for f in range(0, self.page_size):
            print(self.items[f])

    def last(self):
        last = []
        remainder = len(self.items) % self.page_size
        if remainder is 0:
            last.clear()
            for x in range(-1, -remainder-1):
                last.append(list[x])
        elif remainder is 1:
            last.clear()
            for x in range(-1, -remainder):
                last.append(list[x])
        elif remainder is 2:
            last.clear()
            for x in range(-1, -remainder+1):
                last.append(list[x])
        elif remainder is 3:
            last.clear()
            for x in range(-1, remainder+2):
                last.append(list[x])


alphabet_list = "abcdefghijklmnopqrstuvwxyz".split(',')

p = Pagination(alphabet_list, 4)
