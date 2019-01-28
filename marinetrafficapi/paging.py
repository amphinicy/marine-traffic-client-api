class Paging(object):

    def __init__(self, paging_data):
        self.paging_data = paging_data

    def has_next(self):
        if int(self.paging_data['page']) == int(self.paging_data['pages']):
            return False
        else:
            return True

    def has_previous(self):
        if int(self.paging_data['page']) == 1:
            return False
        else:
            return True

    def next(self):
        if self.has_next():
            return int(self.paging_data['page'])+1
        else:
            return False

    def previous(self):
        if self.has_previous():
            return int(self.paging_data['page'])-1
        else:
            return False
