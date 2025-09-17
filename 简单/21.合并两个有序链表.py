"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：

输入：l1 = [], l2 = []
输出：[]
示例 3：

输入：l1 = [], l2 = [0]
输出：[0]


提示：

两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
"""
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass

def list_to_list_node(list1: list) -> Optional[ListNode] | None:
    """列表转换链表"""
    if not list1:
        return None
    head = ListNode(list1[0])
    curr = head
    for item in list1[1:]:
        curr.next = ListNode(item)
        curr = curr.next
    return head

if __name__ == '__main__':
    # 测试用例
    # s = Solution()
    # s.mergeTwoLists(list1=None, list2=None)
    # s = [1,2,3,4]
    # l1 = list_to_list_node(s)
    # print(l1.val)
    pass