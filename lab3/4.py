class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 添加元素到链表末尾
    def append(self, data):     #new_node,current都是节点
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 删除链表中指定值的元素
    def delete(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    # 修改链表中指定值的元素
    def update(self, old_value, new_value):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
            current = current.next

    # 按值查找元素
    def search(self, value):
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    # 按索引查找元素
    def get_at_index(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            current = current.next
            count += 1
        return None

    # 打印链表
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# 创建一个链表并进行操作示例
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    print("初始链表:")
    linked_list.display()

    linked_list.delete(2)
    print("删除值为2的元素后:")
    linked_list.display()

    linked_list.update(3, 4)
    print("将值为3的元素更新为4后:")
    linked_list.display()

    found_node = linked_list.search(4)
    if found_node:
        print(f"查找到值为4的元素: {found_node.data}")
    else:
        print("未找到值为4的元素")

    index_node = linked_list.get_at_index(1)
    if index_node:
        print(f"索引为1的元素为: {index_node.data}")
    else:
        print("未找到索引为1的元素")
