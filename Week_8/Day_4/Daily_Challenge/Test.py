
counter = 0
last = []
listing = []


class Pagination:
    def __init__(self, items, page_size=10):
        self.items = items
        self.page_size = page_size
        self.current_page = []
        self.counter = counter

    def get_visible_items(self):
        if self.counter == 0:
            for x in range(self.page_size):
                listing.append(self.items[x])
            print("get visible item" + str(listing))
        else:
            print("get visible", str(self.current_page))

    def next_page(self):
        # print(self.counter, "h", len(self.items))
        if self.counter < len(self.items) - self.page_size:
            self.counter += self.page_size
            next_items = self.items[0 + self.counter:self.page_size + self.counter:1]
            self.current_page = next_items
        print(self.counter, "h", len(self.items) - self.page_size)

    def prev_page(self):
        if self.counter > self.page_size:
            # print(self.counter)
            self.counter -= self.page_size
            # prev_items = self.items[self.counter - self.page_size:self.counter:1]
            # print(self.counter)
            prev_items = self.items[self.counter - self.page_size:self.counter:1]
            self.current_page = prev_items

    def first_page(self):
        print("first page: " + str(self.items[:self.page_size]))

    def last(self):

        remainder = len(self.items) % self.page_size
        if remainder == 0:
            self.current_page = (self.items[-abs(remainder + self.page_size):])
        else:
            self.current_page = (self.items[-abs(remainder):])

    def go_to_page_num(self, page_num):
        if page_num == round(len(self.items)/self.page_size):
            self.counter = page_num*self.page_size
            print(round(len(self.items)/self.page_size), "n", page_num*self.page_size)
        elif page_num == round(len(self.items)/self.page_size) - 1:
            print("q", page_num, round(len(self.items)/self.page_size) - 1)
            self.counter = page_num*self.p
        else:
            pass

        if page_num == 0 or page_num < round(len(self.items) / self.page_size):
            self.current_page = (self.items[(page_num - 1) * self.page_size:page_num * self.page_size: 1])
        elif page_num < 0:
            pass
        else:
            remainder = len(self.items) % self.page_size
            self.current_page = (self.items[-abs(remainder):])


alphabet_list = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabet_list)

p.next_page()
p.get_visible_items()

p.next_page()
p.get_visible_items()