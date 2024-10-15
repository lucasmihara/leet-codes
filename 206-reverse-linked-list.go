/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	var next *ListNode
	var previous *ListNode = nil
	for ;; {
		next = head.Next
		head.Next = previous	
		if next == nil {
			return head
		}
		previous = head
		head = next
	}
	return head
 }