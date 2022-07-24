
counter = 0
last = []
listing = []


class Pagination:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
        self.counter = counter

    def get_visible_items(self):
        for x in range(self.page_size):
            listing.append(self.items[x])
        print("get visible item" + str(listing))

    def next_page(self):
        if self.counter < len(self.items) - self.page_size:
            self.counter += self.page_size
            next_items = self.items[0 + self.counter:self.page_size + self.counter:1]
            print("next page: " + str(next_items))

    def prev_page(self):
        if self.counter >= self.page_size:
            # self.counter -= self.page_size
            # prev_items = self.items[self.counter - self.page_size:self.counter:1]
            prev_items = self.items[self.counter - self.page_size:self.counter:1]
            print("previous page: " + str(prev_items))

    def first_page(self):
        print("first page: " + str(self.items[:self.page_size]))

    def last(self):
        remainder = len(self.items) % self.page_size
        if remainder == 0:
            print("last page: " + str(self.items[-abs(remainder + self.page_size):]))
        else:
            print("last page: " + str(self.items[-abs(remainder):]))


alphabet_list = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabet_list, 4)
# p.get_visible_items()
# p.first_page()

p.next_page()
p.next_page()
p.prev_page()
p.next_page()
# p.next_page()
# p.next_page()
# p.next_page()
